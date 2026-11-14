# Reduce crashes to reviewed buckets

Status: starter exercise; not completed portfolio work.

Turn a directory of fuzzer crash files into a short list of distinct defects that an analyst has reviewed and classified.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Collect crash inputs from the fuzzing exercise: several from the flawed build and several from the build with only defect A repaired. Build the replay target with AddressSanitizer.

2. Run triage.py. It replays each file and groups them by error type, access type and top program frames. Compare the bucket count with the number of input files, and note the bucket for any file that produces no sanitizer report.

3. Fill the analyst columns of the CSV yourself: a CWE identifier you can justify from the root cause, the root cause in one sentence, and a priority with its reasoning. The script leaves these empty on purpose. Do not assign a severity score that implies reachability or impact you have not shown.

## Commands

```sh
clang -g -O1 -fsanitize=address -fno-omit-frame-pointer tlv_lab.c -o tlv_asan
python3 triage.py ./tlv_asan crashes --csv buckets.csv
cat buckets.csv
```

## Lab scripts

- [triage.py](triage.py)

Read each script before running it. Its header states assumptions and limits.

## Evidence and validation

- The crash set with hashes and the replay build command
- The bucket table before and after your analyst review
- For each bucket: root cause, justified CWE, and what remains unknown

## Learning output

A reviewed triage table: many inputs, few defects, each with a stated root cause and open questions.

## Resource

[CWE](https://cwe.mitre.org/)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
