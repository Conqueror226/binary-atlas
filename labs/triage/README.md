# Triage a toy parser bounds error

Status: starter exercise; not completed portfolio work.

Locate and explain an out-of-bounds read in a deliberately flawed program you own.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Read parser_lab.c. Identify the length-prefix assumption before running anything. Use only your isolated lab.

2. Compile with AddressSanitizer and run the fixed built-in test inputs. Capture the diagnostic and build context. Exact messages depend on your toolchain.

3. Trace the diagnostic to the unchecked length. Explain why a crash or sanitizer report is evidence of a defect but does not by itself establish exploitability or real-world impact.

## Commands

```sh
clang -g -O1 -fsanitize=address -fno-omit-frame-pointer parser_lab.c -o parser_lab
./parser_lab
```

## Evidence and validation

- Source and binary hashes
- A sanitizer diagnostic with versions
- Root cause with bounded impact claims

## Learning output

A reproducible defect report for a controlled teaching program.

## Resource

[AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
