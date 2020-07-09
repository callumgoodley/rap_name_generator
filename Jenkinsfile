pipeline {
    agent any 
    environment {
        MY_SECRET_KEY='aeiou'
        DB_USERNAME='callumgoodley'
        DB_PASSWORD='root'
    }
    stages {
        stage('Build') { 
            steps {
                sh "sudo docker-compose build --parallel"
            }
        }
        stage('Test') { 
            steps {
                sh "sudo docker run -d -p 3306:3306 --name mysql-test mysql"
                sh "sudo docker exec -T mysql-test bash"
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
