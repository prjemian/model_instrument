"""
Utility functions, provides ``running_in_queueserver()``
========================================================

.. autosummary::

    ~running_in_queueserver
"""

__all__ = ["running_in_queueserver"]

import logging

logger = logging.getLogger(__name__)
logger.info(__file__)


def running_in_queueserver():
    """Detect if running in the bluesky queueserver."""
    try:
        from bluesky_queueserver import is_re_worker_active

        active = is_re_worker_active()
        # print(f"{active=!r}")
        return active
    except Exception as cause:  # noqa
        # print(f"{cause=}")
        return False
