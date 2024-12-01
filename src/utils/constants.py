"""
Constants for M-AI
----------------
Central location for all constant values used throughout the project.
"""

import os
from pathlib import Path
from typing import Final

# Directory paths
ROOT_DIR: Final[str] = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_DIR: Final[str] = os.path.join(ROOT_DIR, "configs")
LOGS_DIR: Final[str] = os.path.join(ROOT_DIR, "logs")

# Ensure required directories exist
Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)
Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)

# Environment constants
ENV_DEVELOPMENT: Final[str] = "development"
ENV_PRODUCTION: Final[str] = "production"
ENV_TESTING: Final[str] = "testing"

# Logging constants
DEFAULT_LOG_LEVEL: Final[str] = "INFO"
MAX_LOG_SIZE: Final[int] = 10 * 1024 * 1024  # 10MB
LOG_BACKUP_COUNT: Final[int] = 5