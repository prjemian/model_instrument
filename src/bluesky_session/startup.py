"""
Start a Bluesky Data Acquisition session.
"""

from .utils.best_effort import bec  # noqa
from .utils.best_effort import peaks  # noqa
from .utils.catalog import cat  # noqa
from .utils.functions import running_in_queueserver
from .utils.registry import oregistry  # noqa
from .utils.run_engine import RE  # noqa
from .utils.run_engine import sd  # noqa
from .utils.tests.common import *  # noqa

# These imports must come after the above setup.
if not running_in_queueserver():
    # Sessions in the queueserver do not need the devices & signals.
    # Their plans can find the devices & signals they need in the oregistry.
    from .devices import *  # noqa in.
from .callbacks import *  # noqa
from .plans import *  # noqa
