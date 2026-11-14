# Follow four bytes through C

Status: starter exercise; not completed portfolio work.

Explain the difference between an array, a pointer, and the bytes a program reads.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Download memory.c and read it before compiling. Predict the two printed values and the array size.

2. In your lab VM, compile with debug symbols using the command below. Run your own program and compare your prediction.

3. Draw the four bytes, then change a value safely within the array. Explain why a pointer does not carry the array length.

## Commands

```sh
cc -g -O0 -Wall -Wextra memory.c -o memory
./memory
sha256sum memory.c memory
```

## Evidence and validation

- Source hash and compiler version
- Predicted and observed output
- A memory sketch with array bounds

## Learning output

A four-byte memory sketch supported by observed output.

## Resource

[Compiler Explorer](https://godbolt.org/)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
