"""
Setup the Bluesky RunEngine, provides ``RE`` and ``sd``.
========================================================

.. autosummary::
    ~RE
    ~sd
"""

import bluesky

from .best_effort import bec
from .catalog import cat

RE = bluesky.RunEngine()
"""The bluesky RunEngine object."""

sd = bluesky.SupplementalData()
"""Baselines & monitors for ``RE``."""

RE.subscribe(cat.v1.insert)
RE.subscribe(bec)
RE.preprocessors.append(sd)
