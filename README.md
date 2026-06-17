# OrangeHRM UI Tests

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

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
pytest -v
```

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

Or with `make`:

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
