#!/usr/bin/env bash

set -euo pipefail

RESULTS_DIR="${ALLURE_RESULTS_DIR:-allure-results}"
REPORT_DIR="${ALLURE_REPORT_DIR:-allure-report}"
PYTEST_ARGS_VALUE="${PYTEST_ARGS:-}"
PYTEST_MARKER_VALUE="${PYTEST_MARKER:-}"

mkdir -p "${RESULTS_DIR}" "${REPORT_DIR}"
rm -rf "${RESULTS_DIR}"/* "${REPORT_DIR}"/*

pytest_args=()

if [ -n "${PYTEST_MARKER_VALUE}" ]; then
    pytest_args+=("-m" "${PYTEST_MARKER_VALUE}")
fi

if [ -n "${PYTEST_ARGS_VALUE}" ]; then
    # Split CLI-style arguments from environment variable, for example: "-m smoke -k login".
    # shellcheck disable=SC2206
    extra_pytest_args=(${PYTEST_ARGS_VALUE})
    pytest_args+=("${extra_pytest_args[@]}")
fi

test_exit_code=0
pytest "${pytest_args[@]}" "$@" || test_exit_code=$?

if [ -n "$(find "${RESULTS_DIR}" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null)" ]; then
    allure generate "${RESULTS_DIR}" --clean -o "${REPORT_DIR}" || true
fi

exit "${test_exit_code}"
