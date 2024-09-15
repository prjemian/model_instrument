"""
BestEffortCallback: simple real-time visualizations, provides ``bec``.
======================================================================

.. autosummary::
    ~bec
    ~peaks
"""

from bluesky.callbacks.best_effort import BestEffortCallback

from .functions import running_in_queueserver

bec = BestEffortCallback()
"""BestEffortCallback object, creates live tables and plots."""

if running_in_queueserver():
    bec.disable_plots()

peaks = bec.peaks
"""Dictionary with statistical analysis of LivePlots."""
