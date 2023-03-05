#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports clai/ tests/
poetry run isort --check --diff clai/ tests/
poetry run black --check clai/ tests/
poetry run flake8 clai/ tests/ --darglint-ignore-regex '^test_.*'
poetry run bandit -r --severity medium high clai/ tests/
poetry run vulture --min-confidence 100 clai/ tests/
echo "Lint successful!"