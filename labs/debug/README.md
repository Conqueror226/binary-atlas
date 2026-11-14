# Test a static hypothesis in GDB

Status: starter exercise; not completed portfolio work.

Use dynamic evidence to confirm a specific claim about your own program.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Open the same hashed branch build with GDB. Set a breakpoint at classify and choose a known input.

2. Inspect the argument, step through the comparison, and record the result. Repeat with the boundary input on the other side.

3. Compare runtime evidence with your Ghidra hypothesis. State what you did not observe. Addresses may change between runs and builds.

## Commands

```sh
gdb ./branch
# Inside GDB:
break classify
run
info registers
disassemble classify
nexti
continue
```

## Evidence and validation

- Debugger version and commands
- Two input/output observations
- A claim revised or supported by execution

## Learning output

A hypothesis supported by two controlled observations.

## Resource

[GNU Debugger](https://sourceware.org/gdb/current/onlinedocs/)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
