"""
Setup Debug Reporting
=========================
"""

import logging

from IPython import get_ipython

from ..configs.loaders import iconfig

logger = logging.getLogger(__name__)
logger.info(__file__)

def debug_python():
    # terse error dumps (Exception tracebacks)
    _ip = get_ipython()
    if _ip is not None:
        _xmode_level = iconfig.get("XMODE_DEBUG_LEVEL", "Minimal")
        _ip.run_line_magic("xmode", _xmode_level)
        logger.info("xmode exception level: '%s'", _xmode_level)
