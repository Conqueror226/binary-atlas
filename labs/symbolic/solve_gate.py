#!/usr/bin/env python3
"""Ask a symbolic executor for an input that reaches the gated path in tlv_lab.

Teaching script for an owned toy program. Requires angr in a virtual
environment inside your lab VM:  python3 -m venv venv && venv/bin/pip install angr

Usage: venv/bin/python solve_gate.py ./tlv_plain [output-file]
Build the target first:  cc -g -O0 -DFIXED tlv_lab.c -o tlv_plain
"""
import sys

import angr

try:  # standalone package in angr 9.x
    import claripy
except ModuleNotFoundError:  # bundled in newer angr releases
    from angr import claripy

GATED_RESULT = 0x7777
RECORD_SIZE = 10  # magic(4) + type(1) + len(1) + payload(4)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    project = angr.Project(sys.argv[1], auto_load_libs=False)
    symbol = project.loader.find_symbol("tlv_parse")
    if symbol is None:
        print("tlv_parse symbol not found: build with -g and do not strip.")
        return 2

    record = claripy.BVS("record", RECORD_SIZE * 8)
    buffer_address = 0x10000000
    state = project.factory.call_state(
        symbol.rebased_addr,
        buffer_address,
        RECORD_SIZE,
        add_options={angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,
                     angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},
    )
    state.memory.store(buffer_address, record)

    simulation = project.factory.simulation_manager(state)
    simulation.run()  # the toy has few paths; real targets need exploration limits

    print(f"paths that returned: {len(simulation.deadended)}; "
          f"errored: {len(simulation.errored)}")
    for finished in simulation.deadended:
        result = finished.regs.eax
        if finished.solver.satisfiable(extra_constraints=[result == GATED_RESULT]):
            finished.add_constraints(result == GATED_RESULT)
            data = finished.solver.eval(record, cast_to=bytes)
            print("candidate input (hex):", data.hex())
            if len(sys.argv) > 2:
                with open(sys.argv[2], "wb") as handle:
                    handle.write(data)
                print("written to", sys.argv[2])
            print("This is a solver model, not an observation. "
                  "Run the real binary on it and record the actual result.")
            return 0
    print("No returned path can produce the gated result under this setup.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
