#!/bin/bash
set -euxo pipefail

poetry run isort clai/ tests/
poetry run black clai/ tests/
