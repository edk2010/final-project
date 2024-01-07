
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
            steps {
             script {
                  def dock = docker.build("project-tl:1", "--no-cache -f Dockerfile .")
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