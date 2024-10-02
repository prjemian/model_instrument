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

from .utils._logging_setup import configure_logging

configure_logging()

logger = logging.getLogger(__name__)
logger.info(__file__)

# Bluesky data acquisition setup
from .core.best_effort import bec  # noqa
from .core.best_effort import peaks  # noqa
from .core.catalog import cat  # noqa
from .utils.helper import running_in_queueserver  # noqa
from .core.run_engine import RE  # noqa
from .core.run_engine import sd  # noqa
from .configs.loaders import iconfig  # noqa

# Configure the session with callbacks, devices, and plans.
if iconfig.get("NEXUS_DATA_FILES") is not None:
    from .callbacks.nexus_data_file_writer import nxwriter  # noqa

if iconfig.get("SPEC_DATA_FILES") is not None:
    from .callbacks.spec_data_file_writer import newSpecFile  # noqa
    from .callbacks.spec_data_file_writer import spec_comment  # noqa
    from .callbacks.spec_data_file_writer import specwriter  # noqa

# These imports must come after the above setup.
if running_in_queueserver():
    ### To make the standard plans available in QS, import by '*'.
    from apstools.plans import lineup2  # noqa
    from bluesky.plans import *  # noqa

else:
    # Import bluesky plans and stubs with prefixes set by common conventions.
    # The apstools plans and utils are imported by '*'.
    from apstools.plans import *  # noqa
    from apstools.utils import *  # noqa
    from bluesky import plan_stubs as bps  # noqa
    from bluesky import plans as bp  # noqa
    from .utils.ophyd_setup import oregistry  # noqa

from .devices import *  # noqa
from .plans import *  # noqa

# TODO: Loads plans for development, remove for production.
from .tests.common import *  # noqa
