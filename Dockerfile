FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir  -r requirements.txt
COPY  . /app
EXPOSE 5000
CMD ["python3", "app3.py"]