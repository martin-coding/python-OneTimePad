# python-OneTimePad
A GUI application for easy use of one-time pad encryption written in Python.

## Installation

### Python package (.tar.gz or .whl)

1. With uv: `uv tool install --force one_time_pad-0.1.0.tar.gz`
1. With pipx: `pipx install --force one_time_pad-0.1.0.tar.gz`

## Development

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Setup environment with `uv sync -all-extras --dev`
3. Run package with `uv run one-time-pad`
4. Create ui-files with the QtDesigner `uv run pyside6-designer`
5. Compile ui-files with `uv run pyside6-uic window.ui -o ui_window.py`
