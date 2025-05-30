from fastapi import FastAPI, Request
import httpx
import logging
import os

# Configurar logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Obtener URLs desde variables de entorno (con valores por defecto)
TASK_SERVICE_URL = os.getenv("TASK_SERVICE_URL", "http://task-service:8000")
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:8001")

@app.get("/health")
def health():
    logger.info("GET /health called")
    return {"status": "ok"}

@app.get("/ready")
def ready():
    logger.info("GET /ready called")
    return {"status": "ready"}

@app.post("/task/create")
async def create_task(request: Request):
    logger.info("POST /task/create called")
    body = await request.json()
    logger.info(f"Forwarding to {TASK_SERVICE_URL}/task/create with body: {body}")
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{TASK_SERVICE_URL}/task/create", json=body)
    logger.info(f"Response from task service: {response.status_code}")
    return response.json()

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    logger.info(f"GET /user/{user_id} called")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/user/{user_id}")
    logger.info(f"Response from user service: {response.status_code}")
    return response.json()


