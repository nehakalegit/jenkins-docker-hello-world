pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                git branch: 'main', url: 'https://github.com/atulkamble/jenkins-docker-hello-world.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    image = docker.build("docker.io/atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running container...'
                script {
                    // Stop any existing containers on port 5000
                    sh 'docker stop $(docker ps -q --filter "publish=5000") || true'
                    
                    container = docker.image("atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}")
                                  .run('-d -p 5000:5000 --name jenkins-test-${env.BUILD_ID}')
                }
            }
        }
   
        stage('Test Docker Container') {
            steps {
                echo 'Testing...'
                sh 'sleep 10'    // Wait for container to start
                sh 'curl -f http://localhost:5000/ || exit 1'
                sh 'curl -f "http://localhost:5000/greet?name=Jenkins" || exit 1'
                echo 'All tests passed!'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            script {
                // Stop and remove test container
                sh "docker stop jenkins-test-${env.BUILD_ID} || true"
                sh "docker rm jenkins-test-${env.BUILD_ID} || true"
                
                // Clean up dangling images
                sh 'docker image prune -f || true'
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
