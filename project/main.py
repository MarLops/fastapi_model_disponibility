import configparser
import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.service.logging_service import LogIPMiddleware
from src.controllers.model_consume import app_model_consume

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser(os.environ)
config.read("settings.ini")

app = FastAPI(title='Model Consume',
              version='1.0.0',
              description="""
                API to consume
                """)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LogIPMiddleware)


@app.get("/health",description="Check if it is on")
def health_check():
    return {"status": "OK"}


app.include_router(app_model_consume,prefix='/model')





