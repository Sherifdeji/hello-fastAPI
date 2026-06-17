# Hello FastAPI

An API built with [FastAPI](https://fastapi.tiangolo.com/) to demonstrate core concepts such as basic routing, path parameters, query parameters, and returning JSON responses.

## Features & Endpoints

- **`GET /`** - Returns a simple welcome message.
- **`GET /greet/{name}`** - Demonstrates path parameters by returning a personalized greeting.
- **`GET /time`** - Integrates Python's native `datetime` module to return the server's current time.
- **`GET /quote`** - Returns a random quote from a hardcoded list.
- **`GET /quote?index={number}`** - Demonstrates optional query parameters by returning a specific quote if a valid index is provided, or gracefully handling out-of-bounds requests.

## Getting Started

### Prerequisites

- Python 3.10+
- `pip` package manager

### Installation

1. Clone or download the repository.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the local development server with live-reloading:

```bash
uvicorn main:app --reload
```

The API will be accessible at: `http://127.0.0.1:8000`

### Interactive API Documentation

FastAPI automatically generates interactive API documentation. While the server is running, you can explore and test the endpoints directly from your browser:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
