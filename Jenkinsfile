pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    python --version
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    pip install -r app/order-service/requirements.txt
                '''
            }
        }

        stage('Verify Flask Application') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    cd app/order-service
                    python -m py_compile app.py
                    python -m py_compile database.py
                    python -m py_compile models.py
                '''
            }
        }

        stage('Build Successful') {
            steps {
                echo '======================================='
                echo ' Trading SRE Platform Build SUCCESS '
                echo '======================================='
            }
        }
    }

    post {
        always {
            cleanWs()
        }

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}