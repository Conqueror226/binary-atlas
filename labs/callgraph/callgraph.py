#!/usr/bin/env python3
"""Build a direct-call graph from `objdump -d` and answer a reachability question.

Teaching script for owned toy binaries (x86-64 ELF, GNU objdump). Standard library only.

Usage:
  python3 callgraph.py ./reach --source main --target legacy_decode
  python3 callgraph.py ./reach --cypher graph.cypher     # optional Neo4j import

The answer has three values, never two:
  REACHABLE      a chain of direct calls exists
  NOT SHOWN      no direct chain, and no indirect call could hide one
  UNKNOWN        no direct chain, but an indirect call is reachable from the source
"""
import argparse
import collections
import re
import subprocess
import sys

FUNCTION = re.compile(r"^[0-9a-f]+ <([^>]+)>:$")
DIRECT = re.compile(r"\bcall\w*\s+[0-9a-f]+ <([^>+]+)(?:\+0x[0-9a-f]+)?>")
INDIRECT = re.compile(r"\bcall\w*\s+\*")
TAIL = re.compile(r"\bjmp\w*\s+[0-9a-f]+ <([^>+]+)>$")


def build_graph(binary):
    listing = subprocess.run(["objdump", "-d", "--no-show-raw-insn", binary],
                             check=True, capture_output=True, text=True).stdout
    edges = collections.defaultdict(set)
    indirect = collections.Counter()
    current = None
    for line in listing.splitlines():
        header = FUNCTION.match(line.strip())
        if header:
            current = header.group(1)
            edges.setdefault(current, set())
            continue
        if current is None:
            continue
        direct = DIRECT.search(line) or TAIL.search(line.strip())
        if direct and direct.group(1) != current:
            edges[current].add(direct.group(1))
        elif INDIRECT.search(line):
            indirect[current] += 1
    return edges, indirect


def reachable_from(edges, source):
    parent = {source: None}
    queue = collections.deque([source])
    while queue:
        node = queue.popleft()
        for callee in sorted(edges.get(node, ())):
            if callee not in parent:
                parent[callee] = node
                queue.append(callee)
    return parent


def chain(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return " -> ".join(reversed(path))


def write_cypher(path, edges, indirect):
    quote = lambda name: name.replace("\\", "\\\\").replace("'", "\\'")
    with open(path, "w") as out:
        for name in sorted(edges):
            out.write(f"MERGE (:Function {{name:'{quote(name)}', indirect_calls:{indirect[name]}}});\n")
        for caller in sorted(edges):
            for callee in sorted(edges[caller]):
                out.write(f"MATCH (a:Function {{name:'{quote(caller)}'}}),(b:Function {{name:'{quote(callee)}'}}) "
                          "MERGE (a)-[:CALLS {kind:'direct', evidence:'objdump'}]->(b);\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("binary")
    parser.add_argument("--source", default="main")
    parser.add_argument("--target")
    parser.add_argument("--cypher")
    args = parser.parse_args()

    edges, indirect = build_graph(args.binary)
    if args.source not in edges:
        sys.exit(f"source function {args.source!r} not found (stripped binary?)")
    parent = reachable_from(edges, args.source)
    hiding = sorted(name for name in parent if indirect[name])

    print(f"functions: {len(edges)}  direct edges: {sum(map(len, edges.values()))}  "
          f"indirect call sites: {sum(indirect.values())}")
    print(f"reachable from {args.source} by direct calls: {len(parent)}")
    if hiding:
        print("indirect call sites reachable from source (targets unresolved):", ", ".join(hiding))
    if args.target:
        if args.target not in edges:
            sys.exit(f"target function {args.target!r} not found")
        if args.target in parent:
            print("verdict: REACHABLE  ", chain(parent, args.target))
        elif hiding:
            print("verdict: UNKNOWN  no direct chain; an indirect call could reach it. Resolve with a debugger or data-flow analysis.")
        else:
            print("verdict: NOT SHOWN  no direct chain and no reachable indirect call in this graph.")
    if args.cypher:
        write_cypher(args.cypher, edges, indirect)
        print("wrote", args.cypher)


if __name__ == "__main__":
    main()
