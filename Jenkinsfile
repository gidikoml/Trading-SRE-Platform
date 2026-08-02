pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Trading SRE Platform...'
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r app\\order-service\\requirements.txt'
            }
        }

        stage('Build Completed') {
            steps {
                echo 'Trading SRE Platform Build Successful'
            }
        }

    }
}