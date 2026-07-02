#!/usr/bin/env bash
set -euo pipefail

readonly PROG_DIR=$(dirname $(realpath "$0"))
readonly COLAB_NOTEBOOKS_DIR="${PROG_DIR}/../notebooks"
readonly PI_NOTEBOOKS_DIR="${PROG_DIR}/../raspberry-pi/files/notebooks"

# Clean notebooks with nb-clean, preserving Colab-specific metadata (cellView, id, outputId)
find "$COLAB_NOTEBOOKS_DIR" "$PI_NOTEBOOKS_DIR" -type f -name "*.ipynb" -exec nb-clean clean --preserve-cell-metadata colab cellView id outputId -- {} \;
