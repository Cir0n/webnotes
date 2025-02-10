pipeline {
    agent any
    tools {
        maven 'Maven'
    }
    environment {
        ZAP_HOST = "127.0.0.1"
        ZAP_PORT = "8080"
        SITE_URL = "http://localhost:8080" // URL de ton site en local
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
                SONAR_HOST_URL = 'http://172.17.0.3:9000/' 
                SONAR_AUTH_TOKEN = credentials('SONAR_TOKEN') 
            }
            steps {
                sh 'mvn sonar:sonar -Dsonar.projectKey=sample_project -Dsonar.host.url=$SONAR_HOST_URL -Dsonar.token=$SONAR_AUTH_TOKEN'
            }
        }
        stage('Start OWASP ZAP') {
            steps {
                echo "Starting OWASP ZAP in Docker..."
                sh "docker run -d -p 8080:8080 owasp/zap2docker-stable zap.sh -daemon -host 0.0.0.0 -port 8080"
                sleep(time: 10, unit: 'SECONDS') // Attendre que ZAP démarre
            }
        }
        stage('Run OWASP ZAP Scan') {
            steps {
                echo "Running OWASP ZAP scan on local site..."
                sh """
                curl "http://$ZAP_HOST:$ZAP_PORT/JSON/ascan/action/scan/?url=$SITE_URL&recurse=true&inScopeOnly=true"
                """
            }
        }
        stage('Generate OWASP ZAP Report') {
            steps {
                echo "Generating OWASP ZAP report..."
                sh """
                curl "http://$ZAP_HOST:$ZAP_PORT/OTHER/core/other/htmlreport/" -o ZAP_Report.html
                """
                archiveArtifacts artifacts: 'ZAP_Report.html', fingerprint: true
            }
        }
        stage('Shutdown OWASP ZAP') {
            steps {
                echo "Stopping OWASP ZAP..."
                sh "curl http://$ZAP_HOST:$ZAP_PORT/JSON/core/action/shutdown/"
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
