"""
Start Bluesky Data Acquisition sessions of all kinds.

Includes:

* Python script
* IPython console
* Jupyter notebook
* Bluesky queueserver
"""

# logging setup first
import logging

from .utils.logging_setup import configure_logging

configure_logging()

logger = logging.getLogger(__name__)
logger.bsdev(__file__)

# Bluesky data acquisition setup
from .configs.loaders import iconfig
from .core.best_effort_init import bec  # noqa: F401
from .core.best_effort_init import peaks  # noqa: F401
from .core.catalog_init import cat  # noqa: F401
from .core.run_engine_init import RE  # noqa: F401
from .core.run_engine_init import sd  # noqa: F401
from .utils.helper_functions import running_in_queueserver

# Configure the session with callbacks, devices, and plans.
if iconfig.get("NEXUS_DATA_FILES") is not None:
    from .callbacks.nexus_data_file_writer import nxwriter  # noqa: F401

if iconfig.get("SPEC_DATA_FILES") is not None:
    from .callbacks.spec_data_file_writer import newSpecFile  # noqa: F401
    from .callbacks.spec_data_file_writer import spec_comment  # noqa: F401
    from .callbacks.spec_data_file_writer import specwriter  # noqa: F401

# These imports must come after the above setup.
if running_in_queueserver():
    ### To make the standard plans available in QS, import by '*'.
    from apstools.plans import lineup2  # noqa: F401
    from bluesky.plans import *  # noqa: F403

else:
    # Import bluesky plans and stubs with prefixes set by common conventions.
    # The apstools plans and utils are imported by '*'.
    from apstools.plans import *  # noqa: F403
    from apstools.utils import *  # noqa: F403
    from bluesky import plan_stubs as bps  # noqa: F401
    from bluesky import plans as bp  # noqa: F401

    from .utils.controls_setup import oregistry  # noqa: F401

from .devices import *  # noqa: F403
from .plans import *  # noqa: F403

# Loads plans for development, remove for production.
from .tests.sim_plans import *  # noqa: F403
