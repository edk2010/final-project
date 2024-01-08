def dockerImage;
pipeline {
    agent any



    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/edk2010/final-project.git']])
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("project-tl:1", "--no-cache -f Dockerfile .")
                }
            }

        }

        stage('Run unittest') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'ls /'
                        sh 'pwd'
                    }
                }
            }
        }
        
        
       

    }

}