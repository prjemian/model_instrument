"""
Setup the Bluesky RunEngine, provides ``RE`` and ``sd``.
========================================================

.. autosummary::
    ~RE
    ~sd
"""

import logging

import bluesky

from .best_effort import bec
from .catalog import cat

logger = logging.getLogger(__name__)
logger.info(__file__)

RE = bluesky.RunEngine()
"""The bluesky RunEngine object."""

sd = bluesky.SupplementalData()
"""Baselines & monitors for ``RE``."""

RE.subscribe(cat.v1.insert)
RE.subscribe(bec)
RE.preprocessors.append(sd)
