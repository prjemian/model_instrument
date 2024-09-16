# instrument_template

Bluesky Data Acquisition in console, notebook, & queueserver.

## Demo

```py
from instrument.startup import *
from instrument.utils.tests.common import *

RE(sim_print_plan())
RE(sim_count_plan())
RE(sim_rel_scan_plan())
```

## Installation

Set up the development environment.

```bash
conda create -y -n instrument_template python pyqt=5
conda activate instrument_template
pip install -e .[all]
```

## IPython console

```bash
ipython
```

```py
from instrument_template.startup import *
```

## Jupyter notebook

Start JupyterLab, a Jupyter notebook server, or a notebook, VSCode.

Start the data acquisition:

```py
from instrument_template.startup import *
```

See this [example](./docs/source/demo.ipynb).

## queueserver

The queueserver has a host process that manages a RunEngine. Client sessions
will interact with that host process.  See [qs/README](./qs/README.md) for more
details.

### Run a queueserver host process

Use the queueserver host management script.  This option stops the server (if it
is running) and then starts it.  This is the usual way to (re)start the QS host
process.

```bash
./qs/qs_host.sh restart
```

### Run a queueserver client GUI

At this time, there is one GUI recommended for use with the bluesky queueserver.
Other GUI clients are in development and show promise of improvements.  For now,
use this one.

```bash
queue-monitor &
```
