

pipeline {
    agent {
        docker {
            image 'php:7.4-cli'
        }
    }
    
    
        stage('version') {
            steps {
                sh 'php --version'
            }
        
          stage('build') {
            // Checkout the app at the given commit sha from the webhook
            checkout scm

            // Install dependencies, create a new .env file and generate a new key, just for testing
            sh "composer install"
            sh "cp .env.example .env"
            sh "php artisan key:generate"

            // Run any static asset building, if needed
            // sh "npm install && gulp --production"
        }

        stage('test') {
            // Run any testing suites
            sh "./vendor/bin/phpunit"
        }
        
    }
}
