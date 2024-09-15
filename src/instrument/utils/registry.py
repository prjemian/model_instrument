"""
Ophyd device and signal registry, provides ``oregistry``.
=========================================================

.. autosummary::
    ~oregistry
"""

import logging

from ophydregistry import Registry

logger = logging.getLogger(__name__)
logger.info(__file__)
oregistry = Registry(auto_register=True)
"""Registry of all ophyd-style Devices and Signals."""
