pipeline {
    agent {
        docker {
            image 'php:7.4-cli'
        }
    }
    
    stages {
        stage('version') {
            steps {
                sh 'php --version'
            }
        } 
          stage('Build') {
            steps {
                sh 'php -l *.php'
            }
        }
        
//         stage('chmod'){
//             steps{
//                 sh 'sudo chmod -R 777 / && cd / && mkdir .composer'
//                 sh 'sudo chmod -R 777 /.composer'
//             }
//         }
        
        stage('Install Composer') {
            steps {
                sh ' curl -sS https://getcomposer.org/installer |  php'
       
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'php composer.phar require'
                sh 'php composer.phar install && php composer.phar update'
            }
        }
        
        stage('Install PHPUnit') {
            steps {
                sh 'php composer require --dev phpunit/phpunit'
            }
        }
        stage('Test') {
            steps {
                sh 'phpunit .'
            }
        }
    }
}
