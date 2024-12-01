from setuptools import setup, find_packages

# Read version from src/__init__.py
with open("src/__init__.py", "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break

# Read requirements from requirements.txt
with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="m-ai",
    version=version,
    author="xtractor07",
    description="Advanced AI assistant based on Llama 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xtractor07/m-ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "isort>=5.0",
            "pre-commit>=2.0",
        ],
    },
    entry_points={
        'console_scripts': [
            'm-ai=m_ai.cli:main',
        ],
    },
)