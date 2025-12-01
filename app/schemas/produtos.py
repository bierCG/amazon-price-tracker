from pydantic import BaseModel, ConfigDict

class GetProdutosResponde(BaseModel):
    id:int
    codigo_asin:str
    nome:str
    preco:float
    link:str
    imagem:str

    model_config = ConfigDict(from_attributes=True)