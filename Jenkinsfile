pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                git 'https://github.com/atulkamble/jenkins-docker-hello-world.git'
                // Add checkout steps here
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building...'
                docker.build("atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}")
                // Add build steps here
            }
        }

        stage ('Run Docker Container') {
            steps {
                echo 'Running...'
                script {
                    docker.image("atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}").run('-d -p 5000:5000')
                }
                // Add run steps here
            }
        }
   
        stage('Test Docker Container') {
            steps {
                echo 'Testing...'
                sh 'curl http://localhost:5000'
                // Add test steps here
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