import logging
from logging.config import dictConfig

from dotenv import load_dotenv
from fastapi import FastAPI

from app.core.config import LOGGING_CONFIG

load_dotenv()

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}
