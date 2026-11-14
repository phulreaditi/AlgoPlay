#!/usr/bin/env bash
# AlgoPlay launcher for macOS and Linux
set -e

if command -v python3 &>/dev/null; then
    python3 main.py "$@"
elif command -v python &>/dev/null; then
    python main.py "$@"
else
    echo "Python 3 is required to run AlgoPlay."
    exit 1
fi
