"""
EPICS & ophyd related setup
===========================

.. autosummary::
    ~oregistry
    ~set_control_layer
    ~set_timeouts
    ~epics_scan_id_source
    ~connect_scan_id_pv
"""

import logging

import ophyd
from ophyd.signal import EpicsSignalBase
from ophydregistry import Registry

from .config_loaders import iconfig

logger = logging.getLogger(__name__)
logger.bsdev(__file__)

re_config = iconfig.get("RUN_ENGINE", {})

DEFAULT_CONTROL_LAYER = "PyEpics"
DEFAULT_TIMEOUT = 60  # default used next...
ophyd_config = iconfig.get("OPHYD", {})


def epics_scan_id_source(scan_id_epics, _md):
    """
    Callback function for RunEngine.  Returns *next* scan_id to be used.

    * Ignore metadata dictionary passed as argument.
    * Get current scan_id from PV.
    * Apply lower limit of zero.
    * Increment (so that scan_id numbering starts from 1).
    * Set PV with new value.
    * Return new value.

    Exception will be raised if PV is not connected when next
    ``bps.open_run()`` is called.
    """
    new_scan_id = max(scan_id_epics.get(), 0) + 1
    scan_id_epics.put(new_scan_id)
    return new_scan_id


def connect_scan_id_pv(RE, pv: str = None):
    """
    Define a PV to use for the RunEngine's `scan_id`.
    """
    from ophyd import EpicsSignal

    pv = pv or re_config.get("SCAN_ID_PV")
    if pv is None:
        return

    logger.info("Using EPICS PV %r for RunEngine 'scan_id'", pv)

    scan_id_epics = EpicsSignal(pv, name="scan_id_epics")

    # Setup the RunEngine to use the EPICS PV to provide the scan_id.
    RE.scan_id_source = epics_scan_id_source(scan_id_epics)

    scan_id_epics.wait_for_connection()
    RE.md["scan_id_pv"] = scan_id_epics.pvname
    RE.md["scan_id"] = scan_id_epics.get()  # set scan_id from EPICS


def set_control_layer(control_layer: str = DEFAULT_CONTROL_LAYER):
    """
    Communications library between ophyd and EPICS Channel Access.

    Choices are: PyEpics (default) or caproto.

    OPHYD_CONTROL_LAYER is an application of "lessons learned."

    Only used in a couple rare cases where PyEpics code was failing.
    It's defined here since it was difficult to find how to do this
    in the ophyd documentation.
    """

    control_layer = ophyd_config.get("CONTROL_LAYER", control_layer)
    ophyd.set_cl(control_layer.lower())

    logger.info("using ophyd control layer: %r", ophyd.cl.name)


def set_timeouts():
    """Set default timeout for all EpicsSignal connections & communications."""
    if not EpicsSignalBase._EpicsSignalBase__any_instantiated:
        # Only BEFORE any EpicsSignalBase (or subclass) are created!
        timeouts = ophyd_config.get("TIMEOUTS", {})
        EpicsSignalBase.set_defaults(
            auto_monitor=True,
            timeout=timeouts.get("PV_READ", DEFAULT_TIMEOUT),
            write_timeout=timeouts.get("PV_WRITE", DEFAULT_TIMEOUT),
            connection_timeout=iconfig.get("PV_CONNECTION", DEFAULT_TIMEOUT),
        )


oregistry = Registry(auto_register=True)
"""Registry of all ophyd-style Devices and Signals."""
