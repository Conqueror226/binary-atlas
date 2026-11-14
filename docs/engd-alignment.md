# EngD alignment review

Reviewed 14 November 2026. This document explains why the learning path was extended and how the workspace maps to an engineering doctorate (EngD) on low-level binary analysis for automated vulnerability research. Nothing here records an achievement.

## What is known about the target position

Source for all three: programme correspondence dated 5 November 2026.

- An EngD position in security is expected around the end of 2027 or the beginning of 2028.
- Its focus is low-level binary analysis for automated vulnerability research.
- No EngD projects on security monitoring were available at the time of the inquiry.

Not known: industry partner, target platforms, expected tooling, selection criteria, opening date, application procedure, funding terms, and whether a candidate can shape the scope. These stay listed as unknown on the site until a sourced answer exists.

## Review of the original approach

| Area | Original state | Assessment | Change made |
| --- | --- | --- | --- |
| Foundations (stages 00–03) | C, memory, x86-64, Ghidra, GDB on owned toy programs | Sound and necessary. Kept unchanged. | None |
| Vulnerability research (stage 04) | One manual sanitizer triage and repair; fuzzing only as optional reading | Too manual for a position whose title contains "automated" | New stage 06 with fuzzing, coverage, symbolic execution |
| Program analysis | Not covered | The largest gap: no control-flow or call graphs, no solver-based reasoning | Call-graph reachability and symbolic execution exercises with tested scripts |
| Evaluation method | Clean reruns and bounded claims | Good for single investigations, missing for randomized tools | Repeated trials, variance and baselines in the coverage exercise and concept library |
| Industrial feasibility | Telemetry correlation only | An EngD is judged on a design that works in an organization | New stage 07: hardening inventory, patch verification, crash triage, design brief |
| Reuse of background | Bridges stated per stage | Present but generic | Thesis graph reasoning mapped to call-graph reachability; administration experience mapped to operational requirements |
| Research direction | "Future research focus" unknown | Nothing to discuss with a supervisor | Four candidate directions on the EngD alignment page, labelled as not reviewed |
| Evidence standards | Unknown preserved, no seeded achievements | The strongest part of the workspace | Extended: three-valued reachability verdicts, "unknown" in the hardening audit, empty analyst columns in triage |
| Resource link checks | One hardcoded date for all | Could not stay true as resources are added | Per-resource check date; unchecked links say so |

## How the new exercises were checked

The new teaching sources and scripts were compiled and run once during authoring on x86-64 Linux with Clang 18.1.3, GNU binutils and angr 10.0.7. That confirms the commands work on one toolchain. It is not a result for the portfolio: run them in your own lab and record your own versions and outputs.

Eleven of the thirteen new resource links could not be opened from the authoring environment and are marked "not yet checked". Open each one, then set its `verified` date in `site/data.js`.

## Candidate directions

See the EngD alignment page on the site. In short:

1. Reachability-aware vulnerability triage for third-party binaries. Extends the thesis graph work.
2. Sustainable automated vulnerability discovery for small engineering teams. Extends the SME focus.
3. Binary-level assurance evidence for product security obligations. Builds on administration and inventory experience.
4. From binary root cause to detection content. Keeps the security monitoring background in play.

None has been discussed with a supervisor or company.

## Suggested order of work

1. Finish stages 00–04 with real evidence and publish one clean-rerun investigation.
2. Work through stage 06. Publish the fuzzing and coverage results as a second investigation.
3. Do the call-graph exercise and decide whether direction 1 holds your interest.
4. Write one design brief with `portfolio/templates/engd-design-brief.md` and have someone challenge it.
5. Then contact the programme again with one specific question and links to the evidence.
