pipeline {
    agent any   // Run on any available Jenkins agent

    environment {
        // Name of the Docker image we will build
        IMAGE_NAME = "nehakaledocker/jenkins-docker-hello-world:${env.BUILD_ID}"

        // Name of the container we will run
        CONTAINER_NAME = "my-test-container-${env.BUILD_ID}"
    }

    stages {

        stage('1. Check Project Files') {
            steps {
                echo "Listing the files in the project folder..."
                sh "ls -la"   // Show all files so we know what's here
            }
        }

        stage('2. Build Docker Image') {
            steps {
                echo "Building Docker image: ${env.IMAGE_NAME}"
                sh "docker build -t ${env.IMAGE_NAME} ."  
                // This builds an image using the Dockerfile in this folder
            }
        }

        stage('3. Run the App in Docker') {
            steps {
                echo "Running the app inside a Docker container..."

                // Stop and remove old container (if exists) so it doesn't conflict
                sh "docker stop ${env.CONTAINER_NAME} || true"
                sh "docker rm ${env.CONTAINER_NAME} || true"

                // Start a new container on port 5000
                sh "docker run -d -p 5000:5000 --name ${env.CONTAINER_NAME} ${env.IMAGE_NAME}"
                // -d = run in background
                // -p = map port 5000 on container to port 5000 on host
            }
        }

        stage('4. Test the App') {
            steps {
                echo "Testing the app to check if it works..."

                sh "sleep 5"  // Give the app a few seconds to start

                // Test the homepage "/"
                sh "curl http://localhost:5000/"

                // Test the greet endpoint
                sh "curl http://localhost:5000/greet?name=Jenkins"
            }
        }
    }

    post {
        always {
            echo "Cleaning up Docker container..."

            // Stop the container when pipeline is finished
            sh "docker stop ${env.CONTAINER_NAME} || true"

            // Remove the container
            sh "docker rm ${env.CONTAINER_NAME} || true"
        }
    }
}
