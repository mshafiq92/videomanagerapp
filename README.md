📘 Project Documentation
Introduction

This repository holds the documentation and setup for a containerized FastAPI application with MongoDB integration.
It includes:

Dockerfile → builds the application image

docker-compose.yaml → orchestrates the container setup

Both files are explained line by line, with short comments for clarity.

🚀 Dockerfile – Building Your Application Image

Think of the Dockerfile as a recipe that tells Docker how to build the image for your application.

Line-by-Line Breakdown

FROM python:3.12-slim

Base image with Python 3.12 in a lightweight environment.

Smaller than full Python image → saves space.

WORKDIR /app

Sets /app as the working directory inside the container.

Like cd /app but permanent for the container.

COPY requirements.txt .

Copies requirements.txt to /app/.

Copied first for layer caching optimization.

RUN pip install -r requirements.txt

Installs dependencies like FastAPI, Uvicorn, Motor, etc.

Executed at build time.

COPY app/ ./app/

Copies entire app folder into the container.

COPY .env .

Copies environment variables file into the container.

EXPOSE 8000

Documents that the app uses port 8000.

Note: Only documentation. Actual mapping happens in docker-compose.yaml.

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

Runs FastAPI with Uvicorn server when container starts.

📄 Updated Dockerfile with Comments

# Use lightweight Python 3.12 base image

FROM python:3.12-slim

# Set working directory inside container

WORKDIR /app

# Copy requirements first (better Docker layer caching)

COPY requirements.txt .

# Install Python dependencies

RUN pip install -r requirements.txt

# Copy application code

COPY app/ ./app/

# Copy environment variables file

COPY .env .

# Document that app uses port 8000

EXPOSE 8000

# Start FastAPI app with Uvicorn server

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

⚙️ docker-compose.yaml – Orchestrating Containers

Docker Compose manages multiple containers and their configurations.

Line-by-Line Breakdown

version: "3.8"

File format version, widely supported.

services:

Defines all containers to run.

video-manager:

Main service for the FastAPI app.

Name becomes the container name + network hostname.

build: .

Builds image from the Dockerfile in the current directory.

ports: - "8000:8000"

Maps host port 8000 → container port 8000.

Lets you access the app at <http://localhost:8000>.

environment: - MONGO_URI=${MONGO_URI}

Passes MongoDB connection string from .env.

volumes: - ./app:/app/app

Mounts local app folder inside the container.

Enables live reload during development.

📄 Updated docker-compose.yaml with Comments

# Docker Compose file format version

version: "3.8"

services:

# Main FastAPI application service

  video-manager:
    # Build image from Dockerfile in current directory
    build: .

    # Map host port 8000 to container port 8000
    ports:
      - "8000:8000"

    # Pass MongoDB Atlas connection string from .env
    environment:
      - MONGO_URI=${MONGO_URI}

    # Mount local app folder for live reload during development
    volumes:
      - ./app:/app/app

🔄 Why This Setup Works

Build → Docker creates an image with dependencies + app code.
Run → Compose starts the container.
Connect → Port mapping exposes the API at localhost:8000.
Database → App connects to MongoDB Atlas using .env.
Develop → Volume mount enables live code reload.

✅ Key Benefits

Isolation → Runs in its own environment

Consistency → Same setup across all machines

Portability → Works on Windows, Mac, Linux

Dev-Friendly → Live reload enabled

Simplicity → Just run docker-compose up

📦 This setup gives you a containerized FastAPI app connected to MongoDB Atlas with live reload support for development.
