### 1- Install UV

On macOS/Linux:

```shell
curl -Ls https://astral.sh/uv/install.sh | sudo sh
```

On Windows (PowerShell as admin):

```shell
irm https://astral.sh/uv/install.ps1 | iex
```

or via Homebrew:

```shell
brew install uv
```

Verify:

```shell
uv self version
```

### 2. Initialize a Python Project

```shell
uv init my-app
cd my-app
```

You’ll get a project scaffold:

```
my-app/
├── .venv/
├── .python-version
├── pyproject.toml
├── hello.py
└── README.md
```

### 3. Add Dependencies

Say you’re building a data pipeline:

```shell
uv add pandas numpy
```

This installs the packages, creates the virtual environment, resolves versions, and updates pyproject.toml + uv.lock.

Example pyproject.toml:

```shell
[project]
name = "my-app"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = [
    "pandas>=2.2.2",
    "numpy>=2.0.0"
]
```

To remove packages:

```shell
uv remove pandas
```

### 4. Run Your Python App

Use uv run instead of activating .venv manually:

```shell
uv run hello.py
```

Need to run your full app?

```shell
uv venv exec python src/main.py
```

This ensures your script runs in the right environment, every time.

### Python Version Management with UV

UV can manage Python versions per project via .python-version.

List Installed Versions:

```shell
uv python list --only-installed
```

### Switch Versions:

1. Edit .python-version to e.g. 3.11.7
2. Run:

```shell
uv sync
```

If that version isn’t installed, UV downloads it and rebuilds the environment.

### Sync Dependencies

Changed the Python version? Resync everything:
```shell
uv pip install -e .
```
Want reproducible installs? Use:

```shell
uv pip compile pyproject.toml --group dev --generate-hashes -o requirements.txt
```

Source: [link](https://medium.com/@philip.mutua/python-uv-pyproject-toml-the-fastest-way-to-run-python-apps-913d6213c111)
