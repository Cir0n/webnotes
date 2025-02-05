pipeline {
    agent any
    tools {
        maven 'Maven'
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
            environment {
                SONAR_HOST_URL = 'http://172.20.96.1:32768/' 
            }
            steps {
                sh 'mvn sonar:sonar -Dsonar.projectKey=sample_project -Dsonar.host.url=$SONAR_HOST_URL -Dsonar.token=squ_301db00bed26b40b6239f3721fa74b1308751ded'
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
