pipeline {
    agent any

    stages {

        stage('Prepare') {
            steps {
                echo 'Preparing build environment...'
                sh 'ls -la'
                sh 'cat app.py'
                echo "Building image: atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    def image = docker.build("docker.io/atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}")
                    env.IMAGE_NAME = "atuljkamble/jenkins-docker-hello-world:${env.BUILD_ID}"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running container...'
                script {
                    // Stop any existing containers on port 5000
                    sh '''
                        EXISTING_CONTAINERS=$(docker ps -q --filter "publish=5000" || true)
                        if [ ! -z "$EXISTING_CONTAINERS" ]; then
                            docker stop $EXISTING_CONTAINERS || true
                        fi
                    '''
                    
                    def containerName = "jenkins-test-${env.BUILD_ID}"
                    env.CONTAINER_NAME = containerName
                    
                    def container = docker.image(env.IMAGE_NAME)
                                      .run("-d -p 5000:5000 --name ${containerName}")
                }
            }
        }
   
        stage('Test Docker Container') {
            steps {
                echo 'Testing Docker container...'
                script {
                    // Wait for container to be ready
                    sh 'sleep 10'
                    
                    // Check container status
                    sh "docker ps | grep ${env.CONTAINER_NAME} || (echo 'Container not running!' && exit 1)"
                    
                    // Test endpoints
                    sh '''
                        echo "Testing root endpoint..."
                        curl -f -s http://localhost:5000/ || exit 1
                        
                        echo "Testing greet endpoint..."
                        curl -f -s "http://localhost:5000/greet?name=Jenkins" || exit 1
                        
                        echo "All tests passed!"
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            script {
                // Stop and remove test container
                if (env.CONTAINER_NAME) {
                    sh "docker stop ${env.CONTAINER_NAME} || true"
                    sh "docker rm ${env.CONTAINER_NAME} || true"
                }
                
                // Clean up dangling images
                sh 'docker system prune -a || true'
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
