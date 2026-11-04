from PySpice.Spice.Parser import SpiceParser
from PySpice.Unit import *
from pathlib import Path
import argparse
argp = argparse.ArgumentParser(description="Run PySpice transient on a .cir file")
argp.add_argument("netlist_path", nargs="?", default="bjt.cir")
args = argp.parse_args()
netlist = Path(args.netlist_path).read_text()
parser = SpiceParser(source=netlist)
netlist = Path('bjt.cir').read_text()
parser = SpiceParser(source=netlist)
circuit = parser.build_circuit()
simulator = circuit.simulator()
analysis = simulator.transient(step_time=1@u_us, end_time=5@u_ms)
for v in analysis['out']:
    print(float(v))