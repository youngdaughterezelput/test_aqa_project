# Allure And Jenkins

## What Is Configured

- Failed page steps attach screenshots to Allure
- Failed tests also get a fallback screenshot on the test level
- Docker test run generates:
  - `allure-results/`
  - `allure-report/`
- Jenkins can publish `allure-results/` through the Allure plugin

## Why `permission denied` Happened

The error:

```text
exec ./scripts/run_tests_with_allure.sh: permission denied
```

happened because Docker Compose mounts the project directory with:

```yaml
- .:/app
```

That bind mount overrides the executable bit that was set inside the image.  
Your local file [scripts/run_tests_with_allure.sh](scripts/run_tests_with_allure.sh) is currently not executable, so direct `exec ./scripts/run_tests_with_allure.sh` fails.

It is now fixed by running the script through `bash`:

```yaml
command: bash /app/scripts/run_tests_with_allure.sh
```

and in the image:

```dockerfile
CMD ["bash", "/app/scripts/run_tests_with_allure.sh"]
```

This works even if the local file does not have `+x`.

## Why `allure-ui` Returned 403

The report container previously returned `403` because the report directory was empty when the static server started.

Flow is:

1. `tests` container must complete script startup
2. tests generate `allure-results/`
3. script generates `allure-report/`
4. only then `allure-ui` can serve HTML files

The report service now uses `nginx` again, but with:

- explicit `index index.html`
- explicit `try_files`
- startup validation that checks `/usr/share/nginx/html/index.html`

So if the report is missing, the container exits with a clear message instead of starting against an invalid directory.

If you see:

```text
Directory listing for /
```

it usually means the server is running, but the directory being served is not the generated Allure HTML root you expected.  
For this project, the main check is:

```bash
ls -la allure-report/index.html
```

If `index.html` exists, the report directory is generated correctly.

## Local Usage

### Run tests and generate Allure report

```bash
bash scripts/run_docker_tests.sh
```

Short alias:

```bash
make test-docker
```

This wrapper automatically:

1. removes old Compose containers before the run
2. starts the test stack
3. returns the real test exit code
4. removes containers after the run

So you do not need to manually delete stopped containers each time.

After the run you should have:

- `allure-results/`
- `allure-report/`

### Open generated HTML report

```bash
bash scripts/open_allure_report.sh
```

Short alias:

```bash
make allure
```

Then open:

```text
http://localhost:5252
```

### If report does not open

The helper script already checks that `allure-report/index.html` exists before starting the report server.

You can also verify it manually:

```bash
ls -la allure-report
```

If the directory is empty, first rerun:

```bash
bash scripts/run_docker_tests.sh
```

## Jenkins Strategy

Recommended approach:

1. run tests in Docker
2. generate `allure-results/`
3. optionally generate `allure-report/`
4. archive both directories
5. publish `allure-results/` with Jenkins Allure plugin

For Jenkins, `allure-results/` is the main artifact.  
`allure-report/` is useful as a backup HTML artifact, but the Jenkins UI should preferably render the report itself from `allure-results/`.

## Jenkins Setup

### 1. Install plugins

Required:

- `Allure Jenkins Plugin`
- `Pipeline`

Optional:

- `Docker Pipeline`

If your agent already has Docker and `docker compose`, `Docker Pipeline` is not strictly required.

### 2. Add Allure commandline tool

Go to:

`Manage Jenkins -> Tools`

Add:

- `Allure Commandline`
- Name: `allure`

Jenkins will use it when publishing results.

### 3. Ensure the agent can run Docker

The Jenkins agent must be able to execute:

```bash
docker compose up --build
```

That usually means:

- Docker is installed on the agent
- the Jenkins user has permission to run Docker

### 4. Create Pipeline job

Create a Pipeline job pointing to this repository.  
The repo already contains [Jenkinsfile](Jenkinsfile).

### 5. Run the job

The pipeline will:

1. checkout the repo
3. run `docker compose up --build --abort-on-container-exit --exit-code-from tests`
4. archive:
   - `allure-results/**`
   - `allure-report/**`
5. publish Allure report in Jenkins UI

## Jenkinsfile Behavior

Current [Jenkinsfile](Jenkinsfile):

- runs tests through Docker Compose
- archives Allure artifacts
- publishes Allure results
- always performs `docker compose down --remove-orphans`

## Recommended Jenkins Flow In Practice

After each build you will have:

- Jenkins build status from test exit code
- Allure report tab in Jenkins
- archived `allure-results`
- archived generated `allure-report`

## Useful Commands

Run tests:

```bash
bash scripts/run_docker_tests.sh
```

Stop containers:

```bash
docker compose down --remove-orphans
```

Short alias:

```bash
make clean-docker
```

Clean Allure artifacts:

```bash
make clean-allure
```

Serve generated report:

```bash
bash scripts/open_allure_report.sh
```
