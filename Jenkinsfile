pipeline {
	agent any

	environment {
		DOCKERHUB_CREDENTIALS = 'dockerhub-creds'
		DOCKER_IMAGE = 'maikhoinka/flash-api'
		IMAGE_TAG = "v${env.BUILD_NUMBER}"
	}
	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}
		stage('Build Docker Image') {
			steps {
				echo "Starting to build image: ${DOCKER_IMAGE}:${IMAGE_TAG}..."
				sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
				sh "docker build -t ${DOCKER_IMAGE}:latest ."
			}
		stage('Push to docker hub') {
			steps {
				echo "Login to Docker Hub..."
				withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CREDENTIALS, passwordVariable: 'DOCKERHUB_PASS', usernameVariable: 'DOCKERHUB_USER')]) {
					sh "echo \$DOCKERHUB_PASS | docker login -u \$DOCKERHUB_USER --password-stdin"
					echo "Sending images to the world..."
					sh "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
					sh "docker push ${DOCKER_IMAGE}:latest"
				}
			}
		}
	}
}
}
