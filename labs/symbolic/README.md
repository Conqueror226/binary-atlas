# Solve a path condition with symbolic execution

Status: starter exercise; not completed portfolio work.

Ask a solver for an input that reaches the gated path the fuzzer missed, then confirm the answer on the real binary.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Create a Python virtual environment in your lab VM and install angr from the official package index while the network is still attached. Record the version: the API differs between major releases.

2. Read solve_gate.py before running it. It starts at tlv_parse with ten symbolic bytes, explores every path of this small function and asks whether any return value can equal the gated result. Build the plain target and run the script.

3. The solver output is a model, not an observation. Run the real binary on the generated file and record the actual result. Then write down why this worked here and would not scale unchanged: few paths, no loops over symbolic lengths, no system calls.

## Commands

```sh
python3 -m venv venv && venv/bin/pip install angr
cc -g -O0 -DFIXED tlv_lab.c -o tlv_plain
venv/bin/python solve_gate.py ./tlv_plain gate.bin
./tlv_plain gate.bin
sha256sum tlv_plain gate.bin
```

## Lab scripts

- [solve_gate.py](solve_gate.py)

Read each script before running it. Its header states assumptions and limits.

## Evidence and validation

- angr version and the exact script invocation
- The candidate input (hex) and the real binary’s output on it
- Two limits of the approach, in your own words

## Learning output

One solver-generated input, confirmed by execution, with the technique’s limits stated.

## Resource

[angr](https://docs.angr.io/)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
