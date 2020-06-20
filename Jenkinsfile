node {
  stage('SCM') {
    git 'https://github.com/Dogan1998/Dogan1998-POC-AFSTL-.git'
  }
 
  stage('Build') {
            steps {
              echo 'Building.....'
                sh 'make' 
                archiveArtifacts artifacts: 'docker-compose.yml', fingerprint: true 
            }
        }


    stage('Test') {
            steps {
                  echo 'Testing.....'
                sh 'make check || true' 
                junit '**/resttest.py' 
            }
        }

    stage('SonarQube analysis') {
    def scannerHome = tool 'SonarScanner 4.0';
    withSonarQubeEnv('My SonarQube Server') {
      sh "${scannerHome}/bin/sonar-scanner"
    }

  stage('Deploy') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS' 
              }
            }
            steps {

                echo 'Deploying.....'
                sh 'make publish'
            }
        }
  }
}