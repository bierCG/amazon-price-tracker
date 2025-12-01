from fastapi import APIRouter, Depends

from app.database.repositories.produto_repository import ProdutoRepository
from app.database.repositories.historico_repository import HistoricoRepository
from app.services.scraper_service import ScrapService

router = APIRouter(prefix='/scrap')

def get_service():
    repository_produto = ProdutoRepository()
    repository_historico = HistoricoRepository()
    return ScrapService(repository_produto, repository_historico)

@router.post('/monitorar')
def executar_scraping(
    service: ScrapService = Depends(get_service)
):
    return service.start_process()