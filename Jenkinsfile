pipeline {
    agent any

    environment {
        IMAGE = "inventoryapp:latest"
        CONTAINER_NAME = "inventoryapp-container"
    }

    stages {
        steps {
                git branch: 'main',
                    url: 'https://github.com/VaibhavGumalwad/InventoryApp.git'
            }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh '''
                docker rm -f $CONTAINER_NAME || true
                docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE
                '''
            }
        }
    }
}

