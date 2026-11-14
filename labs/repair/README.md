# Repair & regression-test the parser

Status: starter exercise; not completed portfolio work.

Show that a bounds check rejects truncation while preserving valid behavior.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. After the size == 0 check, reject length > size - 1. Keep the unsigned arithmetic safe by retaining that initial size check. Save the repaired source separately.

2. Repeat the valid and truncated cases under the sanitizer. Add empty input, a zero-length record, an exact-length record, and an over-declared length.

3. Record expected and observed results. A clean sanitizer run covers these inputs only. As an optional next step, read the official libFuzzer guide and design a bounded harness for this owned parser.

## Evidence and validation

- The minimal source diff
- Regression input/output table
- Remaining coverage gaps

## Learning output

A minimal repair, test table, and explicit coverage limits.

## Resource

[LLVM libFuzzer](https://llvm.org/docs/LibFuzzer.html)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
