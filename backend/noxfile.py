from __future__ import annotations
from nox import Session, options
from nox_uv import session # type: ignore

options.default_venv_backend = "uv"
options.reuse_existing_virtualenvs = True

PYTHON_VERSIONS = [
    # "3.12",
    # "3.13",
    "3.14",
]

@session(python=PYTHON_VERSIONS, uv_only_groups=["dev"])
def format(s: Session) -> None:
    s.run("ruff", "format", "api")
    s.run("ruff", "check", "--fix","api")

@session(python=PYTHON_VERSIONS, uv_only_groups=["dev"])
def lint(s: Session) -> None:
    s.run("ruff", "check", "api")

@session(python=PYTHON_VERSIONS, uv_groups=["dev"])
def type_check(s: Session) -> None:
    s.run("mypy", "api")

@session(python=PYTHON_VERSIONS, uv_groups=["dev"])
def unit_test(s: Session) -> None:
    s.run("pytest","--cov")


@session
def all(s: Session) -> None:
    s.notify("format")
    s.notify("lint")
    s.notify("type_check")
    s.notify("unit_test")
    # s.notify("security")