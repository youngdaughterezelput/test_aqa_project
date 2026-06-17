FROM mcr.microsoft.com/playwright/python:v1.60.0-jammy

ARG ALLURE_VERSION=2.34.1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends default-jre curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL -o /tmp/allure.tgz \
    "https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz" \
    && tar -zxf /tmp/allure.tgz -C /opt/ \
    && ln -s "/opt/allure-${ALLURE_VERSION}/bin/allure" /usr/bin/allure \
    && rm /tmp/allure.tgz

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "/app/scripts/run_tests_with_allure.sh"]
