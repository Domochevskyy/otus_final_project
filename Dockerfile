FROM python:3.10
USER root
WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
CMD ['pytest', '--browser=chrome', '--host=192.168.1.5:8081', '--executor=192.168.1.5', '--alluredir=allure-results']
