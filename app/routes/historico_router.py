from fastapi import APIRouter, Depends

from app.services.historico_service import HistoricoService
from app.database.repositories.historico_repository import HistoricoRepository

router = APIRouter(prefix='/historico', tags=['Historico'])

def get_service():
    repository = HistoricoRepository()
    return HistoricoService(repository)

@router.get('/')
def get_historico(
    service: HistoricoService = Depends(get_service)
):
    return service.get_historico()

@router.get('/{asin}') 
def get_historico_produto(
    asin: str,
    service: HistoricoService = Depends(get_service)
):
    return service.get_historico_produto(asin)