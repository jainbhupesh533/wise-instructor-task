# Note-Taking Application API

This README provides instructions for interacting with the Note-Taking Application API. The API allows users to perform basic CRUD operations on notes.
## Prerequisites

Before you begin, ensure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Running the Project

1. Clone the repository:

    ```bash
    git clone https://github.com/jainbhupesh533/
    cd your-project
    ```
   
3. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

4. Once the containers are up and running, the Django application should be accessible at `http://127.0.0.1:8000/`.

5. At the time of intialization, it ll automatically test the django application

## API Endpoints
# Institute Backend System

This backend system allows institutes to track their instructors' check-in & out times throughout the day and view their total working hours on a monthly basis. It provides APIs to store this information into the database and retrieve aggregated monthly reports.

## API Endpoints

#### Create Instructor

- **Endpoint**: `/instructors/create`
- **Method**: POST
- **Description**: Creates a new instructor.
- **Parameters**:
  - `username`: Instructor's username
  - `email`: Instructor's email address
  - `password`: Instructor's password

#### Check-In

- **Endpoint**: `/instructors/login`
- **Method**: POST
- **Description**: For getting the auth token.
- **Parameters**:
  - `username`: instructor username
  - `password`: istructor password
  - 

#### Check-In

- **Endpoint**: `/instructors/checkin`
- **Method**: POST
- **Description**: Records instructor's check-in time.
- **Parameters**:
  - `instructor_id`: ID of the instructor checking in
  - `check_time`: Check-in time (format: "YYYY-MM-DD HH:MM:SS")

#### Check-Out

- **Endpoint**: `/instructors/checkout`
- **Method**: POST
- **Description**: Records instructor's check-out time.
- **Parameters**:
  - `instructor_id`: ID of the instructor checking out
  - `check_time`: Check-out time (format: "YYYY-MM-DD HH:MM:SS")

### Reports

#### Monthly Report

- **Endpoint**: `/instructors/monthly-report`
- **Method**: GET
- **Description**: Computes instructor-wise total checked-in time for all instructors in the given month.
- **Parameters**:
  - `month`: Month (numeric value)
  - `year`: Year (numeric value)