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
            when {
                branch 'main'
                }
            steps {
            sh "terraform apply -auto-approve"
        }
      }
         



 
    stage('run API unitest') {
        when {
            branch 'main'
            }
           steps {
            //node {
               script {
                   // Start a container and keep it running
                   /function_name      = aws_lambda_function.test_lambda.function_name
                    authorization_type = "NONE"/dockerImage.inside("-u root") {
                       
                       
                       def terraform_state = readJSON file: "./terraform.tfstate"
                       //sh "export API_URL=${terraform_state.outputs.lambda_function_url["value"]}"
                       //sh 'echo $API_URL'
                       sh "python unitest_api.py ${terraform_state.outputs.lambda_function_url["value"]}"
                       
                   }
                   
             // }
          }
      }
    }
    
}

   
