from PySpice.Spice.Parser import SpiceParser
from PySpice.Unit import *
from pathlib import Path

netlist = Path('bjt.cir').read_text()
parser = SpiceParser(source=netlist)
circuit = parser.build_circuit()
simulator = circuit.simulator()
analysis = simulator.transient(step_time=1@u_us, end_time=5@u_ms)
for v in analysis['out']:
    print(float(v))