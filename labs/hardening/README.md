# Audit build hardening across binaries

Status: starter exercise; not completed portfolio work.

Produce a hardening inventory for a set of binaries and report missing evidence as unknown rather than as a pass or a fail.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Build tlv_lab.c twice: once with common hardening options and once with them disabled. Strip a copy of the hardened build. Predict which properties each binary will show.

2. Run hardening_audit.py on all three and on one system library. Compare with your prediction. Read the script to see which readelf fact supports each verdict, and where it answers unknown or "not observed".

3. Explain each property in one line for a non-specialist reader: what it makes harder, and what it does not prevent. A hardened build of a flawed parser still contains the flaw.

## Commands

```sh
cc -O2 -fstack-protector-strong -D_FORTIFY_SOURCE=2 -fPIE -pie -Wl,-z,relro,-z,now tlv_lab.c -o tlv_hard
cc -O0 -fno-stack-protector -no-pie -Wl,-z,norelro -z execstack tlv_lab.c -o tlv_soft
strip -o tlv_hard_stripped tlv_hard
python3 hardening_audit.py tlv_hard tlv_soft tlv_hard_stripped
python3 hardening_audit.py --json tlv_hard tlv_soft > inventory.json
```

## Lab scripts

- [hardening_audit.py](hardening_audit.py)

Read each script before running it. Its header states assumptions and limits.

## Evidence and validation

- Exact build commands and tool versions
- The audit output (text or JSON) for every binary
- A short plain-language explanation of each property and its limits

## Learning output

A reproducible hardening inventory that a reviewer can re-run, with unknowns preserved.

## Resource

[OpenSSF compiler hardening guide](https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.html)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
