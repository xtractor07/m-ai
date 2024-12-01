from __future__ import annotations

"""
Logging Configuration for M-AI
----------------------------
Provides a centralized logging configuration with different handlers
for development and production environments.
"""

import logging
import logging.handlers
import os
import sys
from pathlib import Path
from typing import Optional, Dict, Any

from .constants import LOGS_DIR

# Ensure logs directory exists
Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)

# Log format with timestamp, level, module, and message
DEFAULT_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
DETAILED_LOG_FORMAT = (
    "%(asctime)s - %(levelname)s - [%(name)s.%(funcName)s:%(lineno)d] - %(message)s"
)

# Log file names
DEBUG_LOG = os.path.join(LOGS_DIR, "debug.log")
INFO_LOG = os.path.join(LOGS_DIR, "info.log")
ERROR_LOG = os.path.join(LOGS_DIR, "error.log")

def setup_logger(
    name: str,
    level: int = logging.INFO,
    env: str = "development",
    log_file: Optional[str] = None,
    max_bytes: int = 10485760,  # 10MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Set up a logger with appropriate handlers and formatters.

    Args:
        name: Name of the logger
        level: Logging level
        env: Environment ('development' or 'production')
        log_file: Optional specific log file path
        max_bytes: Maximum size of each log file
        backup_count: Number of backup files to keep

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Remove existing handlers if any
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create formatters
    formatter = logging.Formatter(
        DETAILED_LOG_FORMAT if env == "development" else DEFAULT_LOG_FORMAT
    )

    # Console handler (stdout for INFO and below, stderr for WARNING and above)
    if env == "development":
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.addFilter(lambda record: record.levelno <= logging.INFO)
        logger.addHandler(stdout_handler)

        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setFormatter(formatter)
        stderr_handler.setLevel(logging.WARNING)
        logger.addHandler(stderr_handler)

    # File handlers
    if log_file:
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

    return logger

def get_logger(
    name: str,
    config: Optional[Dict[str, Any]] = None
) -> logging.Logger:
    """
    Get or create a logger with the given name and configuration.

    Args:
        name: Name of the logger
        config: Optional configuration dictionary

    Returns:
        Configured logger instance
    """
    if config is None:
        config = {}

    env = config.get('environment', 'development')
    level = config.get('level', logging.INFO)
    log_file = config.get('log_file')

    return setup_logger(
        name=name,
        level=level,
        env=env,
        log_file=log_file,
        max_bytes=config.get('max_bytes', 10485760),
        backup_count=config.get('backup_count', 5)
    )

# Create default loggers for different levels
debug_logger = setup_logger('debug', logging.DEBUG, log_file=DEBUG_LOG)
info_logger = setup_logger('info', logging.INFO, log_file=INFO_LOG)
error_logger = setup_logger('error', logging.ERROR, log_file=ERROR_LOG)