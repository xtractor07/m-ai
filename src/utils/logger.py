from __future__ import annotations

"""
Logging Configuration for M-AI
----------------------------
Implements a hierarchical logging system with different configurations
for development and production environments.
"""

import logging
import logging.handlers
import os
import sys
from pathlib import Path
from typing import Optional, Union

from .constants import LOGS_DIR

# Ensure logs directory exists
Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)

# Constants for logging
DEFAULT_LOG_FORMAT = "[%(asctime)s] %(levelname)-8s %(name)s - %(message)s"
DETAILED_LOG_FORMAT = (
    "[%(asctime)s] %(levelname)-8s [%(name)s:%(funcName)s:%(lineno)d] - %(message)s"
)
MAX_BYTES = 10 * 1024 * 1024  # 10MB
BACKUP_COUNT = 5


class LoggerConfigurator:
    """Configures logging for the M-AI application."""

    def __init__(
        self,
        log_level: Union[str, int] = logging.INFO,
        environment: str = "development",
    ) -> None:
        """
        Initialize the logger configurator.

        Args:
            log_level: The logging level to use
            environment: The environment ('development' or 'production')
        """
        self.log_level = (
            log_level if isinstance(log_level, int) else getattr(logging, log_level.upper())
        )
        self.environment = environment
        self.log_format = (
            DETAILED_LOG_FORMAT if environment == "development" else DEFAULT_LOG_FORMAT
        )

    def _create_console_handler(self) -> logging.Handler:
        """Create a console handler for logging."""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(self.log_format))
        return console_handler

    def _create_file_handler(self, filename: str) -> logging.Handler:
        """Create a rotating file handler for logging."""
        log_file = os.path.join(LOGS_DIR, filename)
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=MAX_BYTES,
            backupCount=BACKUP_COUNT,
            encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(self.log_format))
        return file_handler

    def get_logger(self, name: str, filename: Optional[str] = None) -> logging.Logger:
        """
        Get a configured logger instance.

        Args:
            name: The name of the logger
            filename: Optional filename for file-based logging

        Returns:
            logging.Logger: Configured logger instance
        """
        logger = logging.getLogger(name)
        logger.setLevel(self.log_level)

        # Remove existing handlers to avoid duplication
        logger.handlers.clear()

        # Add console handler
        logger.addHandler(self._create_console_handler())

        # Add file handler if filename is provided
        if filename:
            logger.addHandler(self._create_file_handler(filename))

        # Prevent propagation to root logger
        logger.propagate = False

        return logger


# Default configurator instances
dev_configurator = LoggerConfigurator(log_level=logging.DEBUG, environment="development")
prod_configurator = LoggerConfigurator(log_level=logging.INFO, environment="production")


def get_logger(
    name: str, filename: Optional[str] = None, environment: str = "development"
) -> logging.Logger:
    """
    Get a configured logger instance.

    Args:
        name: The name of the logger
        filename: Optional filename for file-based logging
        environment: The environment ('development' or 'production')

    Returns:
        logging.Logger: Configured logger instance
    """
    configurator = dev_configurator if environment == "development" else prod_configurator
    return configurator.get_logger(name, filename)