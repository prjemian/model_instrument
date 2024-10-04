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
    I Thu-23:49:59 - ############################################################ startup
    I Thu-23:49:59 - logging started
    I Thu-23:49:59 - logging level = 10
    I Thu-23:49:59 - /home/prjemian/Documents/projects/prjemian/model_instrument/src/instrument/utils/_logging_setup.py
    I Thu-23:49:59 - /home/prjemian/Documents/projects/prjemian/model_instrument/src/instrument/utils/aps_functions.py
    I Thu-23:49:59 - /home/prjemian/Documents/projects/prjemian/model_instrument/src/instrument/utils/helper_functions.py
    W Thu-23:49:59 - APS DM setup file does not exist: '/home/dm/etc/dm.setup.sh'
    I Thu-23:49:59 - /home/prjemian/Documents/projects/prjemian/model_instrument/src/instrument/utils/controls_setup.py
    I Thu-23:49:59 - /home/prjemian/Documents/projects/prjemian/model_instrument/src/instrument/utils/metadata.py
    I Thu-23:49:59 - RunEngine metadata saved in directory: /home/prjemian/.config/Bluesky_RunEngine_md
    I Thu-23:49:59 - using ophyd control layer: 'pyepics'
    dict(RE.md)={'versions': {'apstools': '1.6.20', 'bluesky': '1.13.0a3', 'databroker': '1.2.5', 'epics': '3.5.7', 'h5py': '3.9.0', 'intake': '0.6.4', 'matplotlib': '3.9.2', 'numpy': '1.26.4', 'ophyd': '1.9.0', 'pyRestTable': '2020.0.11.dev1+gfcdd4be', 'python': '3.11.10', 'pysumreg': '1.0.6', 'spec2nexus': '2021.2.6'}, 'pid': 566711, 'proposal_id': 'commissioning', 'login_id': 'prjemian@arf.jemian.org', 'scan_id': 9382, 'iconfig': {'ICONFIG_VERSION': '2.0.0', 'DATABROKER_CATALOG': 'temp', 'RUN_ENGINE': {'DEFAULT_METADATA': {'beamline_id': 'instrument', 'instrument_name': 'Most Glorious Scientific Instrument', 'proposal_id': 'commissioning', 'databroker_catalog': 'temp'}, 'USE_PROGRESS_BAR': False}, 'AREA_DETECTOR': {'ALLOW_PLUGIN_WARMUP': True, 'BLUESKY_FILES_ROOT': '/path/to/data/', 'IMAGE_DIR': 'sub/directory/path', 'HDF5_FILE_TEMPLATE': '%s%s_%6.6d.h5'}, 'SPEC_DATA_FILES': {'FILE_EXTENSION': 'dat'}, 'DM_SETUP_FILE': '/home/dm/etc/dm.setup.sh', 'OPHYD': {'TIMEOUTS': {'PV_READ': 5, 'PV_WRITE': 5, 'PV_CONNECTION': 5}}, 'LOGGING': {'NUMBER_OF_PREVIOUS_BACKUPS': 9}, 'XMODE_DEBUG_LEVEL': 'Minimal'}, 'databroker_catalog': 'temp', 'beamline_id': 'instrument', 'instrument_name': 'Most Glorious Scientific Instrument', 'conda_prefix': '/home/prjemian/.conda/envs/bluesky_2024_3'}

.. note:: The first line is a linux *shebang* [#]_ that tells the
    linux command processor to start this script with the
    default ``python`` executable in the current environment.

.. [#] https://linuxhandbook.com/make-file-executable/
.. [#] https://en.wikipedia.org/wiki/Shebang_(Unix)
