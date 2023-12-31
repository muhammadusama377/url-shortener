# URL Shortener App

## Description

The URL Shortener App is a Python-based web application built with FastAPI. It allows users to shorten long URLs into easily shareable and memorable short links. The app supports OpenAPI documentation, and it can be easily deployed using Docker.

## Features

- Shorten long URLs into short links.
- Retrieve original URLs by using short links.
- OpenAPI documentation for easy API exploration.
- Docker support for seamless deployment.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/muhammadusama377/url-shortener.git
    ```

2. Navigate to the project directory:

    ```bash
    cd url-shortener
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Run Migrations:

    ```bash
   alembic upgrade head
    ```

## Usage

1. Run the FastAPI development server:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the application at [http://localhost:8000](http://localhost:8000) in your browser.

3. Use the OpenAPI documentation at [http://localhost:8000/docs](http://localhost:8000/docs) to explore the API and interact with endpoints.

## API Documentation

The OpenAPI documentation provides details about the available endpoints, request/response formats, and example usage. Access the documentation at [http://localhost:8000/docs](http://localhost:8000/docs) when the app is running.

## Docker Deployment

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Run the Docker container:

    ```bash
    docker-compose up
    ```

3. Access the application at [http://localhost:8000](http://localhost:8000) in your browser.

## Contributing

Contributions are welcome! Please follow our [contribution guidelines](CONTRIBUTING.md) to contribute to the project.

## License
