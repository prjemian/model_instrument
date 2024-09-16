"""
Setup the Bluesky RunEngine, provides ``RE`` and ``sd``.
========================================================

.. autosummary::
    ~RE
    ~sd
"""

import logging

import bluesky

logger = logging.getLogger(__name__)  # noqa
logger.info(__file__)  # noqa

from .best_effort import bec  # noqa
from .catalog import cat  # noqa
from .config import iconfig  # noqa
from .epics_tools import connect_scan_id_pv  # noqa
from .metadata import MD_PATH  # noqa
from .metadata import re_metadata  # noqa

re_config = iconfig.get("RE", {})

RE = bluesky.RunEngine()
"""The bluesky RunEngine object."""

# Save/restore RE.md dictionary, in this precise order.
if MD_PATH is not None:
    RE.md = bluesky.utils.PersistentDict(MD_PATH)
RE.md.update(re_metadata(cat))  # programmatic metadata
RE.md.update(re_config.get("DEFAULT_METADATA", {}))

sd = bluesky.SupplementalData()
"""Baselines & monitors for ``RE``."""

RE.subscribe(cat.v1.insert)
RE.subscribe(bec)
RE.preprocessors.append(sd)

connect_scan_id_pv(RE)  # if configured
