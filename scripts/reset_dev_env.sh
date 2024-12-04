#!/bin/bash

echo "Starting development environment reset..."

# Deactivate virtual environment if it's active
if [[ -n "${VIRTUAL_ENV}" ]]; then
    echo "Deactivating current virtual environment..."
    deactivate || true
fi

# Remove existing virtual environment
echo "Removing existing virtual environment..."
rm -rf .venv

# Remove pytest cache
echo "Cleaning up cache files..."
rm -rf .pytest_cache

# Remove Python cache files
find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete

# Create new virtual environment with Python 3.11
echo "Creating new virtual environment with Python 3.11..."
python3.11 -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies in order
echo "Installing core dependencies..."
pip install wheel setuptools

echo "Installing PyTorch..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo "Installing development dependencies..."
pip install -r requirements-dev.txt

echo "Installing project in development mode..."
pip install -e .

echo "Installing and configuring pre-commit..."
# Install pre-commit
pip install pre-commit

# Reinstall pre-commit hooks
pre-commit uninstall || true
pre-commit clean || true
pre-commit install

echo "Development environment has been reset and reinstalled!"
echo "Python version:"
python --version
echo "PyTorch version:"
python -c "import torch; print(torch.__version__)"
