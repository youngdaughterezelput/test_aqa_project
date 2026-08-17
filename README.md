# UI Tests (pet project)

UI test framework for OrangeHRM demo using Playwright, Pytest, Page Object, and Pydantic-based configuration.

## Stack

- Python
- Pytest
- Playwright
- Pydantic / pydantic-settings
- Docker Compose
- Allure
- GitHub Actions
- GitHub Pages

## Project Structure

```text
.
├── .github/workflows/
├── config/
├── docker/nginx/
├── helpers/
├── pages/
├── scripts/
├── tests/
├── conftest.py
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── Makefile
├── pytest.ini
└── requirements.txt
```

## Setup

The project uses Python 3.12.7. If you use `pyenv`, select the project version
before creating the virtual environment:

```bash
pyenv local 3.12.7
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install
python -m pytest -v
```

If `.venv` was previously created with another Python version, remove and recreate
it after selecting Python 3.12.7.

Optional: create `.env` if you want to override default settings.

```bash
cp .env.example .env
```

The project uses `pydantic-settings`.

- If `.env` exists, its values override defaults from `config/settings.py`
- If `.env` does not exist, the framework still runs using built-in defaults

## Run In Docker

```bash
bash scripts/run_docker_tests.sh
```

Or with `make` (example):

```bash
make test-docker
```

This wrapper automatically:

1. removes old Compose containers before the run
2. starts the test stack
3. returns the real test exit code
4. removes containers after the run

## Allure

Failed steps automatically attach screenshots to Allure.
A fallback screenshot is also attached at the test level if setup or test execution fails.

After the Docker run you will have:

- `allure-results/` with raw Allure results
- `allure-report/` with generated HTML report

Open the generated report:

```bash
bash scripts/open_allure_report.sh
```

Or with `make`:

```bash
make allure
```

Then open:

```text
http://localhost:5252
```

If Allure CLI is installed locally, you can also open raw results with:

```bash
allure serve allure-results
```

## Useful Make Commands

Run Docker tests:

```bash
make test-docker
```

Run Docker tests by marker:

```bash
PYTEST_MARKER=smoke bash scripts/run_docker_tests.sh
PYTEST_MARKER=smoke_reset bash scripts/run_docker_tests.sh
PYTEST_ARGS="-m smoke_reset -k cancel" bash scripts/run_docker_tests.sh
```

Or with `make`:

```bash
make test-docker-smoke
make test-docker-reset
```

Open Allure report:

```bash
make allure
```

Stop Docker containers:

```bash
make clean-docker
```

Remove Allure artifacts:

```bash
make clean-allure
```

## GitHub Actions And Pages

The repository includes:

- `.github/workflows/ui-tests.yml` for running UI tests
- `.github/workflows/allure-pages.yml` for publishing Allure HTML to GitHub Pages

To enable published Allure reports:

1. Open `Settings -> Pages` in your GitHub repository
2. In `Source`, select `GitHub Actions`
3. Run the `UI Tests` workflow
4. After a successful run, the `Publish Allure Report` workflow will deploy the report

You will then get a Pages URL like:

```text
https://<github-username>.github.io/<repository-name>/
```

You can also open the latest deployment from the `Actions` or `Deployments` tab in GitHub.

## Jenkins

Detailed Allure and Jenkins setup is documented in `ALLURE_AND_JENKINS.md`.

## Included Tests

- Successful login
- Login with invalid password
- Forgot password navigation
- Reset password page checks
- Login page social icons
- Login page branding checks
