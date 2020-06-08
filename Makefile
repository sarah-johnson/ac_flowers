DOCKER_IMAGE_NAME=ac_flowers
DOCKER_IMAGE_TAG=$(shell git rev-parse --short HEAD)

docker-build:
	docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} .

docker-run: docker-build
	docker run --rm \
	-p 5000:5000 \
	${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}
