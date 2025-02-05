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
        // stage('SonarQube Analysis') {
        //     steps {
        //         echo 'Running SonarQube analysis...'
        //         withSonarQubeEnv("${SONARQUBE_SERVER}") {
        //             sh '''
        //             mvn sonar:sonar \
        //             -Dsonar.projectKey=jenkins \
        //             -Dsonar.host.url=http://172.20.10.2:9000 \
        //             -Dsonar.token=sqa_503f1d3f6931e73dff661ef9b573d2d41082245d
        //             '''
        //         }
        //     }
        // }
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