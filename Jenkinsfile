pipeline {
    agent any
    stages {
    	stage("Build") {
            steps {
                echo "Hello everybody it is testing stage"
                sh "python3 server.py test"
            }
        }
        stage("Deploy to Production") {
            steps {
                
            }
        }
    }
}
