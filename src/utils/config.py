"""Configuration Management for M-AI."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional, cast

import yaml
from pydantic import BaseModel, Field

from .constants import CONFIG_DIR
from .logger import get_logger

logger = get_logger(__name__)


class ModelConfig(BaseModel):
    """Configuration settings for the LLaMA model."""

    model_size: str = Field(
        default="7B",
        description="Size of the LLaMA model to use (7B, 13B, or 70B)",
    )
    model_path: str = Field(
        default="models/llama-2-7b",
        description="Path to the model weights",
    )
    max_tokens: int = Field(
        default=2048,
        description="Maximum number of tokens for model input",
    )
    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        description="Sampling temperature for model output",
    )
    top_p: float = Field(
        default=0.9,
        ge=0.0,
        le=1.0,
        description="Nucleus sampling parameter",
    )


class APIConfig(BaseModel):
    """Configuration settings for the API."""

    host: str = Field(
        default="0.0.0.0",
        description="Host address for the API server",
    )
    port: int = Field(
        default=8000,
        description="Port number for the API server",
    )
    debug: bool = Field(
        default=False,
        description="Enable debug mode",
    )
    workers: int = Field(
        default=1,
        gt=0,
        description="Number of worker processes",
    )


class Config(BaseModel):
    """Main configuration class containing all settings."""

    environment: str = Field(
        default="development",
        description="Execution environment (development/production)",
    )
    model: ModelConfig = Field(default_factory=ModelConfig)
    api: APIConfig = Field(default_factory=APIConfig)
    log_level: str = Field(
        default="INFO",
        description="Logging level",
    )


class ConfigManager:
    """Manages configuration loading and validation."""

    def __init__(self, config_dir: str = CONFIG_DIR) -> None:
        """Initialize the configuration manager."""
        self.config_dir = config_dir
        self._config: Optional[Config] = None

    def load_config(self, env: str = "development") -> Config:
        """Load configuration from YAML files."""
        config_path = os.path.join(self.config_dir, f"config.{env}.yaml")

        if not os.path.exists(config_path):
            logger.warning(f"Config file not found: {config_path}")
            config_path = os.path.join(self.config_dir, "config.default.yaml")
            if not os.path.exists(config_path):
                config = Config()
                self._config = config
                return config

        try:
            with open(config_path, "r") as f:
                config_dict = yaml.safe_load(f)
            config = Config.model_validate(cast(Dict[str, Any], config_dict or {}))
            self._config = config
            logger.info(f"Loaded configuration from {config_path}")
            return config
        except Exception as e:
            logger.error(f"Error loading config from {config_path}: {str(e)}")
            raise

    @property
    def config(self) -> Config:
        """Get the current configuration."""
        if self._config is None:
            self._config = self.load_config()
        return self._config

    def get_model_config(self) -> ModelConfig:
        """Get model-specific configuration."""
        return self.config.model

    def get_api_config(self) -> APIConfig:
        """Get API-specific configuration."""
        return self.config.api

    def update_config(self, updates: Dict[str, Any]) -> None:
        """Update configuration values."""
        if self._config is None:
            raise ValueError("Configuration not loaded. Call load_config() first.")
        config_dict = self._config.model_dump()
        for key, value in updates.items():
            if "." in key:
                parts = key.split(".")
                current = config_dict
                for part in parts[:-1]:
                    current = current.setdefault(part, {})
                current[parts[-1]] = value
            else:
                config_dict[key] = value
        self._config = Config.model_validate(config_dict)
        logger.info("Configuration updated successfully")


# Create a global configuration manager instance
config_manager = ConfigManager()
