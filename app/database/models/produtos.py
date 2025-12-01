from sqlalchemy import Column, String, Integer, Float, DateTime

from app.database.database import Base

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    codigo_asin = Column(String)
    nome = Column(String)
    preco = Column(Float)
    link = Column(String)
    imagem = Column(String)