import groovy.json.JsonSlurper
pipeline {
    agent any
    stages{
        stage('git-clone') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/edk2010/final-project.git']])
            }
        }

        //stage('Build image') {
         //   steps {
         //       script {
          //          dockerImage = docker.build("project-tl:latest", "--no-cache -f Dockerfile .")
          //      }
          //  }
        //}

        //stage('run unitest') {
         //   steps {
         //       script {
                    // Start a container and keep it running
          //          dockerImage.inside("-u root") {
          //              // Execute your unit test commands here
          //              sh 'python -m unittest unitest.py'
                        
           //         }
                    
           //     }
           // }
      //  }

        stage('upload-docker') {
            steps {
                echo 'hello world'
                
            }
       
         }
          stage ('Terraform Init'){
            steps {
            sh "terraform init"
          }
       }
         stage ('Terraform Plan'){
            steps {
            sh "terraform plan" 
         }
      }
         stage ('Terraform Apply & Deploy Docker Image on Webserver'){
            steps {
            sh "terraform apply -auto-approve"
        }
      }
         


        stage('get lambda_function_url') {
            steps {
                script {
                    def jsonSlurper = new JsonSlurper()
                    def output = sh(script: 'terraform output -json', returnStdout: true).trim()
                    def jsonOutput = jsonSlurper.parseText(output)

                    echo "lambda_function_url: ${jsonOutput.lambda_function_url.value}"
                }
            }
        
        }


    }
    
}

   
