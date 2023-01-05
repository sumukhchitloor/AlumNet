pipeline {
    agent {
        docker {
            image 'php:7.4-cli'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'php -l *.php'
            }
        }
        stage('Test') {
            steps {
                sh 'phpunit .'
            }
        }
    }
}