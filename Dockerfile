FROM python:3.9-slim-buster
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir  -r requirements.txt
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get update && apt-get install -y python3-opencv
# RUN apt-get update && apt-get install -y --no-install-recommends \
#         libgl1 \
#         libglib2.0-0 \

COPY /detector /app/detector
COPY /models /app/models
COPY app3.py /app/app3.py
COPY .dockerignore /app/.dockerignore
COPY  . /app
EXPOSE 5000
CMD ["python3", "app3.py"]