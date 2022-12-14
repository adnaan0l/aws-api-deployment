pipeline {
    agent any
    parameters {
        string(
            name: 'STACK_NAME', 
            defaultValue: 'sam-helloworld', 
            description: 'CloudFormation Stack Name'
        )
        string(
            name: 'IMAGE_REPO', 
            defaultValue: '744763296558.dkr.ecr.ap-south-1.amazonaws.com/test/sam-helloworld', 
            description: 'Image Repository'
        )
            
    }
    stages {
        stage('Code Formatting') {
            steps {
                sh """
                    echo 'Running Isort formatting'
                    python3.9 -m isort .
                    echo 'Running Black formatting'
                    python3.9 -m black .
                    echo 'Finished Code formatting'
                    echo ${params.STACK_NAME}
                """
            }
        }
        
        stage('Code Security') {
            steps {
                sh label: '', returnStatus: true, script: """
                        bandit -r . > bandit_results.txt
                        """
                sh "cat bandit_results.txt"
            }
        }

        stage('Unit Tests') {
            steps {
                sh label: '', returnStatus: true, script: """
                        pytest tests/ -v --tb=native > pytest_results.txt
                        """
                sh 'cat pytest_results.txt'
                
            }
        }

        stage('Deploy Serverless') {
            steps {
                withAWS(credentials: 'jenkins-user-creds', region: 'ap-south-1') {
                    sh """
                        sam validate
                        sam build
                        sam deploy --stack-name=${params.STACK_NAME} --image-repository=${params.IMAGE_REPO} --capabilities=CAPABILITY_IAM --on-failure=DELETE
                    """
                }
            }
        }
    }
}
