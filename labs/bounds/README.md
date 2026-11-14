# Reason about lengths & lifetimes

Status: starter exercise; not completed portfolio work.

Identify which data is valid to access and which assumptions need explicit checks.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Use memory.c from the previous exercise. Explain why indexes 0 through 3 are valid and index 4 is outside the array. Do not perform the invalid read in this exercise.

2. Write a checked accessor that accepts a pointer, a size, and an index and rejects an index outside the range.

3. Review signed versus unsigned comparisons and local object lifetimes. Record one uncertainty and look it up before marking this complete.

## Evidence and validation

- A checked accessor with boundary tests
- A lifetime explanation
- An unresolved question or a source-supported resolution

## Learning output

A small bounds-checked function and an explicit ownership explanation.

## Resource

[GNU C introduction](https://www.gnu.org/software/c-intro-and-ref/manual/html_node/index.html)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
