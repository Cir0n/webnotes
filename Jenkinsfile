pipeline {
    agent any
    tools {
        maven 'Maven'
        sonarQubeScanner 'SonarScanner' 
    }
    environment {
        SONARQUBE_SERVER = 'SonarQube'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the repository...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application with Maven...'
                sh 'mvn clean install'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') { 
                    sh '''
                    mvn sonar:sonar \
                    -Dsonar.projectKey=jenkins \
                    -Dsonar.host.url=http://172.20.10.2:9000 \
                    -Dsonar.token=$SONAR_TOKEN
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
