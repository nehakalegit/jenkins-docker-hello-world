pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                git 'https://github.com/atulkamble/jenkins-docker-hello-world.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    image = docker.build("atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running container...'
                script {
                    container = docker.image("atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}")
                                  .run('-d -p 5000:5000')
                }
            }
        }
   
        stage('Test Docker Container') {
            steps {
                echo 'Testing...'
                sh 'sleep 5'    // Wait for container to start
                sh 'curl http://localhost:5000'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
