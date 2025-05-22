# Dummy Model FastAPI Service

This project deploys a dummy model using FastAPI.

## Features
- `/predict` endpoint to return class based on feature input.
- Input validation using Pydantic.
- Dockerfile included.

## Setup Instructions

### Run Locally

1. Clone the repo and navigate to the folder:
```bash
git clone <repo-url>
cd Dummy_Model_API
```

2. Create a virtual environment and install requirements:
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the API:
```bash
uvicorn app.main:app --reload
```

4. Test with:
```json
POST http://127.0.0.1:8000/predict
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

### Run with Docker

1. Build Docker image:
```bash
docker build -t dummy-model-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 dummy-model-api
```

### API Docs
Visit Swagger UI at: `http://127.0.0.1:8000/docs`
