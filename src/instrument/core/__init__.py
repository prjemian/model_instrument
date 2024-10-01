"""
Utility support to start bluesky sessions.

Also contains setup code that MUST run before other code in this directory.
"""

from ._logging_setup import logger  # noqa
from ..configs.loaders import iconfig

from .aps_dm_setup import dm_setup
from .debug_setup import debug_python # noqa need to talk about why the logic is complicated given that the variable is declared
from .mpl_setup import mpl_setup_2  # noqa

debug_python()
mpl_setup_2()
dm_setup(iconfig.get("DM_SETUP_FILE"))
