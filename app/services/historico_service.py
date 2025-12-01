import logging

from app.database.repositories.historico_repository import HistoricoRepository

logger = logging.getLogger(__name__)

class HistoricoService():
    def __init__(self, repository:HistoricoRepository):
        self.repo = repository

    def get_historico(self):
        """
        Retorna o histórico completo de alterações registradas.

        Returns:
            list[Historico]: Lista contendo todos os registros de histórico.
        """
        logger.info("Buscando histórico completo.")
        return self.repo.get_historico()

    def get_historico_produto(self, asin):
        """
        Retorna o histórico de alterações de um produto específico.

        Args:
            asin (str): Código ASIN do produto.

        Returns:
            list[Historico]: Lista de alterações registradas para o produto informado.
        """
        logger.info(f"Buscando histórico do produto ASIN={asin}.")
        return self.repo.get_historico_produto(asin)