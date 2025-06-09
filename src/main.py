from fastapi import FastAPI, Request
import httpx
import logging
import os

# Configurar logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# URLs de microservicios (por defecto, apuntan a nombres de servicio docker)
TASK_SERVICE_URL = os.getenv("TASK_SERVICE_URL", "http://task-service:8002")
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:8003")
DONATION_SERVICE_URL = os.getenv("DONATION_SERVICE_URL", "http://donation-service:8001")
NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8004")

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
    return response.json()

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    logger.info(f"GET /user/{user_id} called")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/user/{user_id}")
    return response.json()

@app.post("/donation/create")
async def create_donation(request: Request):
    logger.info("POST /donation/create called")
    body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{DONATION_SERVICE_URL}/donation/create", json=body)
    return response.json()

@app.post("/notify")
async def send_notification(request: Request):
    logger.info("POST /notify called")
    body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{NOTIFICATION_SERVICE_URL}/notify", json=body)
    return response.json()


