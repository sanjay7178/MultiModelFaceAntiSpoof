FROM python:3.9-slim-buster
# Install system dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1\
    libglib2.0-0 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /flask_app
COPY requirements.txt ./requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir  -r requirements.txt


COPY detector /flask_app/detector
COPY models /flask_app/models
COPY flask_app/app.py /flask_app/app3.py
COPY wsgi.py /flask_app/wsgi.py
COPY .dockerignore /flask_app/.dockerignore
# COPY  . /app
# EXPOSE 5000
# CMD ["python3", "app3.py"]