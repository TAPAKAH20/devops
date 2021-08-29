pipeline {
    agent any

    stages {
    	stage('Checkout'){
    		steps{
    			checkout scm
    		}
    	}

    	stage('Setup') {
            steps {
                sh """
                	pip install -r python_app/requirements.txt
               	"""
            }
        }

        stage('Test') {
            steps {
                sh """
                	python python_app/tests.py
                """
            }
        }

        stage('Buld') {
            steps {
                sh """
                	cd python_app
                	docker build -t r0ach20/devops:latest .
                """
            }
        }

        stage('Publish'){
        	steps{
        		withCredentials([usernamePassword(credentialsId: '98d6f53c-126c-4739-a69e-e5ae9234b53b', usernameVariable: 'HUB_USER', passwordVariable: 'HUB_TOKEN')]) {
        			sh"""
        				docker login -u $HUB_USER -p $HUB_TOKEN 
        				docker image push $HUB_USER/devops:latest
        			"""
        		}

        	}
        }
    }
}
