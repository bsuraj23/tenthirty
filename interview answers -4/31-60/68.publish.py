#67.How do you build and publish a Python package to PyPI?
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
description = "A simple example package"
readme = "README.md"
requires-python = ">=3.8"
license = { file = "LICENSE" }
authors = [
  { name = "Your Name", email = "you@example.com" }
]

dependencies = [
  "requests>=2.0"
]

[project.urls]
Homepage = "https://github.com/yourusername/mypackage"


