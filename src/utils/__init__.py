"""
Utility functions for M-AI
------------------------
Common utilities and helper functions used across the project.
"""

from .logger import get_logger
from .constants import (
    ROOT_DIR,
    CONFIG_DIR,
    LOGS_DIR,
    ENV_DEVELOPMENT,
    ENV_PRODUCTION,
    ENV_TESTING,
)

__all__ = [
    'get_logger',
    'ROOT_DIR',
    'CONFIG_DIR',
    'LOGS_DIR',
    'ENV_DEVELOPMENT',
    'ENV_PRODUCTION',
    'ENV_TESTING',
]