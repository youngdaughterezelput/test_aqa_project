#!/usr/bin/env bash

set -euo pipefail

RESULTS_DIR="${ALLURE_RESULTS_DIR:-allure-results}"
REPORT_DIR="${ALLURE_REPORT_DIR:-allure-report}"

mkdir -p "${RESULTS_DIR}" "${REPORT_DIR}"
rm -rf "${RESULTS_DIR}"/* "${REPORT_DIR}"/*

test_exit_code=0
pytest "$@" || test_exit_code=$?

if [ -n "$(find "${RESULTS_DIR}" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null)" ]; then
    allure generate "${RESULTS_DIR}" --clean -o "${REPORT_DIR}" || true
fi

exit "${test_exit_code}"
