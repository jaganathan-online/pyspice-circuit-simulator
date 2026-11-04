# PySpice Simulation Task

2-stage BJT amplifier simulation that works both in `ngspice` and `PySpice`.

## Project Structure

```
.
├── bjt.cir            # SPICE netlist (compatible with ngspice + PySpice)
├── sim.py             # PySpice - loads bjt.cir as source and prints v(nout)
├── requirements.txt
└── README.md
```

## Prerequisites - Linux (Ubuntu)

System library `libngspice` is required - it's not pip installable.

```bash
sudo apt update
sudo apt install ngspice libngspice0 libngspice0-dev python3-venv
```

Fix PySpice library lookup (Ubuntu installs `libngspice.so.0` not `libngspice.so`):

```bash
ls /usr/lib/x86_64-linux-gnu/libngspice*
# if you only see libngspice.so.0
sudo ln -sf /usr/lib/x86_64-linux-gnu/libngspice.so.0 /usr/lib/x86_64-linux-gnu/libngspice.so
```

## Setup

```bash
git clone <your-repo-url>
cd pyspice-simulation-task

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

**requirements.txt**

```
PySpice==1.5
numpy==1.22
cffi==1.15
```

## Usage

### 1. Run with ngspice directly

```bash
ngspice -b bjt.cir
# or interactive
ngspice bjt.cir
```

In interactive mode:

```
> run
> print v(nout)
> quit
```

### 2. Run with PySpice (prints only output in terminal)

`sim.py`:

```python
from pathlib import Path
from PySpice.Spice.Parser import SpiceParser

source = Path('bjt.cir').read_text()
parser = SpiceParser(source=source)
circuit = parser.build_circuit()
simulator = circuit.simulator()
analysis = simulator.transient(step_time=1e-6, end_time=5e-3)

for v in analysis['nout']:
    print(float(v))
```

Run:

```bash
python3 sim.py
```