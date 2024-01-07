def dock;
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
        / steps {
             // One or more steps need to be included within the steps block.
                }

            agent {
                 dockerfile {
                filename 'Dockerfile'
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