import logging
import app.services.produto_service as services

logger = logging.getLogger(__name__)

def execute_scraping():
    try:
        services.executar_scraping()
        logger.info('Scraping concluído com sucesso')
    except Exception as e:
        logger.error("Erro crítico durante o scraping", exc_info=True)