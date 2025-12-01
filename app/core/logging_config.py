import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    os.makedirs('logs', exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=1_000_000,
        backupCount=5,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)