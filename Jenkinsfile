pipeline {
    agent any

    stages {
        stage('Code Formatting') {
            steps {
                sh "echo 'Running Isort formatting'" 
                sh 'python3.9 -m isort .'
                sh "echo 'Running Black formatting'"
                sh 'python3.9 -m black .'
                sh "echo 'Finished Code formatting'"
            }
        }
        stage('Unit Tests' ) {
            steps {
                sh "python3.9 -m unittest discover -s tests"
            }
        }
    }
}
