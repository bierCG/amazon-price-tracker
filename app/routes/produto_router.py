from fastapi import APIRouter, Depends

from app.schemas.produtos import GetProdutosResponde
from app.database.repositories.produto_repository import ProdutoRepository
from app.services.produto_service import ProdutoService

router = APIRouter(prefix='/produtos', tags=['Produtos'])

def get_service() -> ProdutoService:
    repo = ProdutoRepository()
    return ProdutoService(repo)

@router.get('/', response_model=list[GetProdutosResponde])
def get_produtos(
    service: ProdutoService = Depends(get_service)
):
    return service.get_produtos()

@router.get('/nome/{produto}')
def get_produtos_parcial(
    produto: str,
    service: ProdutoService = Depends(get_service)
):
    return service.get_produtos_parcial(produto)

@router.get('/asin/{asin}')
def get_produto(
    asin: str,
    service: ProdutoService = Depends(get_service)
):
    return service.get_produto_asin(asin)
    
@router.delete('/{asin}')
def excluir_produto(
    asin: str,
    service: ProdutoService = Depends(get_service)
):
    return service.excluir_produto(asin)