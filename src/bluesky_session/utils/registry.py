"""
Ophyd device and signal registry, provides ``oregistry``.
=========================================================

.. autosummary::
    ~oregistry
"""

from ophydregistry import Registry

oregistry = Registry(auto_register=True)
"""Registry of all ophyd-style Devices and Signals."""
