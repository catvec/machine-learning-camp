#!/usr/bin/env bash
set -euo pipefail
readonly PROG_DIR=$(dirname $(realpath "$0"))

cd "$PROG_DIR"
~/.local/bin/uv run jupyter lab \
    --port=8999 \
    --ip='*' \
    --no-browser \
    --NotebookApp.token='' \
    --NotebookApp.password='' \
    --collaborative
