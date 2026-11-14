# Trace a function call

Status: starter exercise; not completed portfolio work.

Observe arguments and return values under a named ABI.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Use your own branch.c build. In Linux x86-64 System V, start by inspecting the first integer argument in edi and the integer result in eax. This differs from Windows x64, whose first integer argument uses ecx.

2. Break at classify, inspect registers, step, and record how the return value reaches the caller. Optimization may inline or remove the call; use the -O0 build.

3. Create a tiny second function with two arguments. Record which registers you observe rather than applying one ABI to every platform.

## Evidence and validation

- Architecture and ABI label
- A register trace for one call
- One ABI-specific limitation

## Learning output

A call trace with context sufficient for another learner to reproduce it.

## Resource

[Intel architecture manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
