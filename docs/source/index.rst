instrument (|release|)
======================

Bluesky Data Acquisition in console, notebook, & queueserver.

Start the data collection session with the same command, whether in the IPython
console, a Jupyter notebook, the queueserver, or even a Python script:

.. code-block:: py
      :linenos:

      from instrument.startup import *
      from instrument.utils.tests.common import *

      RE(sim_print_plan())
      RE(sim_count_plan())
      RE(sim_rel_scan_plan())

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   demo
   api
   license

About ...
-----------

:home: https://prjemian.github.io/instrument_template/
:bug tracker: https://github.com/prjemian/instrument_template/issues
:source: https://github.com/prjemian/instrument_template
:license: :ref:`license`
:full version: |version|
:published: |today|
:reference: :ref:`genindex`, :ref:`modindex`, :ref:`search`
