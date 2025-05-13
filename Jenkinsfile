pipeline {
    agent any

    environment {
        IMAGE_NAME = "inventoryapp"
        CONTAINER_NAME = "inventoryapp-container"
        PORT = "8000"
    }
     

    stages {
       stage('Install SQLite3') {
    steps {
        sh '''
            bash -c "
                sudo apt-get update &&
                sudo apt-get install -y sqlite3 libsqlite3-dev
            "
        '''
    }
}
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/VaibhavGumalwad/InventoryApp.git'
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    bash -c "source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Remove Old Container (if any)') {
            steps {
                sh '''
                    if [ $(docker ps -aq -f name=${CONTAINER_NAME}) ]; then
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                    fi
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh "docker run -d -p ${PORT}:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo "app is running at http://<jenkins-server-ip>:${PORT}"
        }
        failure {
            echo "build failed. Check logs for details."
        }
    }
}
