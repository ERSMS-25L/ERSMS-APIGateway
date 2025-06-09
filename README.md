# API Gateway - ERSMS

This is the API Gateway for the ERSMS Task Management System.

---

##  How to Run

###  With Docker

```bash
docker build -t api-gateway .
docker run -p 8080:8080 ^
  -e TASK_SERVICE_URL=http://localhost:8002 ^
  -e USER_SERVICE_URL=http://localhost:8003 ^
  api-gateway
```

> On Linux/Mac, use `\` instead of `^`.

### 🖥️ Locally with Uvicorn (optional)

```bash
TASK_SERVICE_URL=http://localhost:8002 \
USER_SERVICE_URL=http://localhost:8003 \
uvicorn src.main:app --reload --port 8000
```

---

##  Environment Variables

You can configure service URLs using environment variables:

- `TASK_SERVICE_URL` → default: `http://task-service:8000`
- `USER_SERVICE_URL` → default: `http://user-service:8001`

---

##  Endpoints

- `GET /health` → returns `{ "status": "ok" }`
- `GET /ready` → returns `{ "status": "ready" }`
- `POST /task/create` → forwards to the task service
- `GET /user/{user_id}` → forwards to the user service

---

##  API Contract

### `GET /health`
Returns basic health status.

### `GET /ready`
Returns readiness status.

### `POST /task/create`
Forwards body to:
- `http://task-service:8000/task/create`

### `GET /user/{user_id}`
Forwards request to:
- `http://user-service:8001/user/{user_id}`

---

##  Requirements

See [`requirements.txt`](./requirements.txt) for Python dependencies.

---

##  How to Test

Install `pytest` (if needed):

```bash
pip install pytest
```

Then run:

```bash
pytest tests/
```

> (Make sure you are in the root folder of the project when running tests)

---
