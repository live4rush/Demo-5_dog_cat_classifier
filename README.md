# Dog Cat Classifier

This is a Dog Cat Classifier that uses image classification to distinguish between images of dogs and cats.

## Getting Started

### Prerequisites

Before you begin, make sure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and [Docker](https://docs.docker.com/get-docker/) installed on your machine.

### Setting up a Virtual Environment

1. Create a virtual environment using conda:

    ```bash
    conda create -p ./env python=3.9.18
    ```

2. Activate the virtual environment:

    ```bash
    conda activate ./env
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Optional - Run the model and recreate model_new.h5
    ```bash
    python model_train.py
    ```
5. Optional - Run the model predict and make sure it works
    ```bash
    python predict.py
    ```
6. Run the flask server locally 
    ```bash
    export FLASK_APP=clientApp_Flask
    export FLASK_ENV=development
    flask run --host=0.0.0.0 --port=9000
    ```
7. Install required packages for fastapi conversion
    ```bash
    pip install fastapi uvicorn python-multipart
    ```
8. Create a new file clientApp_FastAPI.py for fastapi (refer to the file for code)
9. Run fastapi server locally
    ```bash
    uvicorn clientApp_FastAPI:app --reload --host 0.0.0.0 --port 9000
    ```

## Containerization with Docker

### Building the Docker Image for Flask App

To containerize the Dog Cat Classifier using Docker, follow these steps:

1. Create a Dockerfile name Dockerfile_Flask in the root of your project with the following content:

    ```dockerfile
    FROM python:3.9.18
    COPY . /app
    WORKDIR /app
    RUN pip3 install -r requirements.txt
    EXPOSE $PORT
    CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT clientApp:app
    ```

2. Build the Docker image using the following command (replace `<image_name>` with your desired image name):

    ```bash
    docker build -f filename -t <image_name> .
    ```
    ```
    for example: docker build -f Dockerfile_Flask -t dog-cat-classifier-flask .
    ```
3. Run the Docker container:

    ```bash
    docker run -p 9000:9000 -e PORT=9000 <image_name>
    ```
    ```
    for example: docker run -p 9000:9000 -e PORT=9000 dog-cat-classifier-flask
    ```


### Building the Docker Image for FastAPI App

To containerize the Dog Cat Classifier using Docker, follow these steps:

1. Create a Dockerfile name Dockerfile_FastAPI in the root of your project with the following content:

    ```dockerfile
    FROM python:3.9.18
    COPY . /app
    WORKDIR /app
    RUN pip3 install -r requirements.txt
    EXPOSE $PORT
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT", "--workers", "4"]
    ```

2. Build the Docker image using the following command (replace `<image_name>` with your desired image name):

    ```bash
    docker build -f filename -t <image_name> .
    ```
    ```
    for example: docker build -f Dockerfile_FastAPI -t dog-cat-classifier-fastapi .
    ```
3. Run the Docker container:

    ```bash
    docker run -p 9000:9000 -e PORT=9000 <image_name>
    ```
    ```
    for example: docker run -p 9000:9000 -e PORT=9000 dog-cat-classifier-fastapi
    ```

Now, your Dog Cat Classifier is running inside a Docker container.

Feel free to explore and enhance the classifier as needed. Happy classifying! 🐶🐱
