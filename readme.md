# IoT Backend with Real-time Data Streaming

This project implements a Flask-based IoT backend system with a MySQL database, user authentication using JWT. The backend is designed to handle sensor registration, data submission, and retrieval, and provides real-time updates to connected clients.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and login with JWT authentication
- Sensor registration, data submission, and retrieval
- MySQL database for storing user and sensor data
- API endpoints for interacting with sensors and retrieving data

## Prerequisites

- Python 3.x
- Flask
- MySQL database


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/2bdulra7manRea/iot-backend.git
   cd iot-backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database settings in `config.py`.

4. Run the application:

   ```bash
   python app.py
   ```

## Usage

- Visit `http://localhost:5000` in your browser to access the application.


## Endpoints

- **User Management:**
  - `POST /register` - Register a new user.
  - `POST /login` - Log in and receive JWT token.

- **Sensor Management:**
  - `POST /sensor/register` - Register a new sensor.
  - `GET /sensor/all` - Get details of all registered sensors.

- **Data Submission and Retrieval:**
  - `POST /sensor/submit` - Submit sensor data.
  - `GET /sensor/:id` - Retrieve historical sensor data.

- **Real-time Data Streaming:**
  - Real-time updates are pushed to connected clients using Flask-SocketIO.

## Authentication

- JWT authentication is required for user data and sensor registration.
- Include the JWT token in the `Authorization` header for authenticated requests.

## Testing

- Unit tests can be run using:

  ```bash
  python -m unittest discover
  ```

## Deployment

- Ensure your deployment environment supports WebSocket connections for Flask-SocketIO.

## Contributing

Feel free to contribute to this project. Create a fork, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
