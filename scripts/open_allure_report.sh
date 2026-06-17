#!/usr/bin/env bash

set -euo pipefail

REPORT_INDEX="${ALLURE_REPORT_INDEX:-allure-report/index.html}"

if [ ! -f "${REPORT_INDEX}" ]; then
    echo "Allure report was not found: ${REPORT_INDEX}"
    echo "Run tests first: bash scripts/run_docker_tests.sh"
    exit 1
fi

echo "Serving Allure report from ${REPORT_INDEX}"
echo "Open http://localhost:5252 after the container starts"

docker compose --profile report up allure-ui
