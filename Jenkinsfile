pipeline {
    agent any

    stages {
        stage('git-clone') {
            steps {
                script {
                    // Clone the Git repository
                    //checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/edk2010/final-project.git']]])
                    git 'https://github.com/edk2010/final-project.git'

                }
            }
        }

        stage('build-docker') {
            steps {
                //script {
                    // Build Docker image
                    //dir('employees') {
                        //docker.build('project-tl:1')
                    //}
                }
            }
        }

        stage('upload-docker') {
            steps {
                echo 'hello world'
                
            }
        }

        
        }
    }