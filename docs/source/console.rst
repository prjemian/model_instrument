IPython console
===============

An IPython console session provides direct interaction with the
various parts of the bluesky (and other Python) packages and tools.

Start the console session with the environment with your bluesky installation,
including the `instrument` package you installed.  Here, ``$`` is a bash
command prompt.  You don't type the command prompt.

.. code-block:: bash

    $ ipython
    Python 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:12:24) [GCC 11.2.0]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.27.0 -- An enhanced Interactive Python. Type '?' for help.

When ready to load the bluesky data acquisition for use, type this command.
Note that ``In [1]:`` and ``In [2]:`` are numbered command prompts from IPython.

.. code-block:: ipy

    In [1]: from instrument.startup import *
    Activating auto-logging. Current session state plus future input saved.
    Filename       : /path/to/project/.logs/ipython_console.log
    Mode           : rotate
    Output logging : True
    Raw input log  : False
    Timestamping   : True
    State          : active
    I Mon-16:55:40 - ############################################################ startup
    I Mon-16:55:40 - logging started
    I Mon-16:55:40 - logging level = 10
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/_logging_setup.py
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/aps_dm_setup.py
    W Mon-16:55:40 - APS DM setup file does not exist: '/home/dm/etc/dm.setup.sh'
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/debug_setup.py
    Exception reporting mode: Minimal
    I Mon-16:55:40 - xmode exception level: 'Minimal'
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/functions.py
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/mpl_setup.py
    I Mon-16:55:40 - /path/to/project/src/instrument/startup.py
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/best_effort.py
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/catalog.py
    I Mon-16:55:40 - Databroker catalog: temp
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/ophyd_setup.py
    I Mon-16:55:40 - using ophyd control layer: 'pyepics'
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/run_engine.py
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/epics_setup.py
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/metadata.py
    I Mon-16:55:40 - RunEngine metadata saved in directory: /home/user/.config/Bluesky_RunEngine_md
    I Mon-16:55:40 - /path/to/project/src/instrument/utils/tests/common.py

    In [2]:

Shortcut
--------

Here's a shortcut that combines both steps:

    .. code-block::

        ipython -i -c "from instrument.startup import *"
