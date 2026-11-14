#!/usr/bin/env python3
"""Report build-hardening properties of ELF binaries using `readelf`.

Teaching script (x86-64 Linux ELF, GNU binutils). Standard library only.
Each property is reported as yes / no / partial / unknown. "unknown" is kept
when the evidence is missing (for example, symbol-based checks on a stripped
binary); it is never converted into a pass or a fail.

Usage: python3 hardening_audit.py [--json] BINARY [BINARY ...]
"""
import json
import subprocess
import sys


def readelf(flag, path):
    return subprocess.run(["readelf", "-W", flag, path], capture_output=True, text=True).stdout


def audit(path):
    header = readelf("-h", path)
    if "ELF Header" not in header:
        return {"file": path, "error": "not an ELF file readelf can parse"}
    segments = readelf("-l", path)
    dynamic = readelf("-d", path)
    symbols = readelf("--dyn-syms", path) + readelf("-s", path)
    has_symbols = "Symbol table" in symbols
    result = {"file": path}

    if "Type:" in header and "DYN" in header:
        result["pie"] = "yes" if "(DEBUG)" in dynamic or "PIE" in dynamic else "unknown (shared object or PIE)"
    else:
        result["pie"] = "no"

    stack = [line for line in segments.splitlines() if "GNU_STACK" in line]
    result["nx_stack"] = "unknown" if not stack else ("no" if "RWE" in stack[0] else "yes")

    if "GNU_RELRO" not in segments:
        result["relro"] = "no"
    else:
        result["relro"] = "yes" if "BIND_NOW" in dynamic or " NOW" in dynamic else "partial"

    if not has_symbols:
        result["stack_protector"] = result["fortify"] = "unknown (no symbols)"
    else:
        result["stack_protector"] = "yes" if "__stack_chk_fail" in symbols else "not observed"
        result["fortify"] = "yes" if "_chk@" in symbols or "_chk\n" in symbols else "not observed"
    result["stripped"] = "no" if ".symtab" in readelf("-S", path) else "yes"
    return result


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    if not args:
        print(__doc__)
        return 2
    rows = [audit(path) for path in args]
    if "--json" in sys.argv:
        print(json.dumps(rows, indent=2))
        return 0
    keys = ["pie", "nx_stack", "relro", "stack_protector", "fortify", "stripped"]
    for row in rows:
        print(row["file"])
        if "error" in row:
            print("  error:", row["error"])
            continue
        for key in keys:
            print(f"  {key:16} {row[key]}")
    print('\n"not observed" means the marker symbol is absent: the option may be off, '
          "or the compiler found nothing to protect.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
