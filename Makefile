.PHONY: test-docker allure clean-docker clean-allure

test-docker:
	bash scripts/run_docker_tests.sh

test-docker-smoke:
	PYTEST_MARKER=smoke bash scripts/run_docker_tests.sh

test-docker-reset:
	PYTEST_MARKER=smoke_reset bash scripts/run_docker_tests.sh

test-docker-board:
	PYTEST_MARKER=smoke_dashboard bash scripts/run_docker_tests.sh

allure:
	bash scripts/open_allure_report.sh

clean-docker:
	docker compose down --remove-orphans

clean-allure:
	rm -rf allure-results allure-report
