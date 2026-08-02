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
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r app/order-service/requirements.txt'
            }
        }

        stage('Build Completed') {
            steps {
                echo 'Trading SRE Platform Build Successful'
            }
        }
    }
}