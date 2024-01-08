def dock 
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
                    // The 'docker.build' should have a tag that usually includes a version number or 'latest'
                    dock = docker.build("project-tl:latest", "--no-cache -f Dockerfile .")
                }
            }
        }

        stage('run unitest') {
            steps {
                script {
                    // You need to reference 'dock' from the previous stage, which can be done by declaring it outside the stages block
                    def container = dock.run("--rm -d")
                    
                    container.inside {
                        // The commands inside here should be relevant to your unit tests
                        sh 'uname -n'
                        sh 'git status'
                        sh 'ls /'
                    }
                    
                    container.stop()
                }
            }
        }

        stage('upload-docker') {
            steps {
                echo 'hello world'
                // You should include steps to push the Docker image to a registry here
            }
        }
    }
    
}
