"""
Databroker catalog, provides ``cat``.
=====================================

.. autosummary::
    ~cat
"""

import logging

import databroker

logger = logging.getLogger(__name__)
logger.info(__file__)
cat = databroker.temp().v2
"""Databroker catalog object, receives new data from ``RE``."""
