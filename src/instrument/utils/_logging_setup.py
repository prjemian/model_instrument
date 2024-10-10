"""
Configure logging for this session.

There are many _loggers_ to control the level of detailed logging for some
bluesky/ophyd internals.  The next table shows some of the many possible logger
names.  Configure the ``ACTIVATE_LOGGERS`` dictionary (below, where the keys are
logger names and the values are logging level, as shown) with any of these
names, or others which you may find useful:

==========================  ====================================================
logger name                 description
==========================  ====================================================
``bluesky``                 logger to which all bluesky log records propagate
``bluesky.emit_document``   when a Document is emitted. The log record does not contain the full content of the Document.
``bluesky.RE``              Records from a RunEngine. INFO-level notes state changes. DEBUG-level notes when each message from a plan is about to be processed and when a status object has completed.
``bluesky.RE.msg``          when each ``Msg`` is about to be processed.
``bluesky.RE.state``        when the RunEngine’s state changes.
``databroker``              logger to which all databroker log records propagate
``ophyd``                   logger to which all ophyd log records propagate
``ophyd.objects``           records from all devices and signals (that is, OphydObject subclasses)
``ophyd.control_layer``     requests issued to the underlying control layer (e.g. pyepics, caproto)
``ophyd.event_dispatcher``  regular summaries of the backlog of updates from the control layer that are being processed on background threads
==========================  ====================================================

References:

* https://blueskyproject.io/ophyd/user_v1/reference/logging.html#logger-names
* https://blueskyproject.io/bluesky/debugging.html#logger-names
"""

import logging


def configure_logging():
    """Temporary logging setup.  Ignores iconfig for now."""
    brief_date = "%a-%H:%M:%S"
    brief_format = "%(levelname)-.1s %(asctime)s: %(message)s"
    logging.basicConfig(
        encoding="utf-8",
        level=logging.INFO,
        format=brief_format,
        datefmt=brief_date,
    )

    logger = logging.getLogger(__name__)
    logger.info(__file__)

    # calm logging in these other modules
    for module in "bluesky databroker ophyd".split():
        logging.getLogger(module).setLevel(logging.WARNING)
