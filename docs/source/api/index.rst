.. _api:

API: The Source Code
====================

.. autosummary::
    :nosignatures:

    ~instrument.startup

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   callbacks
   configs
   core
   devices
   plans
   utils

``instrument.startup``
-------------------------------

This same code can be used with IPython console & Jupyter notebook sessions and
the bluesky queueserver.  Use this inspiration to build your own custom startup
procedures.

.. literalinclude:: ../../../src/instrument/startup.py
    :language: python
    :linenos:

.. automodule:: instrument.startup
