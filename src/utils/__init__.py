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