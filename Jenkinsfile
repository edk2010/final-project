import groovy.json.JsonSlurper
import net.sf.json.JSONArray
pipeline {
    agent any
    stages{
        stage('git-clone') {
            steps {
                //checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/edk2010/final-project.git']])
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
                       sh 'python -m unittest unitest.py'
                       
                   }
                   
              }
          }
      }

        

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
         stage ('Terraform Apply & Deploy lambda and s3'){
            steps {
            sh "terraform apply -auto-approve"
        }
      }
         



 
    stage('run API unitest') {
           steps {
               script {
                   // Start a container and keep it running
                   //dockerImage.inside("-u root") {
                       // Execute your unit test commands here
                       
                       def terraform_state = readJSON file: "./terraform.tfstate"
                       sh "export API_URL=${terraform_state.outputs.lambda_function_url["value"]}"
                       sh "python -m unittest unitest_api.py"
                       
                   //}
                   
              }
          }
      }
    }
    
}

   
