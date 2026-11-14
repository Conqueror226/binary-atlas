# Measure what the fuzzer reached

Status: starter exercise; not completed portfolio work.

Replace "it ran for a minute" with a coverage measurement from repeated trials, and find the code the campaign never executed.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Build the repaired harness with source-based coverage. Run at least three trials that differ only in the seed, each into its own empty corpus directory and its own profile file.

2. Produce a coverage report per trial. Record line, region and branch coverage for each. Fuzzing is randomized: report every trial and the spread, never only the best one.

3. Open the annotated source and find the line with a zero count. Explain why random mutation rarely satisfies that condition. This uncovered line is the starting point for the symbolic execution exercise.

## Commands

```sh
clang -g -O1 -DFUZZ -DFIXED -fsanitize=fuzzer -fprofile-instr-generate -fcoverage-mapping tlv_lab.c -o tlv_cov
for t in 1 2 3; do
  mkdir -p trial$t
  LLVM_PROFILE_FILE=trial$t.profraw ./tlv_cov trial$t -seed=$t -max_total_time=30
  llvm-profdata merge -o trial$t.profdata trial$t.profraw
  llvm-cov report ./tlv_cov -instr-profile=trial$t.profdata
done
llvm-cov show ./tlv_cov -instr-profile=trial1.profdata tlv_lab.c
```

## Evidence and validation

- Coverage table for at least three trials with seeds and budgets
- The annotated source line that was not reached
- A note on variance between trials and on what coverage cannot tell you

## Learning output

A small, honest evaluation: repeated trials, reported spread, and a named coverage gap.

## Resource

[Clang source-based coverage](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
