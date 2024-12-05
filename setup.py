from setuptools import setup, find_packages
from pathlib import Path

# Requirements
try:
  this_directory = Path(__file__).absolute().parent
  with open((this_directory / "requirements.txt"), encoding = "utf-8") as f:
    requirements = f.readlines()
  requirements = [line.strip() for line in requirements]
except FileNotFoundError:
  requirements = []

# Metadata
setup(
  name = "michaelpy",
  version = "0.0.1",
  author = "Michael Schötz",
  author_email = "michael.schoetz@th-deg.de",
  description = "Demo Python package",
  license = "Apache License 2.0",
  packages = find_packages(),
  install_requires = requirements
)