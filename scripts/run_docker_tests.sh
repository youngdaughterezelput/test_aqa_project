#!/usr/bin/env bash

set -euo pipefail

cleanup() {
    docker compose down --remove-orphans >/dev/null 2>&1 || true
}

cleanup
trap cleanup EXIT

docker compose up --build --abort-on-container-exit --exit-code-from tests "$@"
