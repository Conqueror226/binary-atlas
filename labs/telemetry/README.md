# Connect binary behavior to telemetry

Status: starter exercise; not completed portfolio work.

Relate one observed benign program action to a source-backed event without overstating causality.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. In an optional isolated Windows lab, compile a benign program that opens a local text file. Record source, binary hash, time zone, and execution time. Do not assume the Linux sample produces Windows telemetry.

2. Choose available logs and document the audit policy and collection configuration. Event 4624 concerns logon context; it does not prove a function call, file access, or malicious behavior. Process telemetry availability depends on configuration.

3. If your isolated monitoring lab includes Security Onion, correlate only the records actually collected. In Neo4j, label evidence-derived relationships separately from hypotheses and preserve source record references.

## Evidence and validation

- Lab and telemetry collection configuration
- Timestamped source event references
- An evidence graph with alternative explanations

## Learning output

A bounded behavior-to-event correlation, or an honest record of missing telemetry.

## Resource

[Windows event 4624](https://learn.microsoft.com/windows/security/threat-protection/auditing/event-4624)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
