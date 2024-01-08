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
                    dockerImage = docker.build("project-tl:latest", "--no-cache -f Dockerfile .")
                }
            }
        }

        stage('run unitest') {
            steps {
                script {
                    // Start a container and keep it running
                    dockerImage.inside("-u root") {
                        // Execute your unit test commands here
                        sh 'uname -n'
                        sh 'git status'
                        sh 'ls /'
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

    post {
        always {
            // Post-build actions
        }
    }
}
