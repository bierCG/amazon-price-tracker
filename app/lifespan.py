import logging

from fastapi import FastAPI
from app.tasks.scheduler import start_scheduler
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()

    yield

    logger.info("Encerrando app...")