pipeline {
    agent any

    environment {
        VENV = "venv"
        IMAGE_NAME = "trading-order-service"
        IMAGE_TAG = "v1"
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

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    cd app/order-service
                    pytest -v
                '''
            }
        }

        stage('Verify Python Code') {
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

        stage('Check Docker') {
            steps {
                sh '''
                    docker --version
                    docker ps
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} app/order-service
                '''
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh '''
                    docker images | grep ${IMAGE_NAME}
                '''
            }
        }

        stage('Build Successful') {
            steps {
                echo '========================================='
                echo ' Trading SRE Platform Pipeline SUCCESS'
                echo '========================================='
            }
        }
    }

    post {

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }

        always {
            cleanWs()
        }
    }
}