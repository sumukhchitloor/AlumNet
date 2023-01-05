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
                sh 'curl -L https://phar.phpunit.de/phpunit.phar > phpunit.phar'
                sh 'chmod +x phpunit.phar'
                sh 'mv phpunit.phar /usr/local/bin/phpunit'
            }
        }
        stage('Test') {
            steps {
                sh 'phpunit .'
            }
        }
        stage('Build Image') {
            steps {
                script {
                    def registry = 'alumnet/alumnet'
                    def image = 'myphpapp'
                    def tag = "${registry}/${image}:${env.BUILD_NUMBER}"
                    docker.build("${tag}", '.')
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
                    def registry = 'alumnet/alumnet'
                    def image = 'myphpapp'
                    def tag = "${registry}/${image}:${env.BUILD_NUMBER}"
                    sh "docker push ${tag}"
                }
            }
        }
    }
}
