"""Tests for the logging system."""

import logging
import tempfile
from typing import Generator

from pytest import fixture

from src.utils.logger import LoggerConfigurator, get_logger


@fixture(scope="function")  # type: ignore[misc]
def temp_log_dir() -> Generator[str, None, None]:
    """Create a temporary directory for log files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


def test_logger_basic_configuration() -> None:
    """Test basic logger configuration."""
    logger = get_logger("test")
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) > 0
    assert not logger.propagate


def test_logger_with_file(temp_log_dir: str) -> None:
    """Test logger with file output."""
    log_file = "test.log"
    logger = get_logger("test_file", filename=log_file)
    assert len(logger.handlers) == 2  # Console and file handlers
    # Test logging
    test_message = "Test log message"
    logger.info(test_message)


def test_different_environments() -> None:
    """Test logger configuration in different environments."""
    dev_logger = get_logger("test_dev", environment="development")
    prod_logger = get_logger("test_prod", environment="production")
    assert dev_logger.level == logging.DEBUG
    assert prod_logger.level == logging.INFO


def test_custom_log_level() -> None:
    """Test logger with custom log level."""
    configurator = LoggerConfigurator(log_level=logging.WARNING)
    logger = configurator.get_logger("test_custom")
    assert logger.level == logging.WARNING


def test_handler_formatting() -> None:
    """Test log message formatting."""
    logger = get_logger("test_format")
    for handler in logger.handlers:
        formatter = handler.formatter
        assert formatter is not None
        assert isinstance(formatter, logging.Formatter)
