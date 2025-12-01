from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL
from app.core.settings import settings

Base = declarative_base()

def Session():
    url = URL.create(
        settings.DRIVER_NAME,
        settings.USER_NAME,
        settings.PASSWORD,
        settings.HOST,
        settings.PORT,
        settings.DATABASE
    )
    engine = create_engine(url, future=True)
    session = sessionmaker(bind=engine)
    return session()