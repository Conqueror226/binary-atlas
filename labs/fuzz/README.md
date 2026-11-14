# Fuzz an owned parser with a time budget

Status: starter exercise; not completed portfolio work.

Run a coverage-guided fuzzer against a deliberately flawed record parser and learn why fixing one defect reveals the next.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Read tlv_lab.c first. Write down the record format, the two teaching defects (A and B) and the gated path in record type 3. Note the volatile sink in the harness: without it the optimizer may delete the call under test, and the fuzzer would report runs that test nothing.

2. Build the harness and fuzz with a fixed time budget and a recorded seed. Keep the crash file, the sanitizer summary and the exact command. Then rebuild with -DFIX_A and fuzz again: a second, different defect should become visible. Record how long each took in your run; do not copy times from anywhere else.

3. Rebuild with -DFIXED and run the same budget. A run without crashes covers that budget, that seed and that harness only. Write one sentence on what the campaign did not exercise.

## Commands

```sh
mkdir -p corpus crashes
printf 'ATLS\x01\x02\x0a\x14' > corpus/seed-valid
clang -g -O1 -DFUZZ -fsanitize=fuzzer,address -fno-omit-frame-pointer tlv_lab.c -o tlv_fuzz
./tlv_fuzz corpus -seed=1 -max_total_time=60 -artifact_prefix=crashes/
# Repair defect A only, then look for what it was hiding:
clang -g -O1 -DFUZZ -DFIX_A -fsanitize=fuzzer,address -fno-omit-frame-pointer tlv_lab.c -o tlv_fuzz_a
./tlv_fuzz_a corpus -seed=1 -max_total_time=60 -artifact_prefix=crashes/
# Both repaired:
clang -g -O1 -DFUZZ -DFIXED -fsanitize=fuzzer,address -fno-omit-frame-pointer tlv_lab.c -o tlv_fuzz_fixed
./tlv_fuzz_fixed corpus -seed=1 -max_total_time=60
```

## Evidence and validation

- Compiler and libFuzzer version, flags, seed and time budget for every run
- Crash inputs with SHA-256 and the sanitizer summary line for defects A and B
- A statement of what the clean run does and does not show

## Learning output

Two reproducible crash inputs with distinct causes, and a bounded statement about the repaired build.

## Resource

[LLVM libFuzzer](https://llvm.org/docs/LibFuzzer.html)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
