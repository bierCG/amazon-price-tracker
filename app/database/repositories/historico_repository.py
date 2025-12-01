from app.database.database import Session
from app.database.models.historico import HistoricoProduto

class HistoricoRepository:
    def __init__(self):
        pass

    def get_historico(self):
        with Session() as session:
            return session.query(HistoricoProduto).all()

    def get_historico_produto(self, asin):
        with Session() as session:
            return session.query(HistoricoProduto).filter(HistoricoProduto.codigo_asin == asin).all()
        
    def registra_mudanca_historico(self, codigo_asin, preco, data):
        with Session() as session:
            mudanca = HistoricoProduto(
                codigo_asin=codigo_asin,
                preco=preco,
                data=data
            )
            session.add(mudanca)
            session.commit()