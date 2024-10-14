"""
Configure logging for this session.

.. rubric:: Public
.. autosummary::
    ~configure_logging

.. rubric:: Internal
.. autosummary::
    ~_setup_console_logger
    ~_setup_file_logger
    ~_setup_ipython_logger
    ~_setup_module_logging

.. seealso:: https://blueskyproject.io/bluesky/main/debugging.html
"""

import logging
import logging.handlers
import os
import pathlib

BYTE = 1
kB = 1024 * BYTE
MB = 1024 * kB

BRIEF_DATE = "%a-%H:%M:%S"
BRIEF_FORMAT = "%(levelname)-.1s %(asctime)s.%(msecs)03d: %(message)s"
DEFAULT_CONFIG_FILE = pathlib.Path(__file__).parent.parent / "configs" / "logging.yml"


def configure_logging():
    """Configure logging as described in file."""
    from ..configs.loaders import load_config_yaml

    # (Re)configure the root logger.
    logger = logging.getLogger(__name__).root
    logger.debug("logger=%r", logger)

    config_file = os.environ.get("BLUESKY_INSTRUMENT_CONFIG_FILE")
    if config_file is None:
        config_file = DEFAULT_CONFIG_FILE
    else:
        config_file = pathlib.Path(config_file)

    logging_configuration = load_config_yaml(config_file)
    for part, cfg in logging_configuration.items():
        logging.debug("%r - %s", part, cfg)

        # Each handler has its own level.
        if part == "console_logs":
            _setup_console_logger(logger, cfg)

        elif part == "file_logs":
            _setup_file_logger(logger, cfg)

        elif part == "ipython_logs":
            _setup_ipython_logger(logger, cfg)

        elif part == "modules":
            _setup_module_logging(cfg)


def _setup_console_logger(logger, cfg):
    """
    Reconfigure the root logger as configured by the user.

    We can't apply user configurations in ``configure_logging()`` above
    because the code to read the config file triggers initialization of
    the logging system.

    .. seealso:: https://docs.python.org/3/library/logging.html#logging.basicConfig
    """
    logging.basicConfig(
        encoding="utf-8",
        level=cfg["level"].upper(),
        format=cfg["log_format"],
        datefmt=cfg["date_format"],
        force=True,  # replace any previous setup
    )


def _setup_file_logger(logger, cfg):
    """Record log messages in file(s)."""
    formatter = logging.Formatter(
        fmt=cfg["log_format"],
        datefmt=cfg["date_format"],
        style="%",
        validate=True,
    )
    formatter.default_msec_format = "%s.%03d"

    backupCount = cfg.get("backupCount", 9)
    maxBytes = cfg.get("maxBytes", 1 * MB)
    log_path = pathlib.Path(cfg.get("log_directory", ".logs")).resolve()
    if not log_path.exists():
        os.makedirs(str(log_path))

    file_name = log_path / cfg.get("log_filename_base", "logging.log")
    if maxBytes > 0 or backupCount > 0:
        backupCount = max(backupCount, 1)  # impose minimum standards
        maxBytes = max(maxBytes, 100 * kB)
        handler = logging.handlers.RotatingFileHandler(
            file_name,
            maxBytes=maxBytes,
            backupCount=backupCount,
        )
    else:
        handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    if cfg.get("rotate_on_startup", False):
        handler.doRollover()
    logger.addHandler(handler)
    logger.info("%s startup", "*" * 40)
    logger.info(__file__)
    logger.info("Log file: %s", file_name)


def _setup_ipython_logger(logger, cfg):
    """
    Internal: Log IPython console session In and Out to a file.

    See ``logrotate?`` int he IPython console for more information.
    """
    log_path = pathlib.Path(cfg.get("log_directory", ".logs")).resolve()
    try:
        from IPython import get_ipython

        # start logging console to file
        # https://ipython.org/ipython-doc/3/interactive/magics.html#magic-logstart
        _ipython = get_ipython()
        log_file = log_path / cfg.get("log_filename_base", "ipython_log.py")
        log_mode = cfg.get("log_mode", "rotate")
        options = cfg.get("options", "-o -t")
        if _ipython is not None:
            _ipython.magic(f"logstart {options} {log_file} {log_mode}")
            if logger is not None:
                logger.info("Console logging: %s", log_file)
    except Exception as exc:
        if logger is None:
            print(f"Could not setup console logging: {exc}")
        else:
            logger.exception("Could not setup console logging.")


def _setup_module_logging(cfg):
    """Internal: Set logging level for each named module."""
    for module, level in cfg.items():
        logging.getLogger(module).setLevel(level.upper())
