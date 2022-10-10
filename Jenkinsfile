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
        
        stage('Code Security') {
            steps {
                sh "bandit -r ./ >> bandit_results.txt"
                sh "cat bandit_results.txt"
            }
        }

        stage('Unit Tests') {
            steps {
                sh "pytest tests/ -v --tb=native >> pytest_results.txt"
                sh "cat pytest_results.txt"
            }
        }
    }
}
