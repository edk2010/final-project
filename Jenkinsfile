pipeline {
    
    agent any
    
    stages {
        stage('git-clone') {
            steps {
                //script {
                    // Clone the Git repository
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/edk2010/final-project.git']])
                    //git 'https://github.com/edk2010/final-project.git'
                    //git branch: 'main', url: 'https://github.com/edk2010/final-project.git'

                //}
            }
        }

        stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

            app = docker.build("final-project/project-tl")
            }



        }

        stage('upload-docker') {
            steps {
                echo 'hello world'
                
            }
        }

        
        }
    }