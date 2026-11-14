#!/usr/bin/env python3
"""List the functions whose instructions differ between two builds of a program.

Teaching script for owned toy binaries (GNU objdump, unstripped builds made
with the same compiler and flags). Standard library only.

Addresses and symbol offsets are masked so that code which merely moved is
not reported as changed. This is a coarse first pass: a matching fingerprint
does not prove two functions behave the same, and inlining or different
compiler flags will make almost everything look changed.

Usage: python3 funcdiff.py OLD_BINARY NEW_BINARY [--show FUNCTION]
"""
import difflib
import hashlib
import re
import subprocess
import sys

FUNCTION = re.compile(r"^[0-9a-f]+ <([^>]+)>:$")
ADDRESS = re.compile(r"\b[0-9a-f]{3,16}\b(?= <)|0x[0-9a-f]+\(%rip\)|#.*$")
SYMBOL_OFFSET = re.compile(r"<([^>+]+)\+0x[0-9a-f]+>")


def functions(binary):
    listing = subprocess.run(["objdump", "-d", "--no-show-raw-insn", binary],
                             check=True, capture_output=True, text=True).stdout
    table, current = {}, None
    for line in listing.splitlines():
        header = FUNCTION.match(line.strip())
        if header:
            current = header.group(1)
            table[current] = []
        elif current and ":" in line:
            instruction = line.split(":", 1)[1].strip()
            instruction = SYMBOL_OFFSET.sub(r"<\1+OFF>", ADDRESS.sub("ADDR", instruction))
            if instruction:
                table[current].append(" ".join(instruction.split()))
    return table


def fingerprint(lines):
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()[:16]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        return 2
    old, new = functions(args[0]), functions(args[1])
    changed = sorted(name for name in old.keys() & new.keys() if fingerprint(old[name]) != fingerprint(new[name]))
    print(f"functions compared: {len(old.keys() & new.keys())}")
    print("changed:", ", ".join(changed) or "none")
    print("only in old:", ", ".join(sorted(old.keys() - new.keys())) or "none")
    print("only in new:", ", ".join(sorted(new.keys() - old.keys())) or "none")
    if "--show" in sys.argv:
        name = sys.argv[sys.argv.index("--show") + 1]
        if name not in old or name not in new:
            sys.exit(f"{name} is not present in both builds")
        print("\n".join(difflib.unified_diff(old[name], new[name], "old/" + name, "new/" + name, lineterm="")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
