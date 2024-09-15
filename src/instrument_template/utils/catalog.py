"""
Databroker catalog, provides ``cat``.
=====================================

.. autosummary::
    ~cat
"""

import databroker

cat = databroker.temp().v2
"""Databroker catalog object, receives new data from ``RE``."""
