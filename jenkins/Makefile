jenkins_image:
	docker build --tag jenkins_image - < $(CURDIR)/Dockerfile

jenkins_container:
	docker run --name jenkins_cont  \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v jenkins_home:/var/jenkins_home \
	-p 5050:8080 \
	-p 50000:50000 \
	jenkins_image

jenkins_start:
	docker start jenkins_cont -a
