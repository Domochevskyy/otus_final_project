TESTS_DIR ?= /app/tests
PYTEST_OPTIONS ?= --color=no --setup-show --alluredir=allure-results
IMAGE_NAME ?= opencart_tests_image
CONTAINER_NAME ?= opencart_tests_container


up_opencart:
	OPENCART_PORT=8081	\
	PHPADMIN_PORT=8888	\
	LOCAL_IP=$(hostname -I | grep -o "^[0-9.]*")	\
	docker-compose up  -d

build:
	docker build --tag $(IMAGE_NAME) .

tests: build
	docker run --name $(CONTAINER_NAME) \
			   --network selenoid \
			   --privileged	\
			   $(IMAGE_NAME) pytest $(PYTEST_OPTIONS) $(TESTS_DIR)
	docker cp $(CONTAINER_NAME):/app/allure-results .
	docker rm $(CONTAINER_NAME)

allure:
	allure generate --clean && allure open

down:
	OPENCART_PORT=8081	\
	PHPADMIN_PORT=8888	\
	LOCAL_IP=`hostname -I | grep -o "^[0-9.]*"`	\
	docker-compose down
