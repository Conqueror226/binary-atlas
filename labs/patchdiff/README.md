# Verify a repair at binary level

Status: starter exercise; not completed portfolio work.

Show from two binaries alone which function a fix changed, and connect the changed instructions to the source-level bounds check.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Build the flawed program and the build with defect A repaired, using identical compiler and flags. Record both hashes.

2. Run funcdiff.py. It should report exactly one changed function. Use --show to print the instruction-level difference and identify the added comparison and branch.

3. Rebuild the old source a second time and diff it against the first build to confirm the tool reports no change. Then change only the optimization level and observe how much "changes". State what this tells you about comparing vendor binaries built with unknown flags.

## Commands

```sh
cc -g -O1 tlv_lab.c -o tlv_old
cc -g -O1 -DFIX_A tlv_lab.c -o tlv_new
sha256sum tlv_old tlv_new
python3 funcdiff.py tlv_old tlv_new --show tlv_parse
cc -g -O1 tlv_lab.c -o tlv_rebuild
python3 funcdiff.py tlv_old tlv_rebuild
cc -g -O2 tlv_lab.c -o tlv_o2
python3 funcdiff.py tlv_old tlv_o2
```

## Lab scripts

- [funcdiff.py](funcdiff.py)

Read each script before running it. Its header states assumptions and limits.

## Evidence and validation

- Hashes and build commands for each binary
- The function-level diff and your annotation of the added check
- The control comparison (identical rebuild) and the flag-change comparison

## Learning output

A binary-level confirmation that a specific fix is present, with a control and a stated limit.

## Resource

[Ghidra repository](https://github.com/NationalSecurityAgency/ghidra)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
