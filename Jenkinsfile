pipeline {
    agent any
    
    stages {
        stage('git-clone') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                script {
                    // Build the Docker image and tag it
                    dockerImage = docker.build("project-tl:latest", "--no-cache -f Dockerfile .")
                }
            }
        }

        stage('run unitest') {
            steps {
                script {
                    // Use 'dockerImage.inside' to run commands inside the Docker container
                    dockerImage.inside {
                        sh 'uname -n'
                        sh 'git status'
                        sh 'ls /'
                        // Include your unit test commands here
                    }
                }
            }
        }

        stage('upload-docker') {
            steps {
                echo 'hello world'
                // Add Docker push commands here if necessary
            }
        }
    }

    
}
