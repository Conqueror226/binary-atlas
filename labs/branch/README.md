# Read your first branch

Status: starter exercise; not completed portfolio work.

Connect a C condition to machine instructions and verify the boundary input.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Download branch.c. Predict the results for values 15 and 16, then compile with debug symbols and no optimization.

2. Disassemble classify. Identify the compare, conditional branch, and return value. Your compiler output may differ from the illustrative trace in the workspace.

3. Recompile at -O2. Explain any change in instruction selection or inlining. Keep the compiler, target, ABI, and flags with both observations.

## Commands

```sh
cc -g -O0 -Wall -Wextra branch.c -o branch
./branch
objdump -d -M intel branch
cc -g -O2 branch.c -o branch-o2
```

## Evidence and validation

- Annotated disassembly for your exact build
- Boundary input observations
- A comparison of -O0 and -O2 with limitations

## Learning output

An annotated branch with a verified boundary condition.

## Resource

[OpenSecurityTraining2](https://p.ost2.fyi/courses/course-v1%3AOpenSecurityTraining2%2BArch1001_x86-64_Asm%2B2021_v1/)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
