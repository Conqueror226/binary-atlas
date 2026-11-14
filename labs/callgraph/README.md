# Answer a reachability question on a call graph

Status: starter exercise; not completed portfolio work.

Decide whether a flagged function can be reached from the program entry, and keep "unknown" as a legitimate answer when the graph is incomplete.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Read reach.c. legacy_decode stands for a function a scanner has flagged. Predict, from the source, whether main can reach it. Then build the binary and run callgraph.py with main as source and legacy_decode as target.

2. The script reports UNKNOWN, not "unreachable": dispatch contains an indirect call whose targets a direct-call graph cannot see. Resolve it with evidence: break on legacy_decode in GDB, run the program with one and with two arguments, and record which run reaches it.

3. Optional: export the graph with --cypher and load it into Neo4j. Add the edge you observed in the debugger as a separate relationship type with its evidence source, so recovered and observed edges stay distinguishable.

## Commands

```sh
cc -g -O1 -Wall -Wextra reach.c -o reach
python3 callgraph.py ./reach --source main --target legacy_decode
python3 callgraph.py ./reach --source main --target audit_log
gdb -batch -ex "break legacy_decode" -ex "run" -ex "bt" --args ./reach atlas
gdb -batch -ex "break legacy_decode" -ex "run" -ex "bt" --args ./reach atlas second
python3 callgraph.py ./reach --cypher graph.cypher
```

## Lab scripts

- [callgraph.py](callgraph.py)

Read each script before running it. Its header states assumptions and limits.

## Evidence and validation

- Script output with the three-valued verdict
- Debugger evidence that resolves the indirect call for specific inputs
- A note on what static call graphs over- and under-approximate

## Learning output

A reachability verdict backed by static and dynamic evidence, with unresolved edges labelled.

## Resource

[Ghidra repository](https://github.com/NationalSecurityAgency/ghidra)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
