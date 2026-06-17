pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Env') {
            steps {
                sh '''
                    if [ ! -f .env ]; then
                      cp .env.example .env
                    fi
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose up --build --abort-on-container-exit --exit-code-from tests'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**, allure-report/**', allowEmptyArchive: true
            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            )
            sh 'docker compose down --remove-orphans || true'
        }
    }
}
