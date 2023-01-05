pipeline {
    agent {
        docker {
            image 'php:7.4-cli'
//             volumes:
//                 - /var/run/docker.sock:/var/run/docker.sock

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
        
        stage('Docker install') {
            steps {
                sh 'curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz'
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
