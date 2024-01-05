pipeline {
    agent { label 'workers' }
    stages {
        stage('hello') {
            steps {
                echo 'Hello World!!!'
            }
        }
        stage('cat') {
            when {
                branch 'dev*'
            }
            steps {
                sh '''
                cat README.md
                '''
            }
        }
    }
}
