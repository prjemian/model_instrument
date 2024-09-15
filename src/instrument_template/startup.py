"""
Start a Bluesky Data Acquisition session in console, notebook, & queueserver.
"""

import logging

logger = logging.getLogger(__name__)  # noqa
logger.info(__file__)  # noqa

from .utils.best_effort import bec  # noqa
from .utils.best_effort import peaks  # noqa
from .utils.catalog import cat  # noqa
from .utils.functions import running_in_queueserver  # noqa
from .utils.functions import subscribe_re_callbacks  # noqa
from .utils.registry import oregistry  # noqa
from .utils.run_engine import RE  # noqa
from .utils.run_engine import sd  # noqa

# These imports must come after the above setup.
if running_in_queueserver():
    from apstools.plans import lineup2  # noqa
    from bluesky.plans import *  # noqa
else:
    from apstools.plans import *  # noqa
    from apstools.utils import *  # noqa
    from bluesky import plan_stubs as bps  # noqa
    from bluesky import plans as bp  # noqa

    # Sessions in the queueserver do not need the devices & signals.
    # Their plans can find the devices & signals they need in the oregistry.
    from .devices import *  # noqa

from .callbacks import *  # noqa
from .plans import *  # noqa

# TODO: developer use only
from .utils.tests.common import *  # noqa

subscribe_re_callbacks(RE)  # after the devices are created
