import toml
from pathlib import Path

__root__ = Path(__file__).parents[0]

version_file = __root__.joinpath("version.txt")

version_file.write_text(f"{toml.load(Path(__file__).parents[3].joinpath('pyproject.toml'))['tool']['poetry']['version']}\n")

__version__ = version_file.read_text().strip()

