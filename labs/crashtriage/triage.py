#!/usr/bin/env python3
"""Group fuzzer crash files into buckets by replaying them under AddressSanitizer.

Teaching script for an owned toy program. Standard library only.
A bucket is (sanitizer error type, access type, top frames inside the program).
Buckets are a triage aid: two inputs in one bucket probably share a root cause,
but only root-cause analysis can confirm it, and one root cause can also
appear in several buckets.

Usage: python3 triage.py ./tlv_asan CRASH_DIR [--frames 3] [--csv buckets.csv]
Build the replay target first:
  clang -g -O1 -fsanitize=address -fno-omit-frame-pointer tlv_lab.c -o tlv_asan
"""
import argparse
import collections
import csv
import hashlib
import pathlib
import re
import subprocess

ERROR = re.compile(r"ERROR: AddressSanitizer: ([\w-]+)")
ACCESS = re.compile(r"^(READ|WRITE) of size (\d+)", re.M)
FRAME = re.compile(r"^\s+#\d+ 0x[0-9a-f]+ in (\S+) (\S+)", re.M)
RUNTIME = ("__asan", "__interceptor", "__sanitizer", "__libc_start", "_start")


def replay(binary, path, depth):
    try:
        run = subprocess.run([binary, str(path)], capture_output=True, text=True, timeout=10)
    except subprocess.TimeoutExpired:
        return ("timeout", "-", ()), ""
    report = run.stderr
    error = ERROR.search(report)
    if not error:
        return ("no-sanitizer-report (exit %d)" % run.returncode, "-", ()), report
    access = ACCESS.search(report)
    frames = [name for name, _ in FRAME.findall(report.split("\n\n")[0])
              if not name.startswith(RUNTIME)]
    return (error.group(1), access.group(1) if access else "-", tuple(frames[:depth])), report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("binary")
    parser.add_argument("crash_dir")
    parser.add_argument("--frames", type=int, default=3)
    parser.add_argument("--csv")
    args = parser.parse_args()

    buckets = collections.defaultdict(list)
    for path in sorted(pathlib.Path(args.crash_dir).iterdir()):
        if path.is_file():
            key, _ = replay(args.binary, path, args.frames)
            buckets[key].append(path)

    rows = []
    for (error, access, frames), files in sorted(buckets.items(), key=lambda item: -len(item[1])):
        bucket_id = hashlib.sha256(repr((error, access, frames)).encode()).hexdigest()[:10]
        smallest = min(files, key=lambda p: p.stat().st_size)
        rows.append([bucket_id, error, access, " < ".join(frames) or "-", len(files), smallest.name])
        print(f"bucket {bucket_id}  {error} {access}  frames: {' < '.join(frames) or '-'}")
        print(f"  inputs: {len(files)}  smallest: {smallest.name} ({smallest.stat().st_size} bytes)")
    print(f"{sum(len(f) for f in buckets.values())} inputs -> {len(buckets)} buckets")
    if args.csv:
        with open(args.csv, "w", newline="") as out:
            writer = csv.writer(out)
            writer.writerow(["bucket", "error", "access", "frames", "inputs", "smallest_input",
                             "cwe (analyst)", "root cause (analyst)", "priority (analyst)"])
            writer.writerows(row + ["", "", ""] for row in rows)
        print("wrote", args.csv, "- analyst columns are left empty on purpose")


if __name__ == "__main__":
    main()
