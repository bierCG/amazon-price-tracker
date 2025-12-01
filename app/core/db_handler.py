from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

def db_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            logger.error(f"Erro no banco em {func.__name__}: {e}")
            return None
        except Exception as e:
            logger.exception(f"Erro inesperado em {func.__name__}: {e}")
    return wrapper