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
                sh "sudo docker stop mysql-test"
                sh "sudo docker rm mysql-test"
                sh "sudo docker run -d -p 3306:3306 --name mysql-test mysql -e MYSQL_DATABASE=test"
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
