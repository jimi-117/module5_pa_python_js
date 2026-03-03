from nox import Session, options
from nox_uv import session # type: ignore

options.default_venv_backend = "uv"
options.reuse_existing_virtualenvs = True

PYTHON_VERSIONS = [
    # "3.12",
    # "3.13",
    "3.14",
]

@session(PYTHON_VERSIONS=PYTHON_VERSIONS, uv_only_groups=["dev"])
def format(s: Session) -> None:
    s.run("ruff", "format", "src")