from sqlalchemy import Column, String, Integer, Float, DateTime

from app.database.database import Base

class HistoricoProduto(Base):
    __tablename__ = 'historico_produtos'
    id = Column(Integer, primary_key=True)
    preco = Column(Float)
    data = Column(DateTime)
    codigo_asin = Column(String)