import os

APP_NAME = os.getenv("APP_NAME", "Agentic SDC Project 2 API")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
