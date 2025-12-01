from fastapi import HTTPException
import logging

from app.database.repositories.produto_repository import ProdutoRepository
from app.services.scraper_service import ScrapService

logger = logging.getLogger(__name__)

class ProdutoService():
    def __init__(self, repository:ProdutoRepository):
        """
        Inicializa o serviço de produtos.

        Args:
            repository (ProdutoRepository): Instância do repositório de produtos.
        """
        self.repo = repository
        
    def get_produtos(self):
        """
        Retorna todos os produtos cadastrados.

        Returns:
            list[Produto]: Lista completa de produtos.
        """
        return self.repo.get_produtos()
    
    def get_produtos_parcial(self, produto: str):
        """
        Retorna produtos filtrados parcialmente pelo nome.

        Args:
            produto (str): Termo de busca parcial.

        Returns:
            list[Produto]: Produtos cujo nome contém o termo informado.
        """
        return self.repo.get_produtos_parcial(produto)
    
    def get_produto_asin(self, asin: str):
        """
        Busca um produto específico utilizando o ASIN da Amazon.

        Args:
            asin (str): Código ASIN do produto.

        Returns:
            Produto | None: O produto correspondente, ou None se não encontrado.
        """
        return self.repo.get_produto_asin(asin)
    
    def excluir_produto(self, asin: str):
        """
        Exclui um produto com base no seu ASIN.

        Args:
            asin (str): Código ASIN do produto a ser removido.

        Returns:
            bool: True se a exclusão ocorreu, False caso contrário.
        """
        return self.repo.excluir_produto(asin)