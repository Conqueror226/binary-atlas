# Create a reproducible lab baseline

Status: starter exercise; not completed portfolio work.

Build an isolated environment for your own benign C programs and make it recoverable.

Scope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.

## Investigation steps

1. Work through the Lab setup checklist. Choose a Linux VM for the first C/GDB exercises. A later Windows VM is optional for PE and event correlation.

2. Record host architecture, guest OS, compiler, debugger, and tool versions. If your host uses ARM, select an appropriate x86-64 environment or record an architecture change; these exercises assume x86-64.

3. Install from official sources, then take a clean snapshot. Disconnect networking before program execution. Record the snapshot name and date.

## Evidence and validation

- Environment and version inventory
- Network mode and isolation notes
- A named clean snapshot

## Learning output

A documented environment you can restore.

## Resource

[GNU Debugger](https://sourceware.org/gdb/current/onlinedocs/)

Use the website lab page for the worked solution and concept links. Preserve your own actual results separately.
