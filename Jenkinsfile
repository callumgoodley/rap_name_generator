pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh "sudo docker-compose build --parallel"
            }
        }
        stage('Set env variables') {
            steps {
                sh "MY_SECRET_KEY=${MY_SERCRET_KEY}"
                sh "DB_USERNAME=${DB_USERNAME}"
                sh "DB_PASSWORD=${DB_PASSWORD}"
            }
        }
        stage('Test') { 
            steps {
                sh "sudo docker run -d -p 3306:3306 --name mysql-test mysql"
                sh "sudo docker exec -it mysql-test bash"
                sh "mysql --user=$DB_USERNAME --password=$DB_PASSWORD test << EOF CREATE DATABASE test; EOF"
                sh "python3 -m pytest"
                sh "sudo docker stop mysql-test"
                sh "sudo docker rm mysql-test"
            }
        }
        stage('Deploy') { 
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}
