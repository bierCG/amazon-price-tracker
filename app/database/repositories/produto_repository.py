from app.core.db_handler import db_handler
from app.database.database import Session
from app.database.models.produtos import Produto

class ProdutoRepository():
    def __init__(self):
        pass

    @db_handler
    def get_produtos(self):
        with Session() as session: return session.query(Produto).all()

    def get_produtos_parcial(self,valor):
        with Session() as session: return session.query(Produto).filter(Produto.nome.ilike(f'%{valor}%')).all()

    @db_handler
    def get_produto_asin(self,asin):
        with Session() as session:
            return session.query(Produto).filter(Produto.codigo_asin == asin).first()

    @db_handler
    def get_preco_produto(self,asin):
        with Session() as session:
            return session.query(Produto.preco).filter(Produto.codigo_asin == asin).scalar()

    @db_handler
    def get_codigos_asin(self):
        with Session() as session:
            rows = session.query(Produto.codigo_asin).all()
            asins = [asin for (asin,) in rows]
            return asins

    @db_handler
    def registrar_produtos(self,produtos):
        with Session() as session:
            for produto in produtos:
                novo_produto = Produto(
                    codigo_asin=produto['codigo_asin'],
                    nome=produto['nome'],
                    preco=produto['preco'],
                    link=produto['link'],
                    imagem=produto['imagem']
                )
                session.add(novo_produto)
                
            session.commit()

    @db_handler
    def atualiza_preco(self,codigo_asin, preco):
        with Session() as session:
            session.query(Produto).filter(Produto.codigo_asin == codigo_asin).update({Produto.preco:preco})
            session.commit()

    @db_handler
    def excluir_produto(self,asin):
        with Session() as session:
            session.query(Produto).filter(Produto.codigo_asin == asin).delete()