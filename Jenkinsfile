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

        stage('docker build and test'){
            agent { dockerfile true}
            steps {
                sh 'cd /app/final-project/employees'
                sh 'python unitest.py'

            }



        }

        stage('upload-docker') {
            steps {
                echo 'hello world'
                
            }
        }

        
        }
    }