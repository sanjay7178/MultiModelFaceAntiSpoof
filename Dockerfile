# Stage 1: Build Flask App
FROM python:3.9-slim-buster AS flask_app_builder

RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /flask_app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY flask_app/static/ /flask_app/static/
COPY flask_app/detector/ /flask_app/detector/
COPY flask_app/models/ /flask_app/models/
COPY flask_app/app.py /flask_app/app.py
COPY flask_app/wsgi.py /flask_app/wsgi.py

# Stage 2: Build Nginx
FROM nginx:1.15.8 AS nginx_builder

RUN rm /etc/nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/project.conf /etc/nginx/conf.d/

# Stage 3: Final Image
FROM python:3.9-slim-buster

# Install system dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the built Flask app from Stage 1
COPY --from=flask_app_builder /flask_app /flask_app

# Copy the built Nginx configuration from Stage 2
COPY --from=nginx_builder /etc/nginx /etc/nginx

# Expose the ports
EXPOSE 8000
EXPOSE 80

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "wsgi:app"]
