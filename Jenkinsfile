
pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        AWS_ACCOUNT_ID = '130115303986'
        ECR_REPOSITORY = 'nexora-backend'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        IMAGE_URI = "${ECR_REGISTRY}/${ECR_REPOSITORY}"
    }

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
                sh '''
                    docker build -t ${IMAGE_URI}:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Docker Verify') {
            steps {
                sh '''
                    docker image inspect ${IMAGE_URI}:${BUILD_NUMBER}
                '''
            }
        }

        stage('ECR Login') {
            steps {
                sh '''
                    #!/bin/bash
                    aws ecr get-login-password --region ${AWS_REGION} |
                    docker login --username AWS --password-stdin ${ECR_REGISTRY}
                '''
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    docker push ${IMAGE_URI}:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo "Nexora image ${IMAGE_URI}:${BUILD_NUMBER} published successfully!"
        }

        failure {
            echo 'Nexora CI/CD pipeline failed.'
        }
    }
}
