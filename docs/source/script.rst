Python scripts
==============

Bluesky data acquisition can be written as Python command programs (scripts).
This example program shows the RunEngine's metadata.  Save it to a file (perhaps
named ``example.py``).  Be sure to make the file executable. [#]_

.. code-block:: py
    :linenos:

    #!/usr/bin/env python
    from instrument.startup import RE

    print(f"{dict(RE.md)=!r}")

Assuming you named this file ``example.py``, then run it (in the environment
with your bluesky installation).  Note that ``$`` is a command prompt.  You don't
type that.

.. code-block:: bash
    :linenos:

    $ example.py
    I Mon-17:14:30 - ############################################################ startup
    I Mon-17:14:30 - logging started
    I Mon-17:14:30 - logging level = 10
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/_logging_setup.py
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/aps_dm_setup.py
    W Mon-17:14:30 - APS DM setup file does not exist: '/home/dm/etc/dm.setup.sh'
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/debug_setup.py
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/functions.py
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/mpl_setup.py
    I Mon-17:14:30 - /path/to/project/src/instrument/startup.py
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/best_effort.py
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/catalog.py
    I Mon-17:14:30 - Databroker catalog: temp
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/ophyd_setup.py
    I Mon-17:14:30 - using ophyd control layer: 'pyepics'
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/run_engine.py
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/epics_setup.py
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/metadata.py
    I Mon-17:14:30 - RunEngine metadata saved in directory: /home/user/.config/Bluesky_RunEngine_md
    I Mon-17:14:30 - /path/to/project/src/instrument/utils/tests/common.py
    dict(RE.md)={'login_id': 'user@host', 'databroker_catalog': 'temp', 'proposal_id': 'training', 'iconfig': {'ICONFIG_VERSION': '2.0.0', 'DATABROKER_CATALOG': 'temp', 'RUN_ENGINE': {'DEFAULT_METADATA': {'beamline_id': 'instrument', 'instrument_name': 'Most Glorious Scientific Instrument', 'proposal_id': 'commissioning', 'databroker_catalog': 'temp'}, 'USE_PROGRESS_BAR': False}, 'AREA_DETECTOR': {'ALLOW_PLUGIN_WARMUP': True, 'BLUESKY_FILES_ROOT': '/path/to/data/', 'IMAGE_DIR': 'sub/directory/path', 'HDF5_FILE_TEMPLATE': '%s%s_%6.6d.h5'}, 'SPEC_DATA_FILES': {'FILE_EXTENSION': 'dat'}, 'DM_SETUP_FILE': '/home/dm/etc/dm.setup.sh', 'OPHYD': {'TIMEOUTS': {'PV_READ': 5, 'PV_WRITE': 5, 'PV_CONNECTION': 5}}, 'LOGGING': {'NUMBER_OF_PREVIOUS_BACKUPS': 9}, 'XMODE_DEBUG_LEVEL': 'Minimal'}, 'conda_prefix': '/home/user/.conda/envs/bstest', 'pid': 4058829, 'instrument_name': 'BCDA EPICS Bluesky training', 'versions': {'apstools': '1.6.20', 'bluesky': '1.12.0', 'databroker': '1.2.5', 'epics': '3.5.7', 'h5py': '3.11.0', 'intake': '0.6.4', 'matplotlib': '3.9.2', 'numpy': '1.26.4', 'ophyd': '1.9.0', 'pyRestTable': '2020.0.8', 'python': '3.12.4', 'pysumreg': '1.0.6', 'spec2nexus': '2021.2.6'}, 'scan_id': 51, 'beamline_id': 'Bluesky_training'}


.. note:: The first line is a linux *shebang* [#]_ that tells the
    linux command processor to start this script with the
    default ``python`` executable in the current environment.

.. [#] https://linuxhandbook.com/make-file-executable/
.. [#] https://en.wikipedia.org/wiki/Shebang_(Unix)
