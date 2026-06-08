# Password Checker

[![CI](https://github.com/NaamaTzadok/password_checker/actions/workflows/ci.yml/badge.svg)](https://github.com/NaamaTzadok/password_checker/actions/workflows/ci.yml)

A small Python password strength checker that evaluates a password based on length, lowercase letters, uppercase letters, numbers, and special characters.

## What it does

When run, the project prompts the user for a password using a hidden input. It calculates a strength score from 0 to 5 and prints a user-friendly strength level:

- Super Weak 🥶
- Very Weak ⚠️
- Weak 👎🏽
- Medium 👍🏽
- Strong 💪🏽
- Very Strong 🔥

The scoring rules are:

- `+1` if the password is at least 8 characters long
- `+1` if it contains a lowercase letter
- `+1` if it contains an uppercase letter
- `+1` if it contains a digit
- `+1` if it contains a special character

## Requirements

- Python 3.14 or later

## Installation

Install the package in editable mode and install development dependencies with `uv`:

```bash
python -m pip install -e .
uv sync --dev
```

## Running

Run the script from the repository root:

```bash
python main.py
```

Enter a password when prompted and the checker will output the corresponding strength level.

## Testing

Run the test suite with pytest:

```bash
uv run pytest
```

## CI

This repository includes a GitHub Actions workflow at `.github/workflows/ci.yml`. The CI pipeline checks formatting, static typing, and test coverage:

- `uv run ruff check .`
- `uv run ruff format --check .`
- `uv run ty check`
- `uv run pytest --cov --cov-fail-under=80`
