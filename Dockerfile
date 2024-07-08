FROM python 
WORKDIR /app
COPY . /app
CMD ["python","test_docker.py"]
