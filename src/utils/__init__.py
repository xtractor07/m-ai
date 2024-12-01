"""
Utility functions for M-AI
------------------------
Common utilities and helper functions used across the project.
"""

import os
from typing import Final

# Base paths
ROOT_DIR: Final[str] = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_DIR: Final[str] = os.path.join(ROOT_DIR, "configs")
LOGS_DIR: Final[str] = os.path.join(ROOT_DIR, "logs")
from .logger import get_logger
from .constants import (
    ROOT_DIR,
    CONFIG_DIR,
    LOGS_DIR,
    ENV_DEVELOPMENT,
    ENV_PRODUCTION,
    ENV_TESTING,
)
from .config import (
    Config,
    ModelConfig,
    APIConfig,
    ConfigManager,
    config_manager,
)

__all__ = [
    'get_logger',
    'ROOT_DIR',
    'CONFIG_DIR',
    'LOGS_DIR',
    'ENV_DEVELOPMENT',
    'ENV_PRODUCTION',
    'ENV_TESTING',
    'Config',
    'ModelConfig',
    'APIConfig',
    'ConfigManager',
    'config_manager',
]

