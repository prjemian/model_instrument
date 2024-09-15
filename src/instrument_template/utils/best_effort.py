"""
BestEffortCallback: simple real-time visualizations, provides ``bec``.
======================================================================

.. autosummary::
    ~bec
    ~peaks
"""

import logging

from bluesky.callbacks.best_effort import BestEffortCallback

from .functions import running_in_queueserver

logger = logging.getLogger(__name__)
logger.info(__file__)

bec = BestEffortCallback()
"""BestEffortCallback object, creates live tables and plots."""

if running_in_queueserver():
    bec.disable_plots()

peaks = bec.peaks
"""Dictionary with statistical analysis of LivePlots."""
