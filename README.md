# Project Overview
The **PROJECT** is a FastAPI-based application designed to evaluate a candidate's ability to validate data and implement cron jobs, as per the Backend Developer (Python FastAPI) assignment. It provides a **GET** endpoint to retrieve advertising metrics with flexible filtering and a **cron job** that logs timestamps every 6 hours. The project uses **SQLite** as the database and follows a **Django-like structure**.

## Features
- **FastAPI Service:** A `GET /api/v1/ad-metrics/` endpoint with Pydantic-validated query parameters.
- **Database:** SQLite with SQLAlchemy models for ad metrics and dimension tables.
- **Cron Job:** Asynchronous logging every 6 hours using APScheduler.
- **Utilities:** Reusable database functions in `core/db_utils.py`.

## Project Structure
```
FAST_API_PROJECT/
├── apps/
│   ├── api/              # API endpoints, routes, and schemas
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   │   ├── urls.py
│   │   └── schemas.py
│   ├── cron/             # Cron job implementation
│   │   ├── __init__.py
│   │   └── tasks.py
├── core/                 # Database models and utilities
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── db_utils.py
├── insert_100_test_data.py  # Script to populate test data
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Setup Instructions

### Prerequisites
- **Operating System:** Linux (e.g., Ubuntu), macOS, or Windows (WSL recommended).
- **Python:** Version **3.12** or higher (`python3 --version`).
- **pip:** Python package manager (included with Python).
- **Git:** Optional, for cloning the repository if hosted.

### 1. Clone or Download the Project
If the project is hosted on a Git repository:
```sh
git clone <repository-url>
cd FAST_API_PROJECT
```
Alternatively, download and extract the project files manually, then navigate to the root directory:
```sh
cd FAST_API_PROJECT
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate dependencies:
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
You’ll see `(venv)` in your terminal prompt when activated.

### 3. Install Dependencies
The project dependencies are listed in `requirements.txt`:
```
fastapi==0.110.0
uvicorn==0.29.0
sqlalchemy==2.0.28
pydantic==2.6.4
apscheduler==3.10.4
```
Install them with:
```sh
pip install -r requirements.txt
```

### 4. Initialize the Database
Run the provided script to create the SQLite database (`ad_metrics.db`) and populate it with 100 rows of test data:
```sh
python insert_100_test_data.py
```
**Expected Output:** "Successfully inserted 100 rows of test data".

**Note:** This creates tables and inserts data for dates (March 1 to June 9, 2025) and ad metrics.

### 5. Run the Application
Start the FastAPI server:
```sh
python main.py
```
The server will run on `http://localhost:8000`.
A cron job will log timestamps to `cron.log` every **6 hours**.

### 6. Verify the Setup
- **API Documentation:** Open [`http://localhost:8000/docs`](http://localhost:8000/docs) in a browser to access the Swagger UI.
- **Test the Endpoint:**
```sh
curl -X GET "http://localhost:8000/api/v1/ad-metrics/?start_date=2025-03-01&end_date=2025-03"
