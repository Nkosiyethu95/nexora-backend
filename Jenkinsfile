pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t nexora-backend:${BUILD_NUMBER} .'
            }
        }

        stage('Docker Verify') {
            steps {
                sh 'docker image inspect nexora-backend:${BUILD_NUMBER}'
            }
        }
    }

    post {
        success {
            echo 'Nexora backend CI pipeline succeeded!'
        }

        failure {
            echo 'Nexora backend CI pipeline failed.'
        }
    }
}
