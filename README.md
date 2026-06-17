# Test UI Tests

UI test framework for OrangeHRM demo using Playwright, Pytest, Page Object, and Pydantic-based configuration.

## Stack

- Python
- Pytest
- Playwright
- Pydantic / pydantic-settings
- Docker Compose
- Allure

## Project structure

```text
.
├── config/
├── pages/
├── tests/
├── conftest.py
├── docker-compose.yml
├── Dockerfile
├── pytest.ini
└── requirements.txt
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
cp .env.example .env
pytest -v
```

## Run in Docker

```bash
bash scripts/run_docker_tests.sh
```

Or with `make`:

```bash
make test-docker
```

## Allure

Failed steps automatically attach screenshots to Allure. A fallback screenshot is also attached at the test level if setup or test execution fails.

Local run with results:

```bash
pytest
```

Results are written to `allure-results/`.

Generate HTML report inside Docker:

```bash
bash scripts/run_docker_tests.sh
```

After the run you will have:

- `allure-results/` with raw Allure results
- `allure-report/` with generated HTML report

Open the generated report through a lightweight container:

```bash
bash scripts/open_allure_report.sh
```

Or with `make`:

```bash
make allure
```

Then open `http://localhost:5252`.

If Allure CLI is installed locally, you can also open raw results with:

```bash
allure serve allure-results
```

Detailed Allure and Jenkins setup is documented in [ALLURE_AND_JENKINS.md](/Users/rezelput/Documents/Projects/qa_framework_project/ALLURE_AND_JENKINS.md).

## Included tests

- Successful login
- Login with invalid password
- Dashboard availability after login

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