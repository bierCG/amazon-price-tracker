from app.database.repositories.produto_repository import ProdutoRepository
from app.database.repositories.historico_repository import HistoricoRepository

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

keywords = ["ipad", "apple", "a16"]
block = ["capa", "case", "película", "bolsa", "caneta", "keyboard", "folio"]

class ScrapService():
    def __init__(
            self, 
            repository_produto: ProdutoRepository,
            repository_historico: HistoricoRepository
        ):
        self.repo_produto = repository_produto
        self.repo_historico = repository_historico
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)

    def start_process(self):
        try:
            produtos = self.get_dados_amazon()
            
            produtos_filtrados = self.filtra_precos(produtos)
            if produtos_filtrados:
                self.repo_produto.registrar_produtos(produtos_filtrados)
        finally:
            self.driver.quit()

    def filtra_precos(self, produtos: list[dict]) -> list[dict]:
        """
        Recebe uma lista de produtos e:
        - Atualiza o preço no banco quando houver alteração.
        - Retorna somente os produtos que ainda não estão cadastrados (novos).

        Parameters:
            produtos (list[dict]): Lista de produtos retornados pelo scraping,
            onde cada item representa um produto com suas informações.

        Returns:
            list[dict]: Lista contendo apenas produtos novos que ainda
            não existem no banco.
        """
        
        produtos_novos = []
        asin_existentes  = self.repo_produto.get_codigos_asin()

        for produto in produtos:
            asin = produto['codigo_asin']
            preco = produto['preco']

            if asin not in asin_existentes:
                produtos_novos.append(produto)
                continue
            
            preco_atual = self.repo_produto.get_preco_produto(produto['codigo_asin'])
            
            if preco != preco_atual:
                
                self.repo_produto.atualiza_preco(asin, preco)
                self.repo_historico.registra_mudanca_historico(
                    codigo_asin=asin,
                    preco=preco,
                    data=datetime.now()
                )

        self.converter_preco()
        return produtos_novos

    def converter_preco(self):
        """
        Extrai o preço exibido no formato da Amazon (parte inteira e decimal)
        e converte para float.

        Returns:
            float: valor do preço, por exemplo 1234.56

        Observações:
            - Remove pontos da parte inteira (ex: "1.234" → "1234")
            - Junta parte inteira e decimal em uma string antes de converter
            - Pode levantar exceções se os elementos não forem encontrados
        """
         
        inteiro = self.driver.find_element(By.CLASS_NAME, "a-price-whole").text.replace(".", "")
        decimal = self.driver.find_element(By.CLASS_NAME, "a-price-fraction").text
        return float(f'{inteiro}.{decimal}')

    def pegar_titulo(self, item):
        seletores = [
            "h2 a span",
            "h2 span",
            "a.a-link-normal span",
            "span.a-size-medium.a-color-base.a-text-normal",
            "span.a-size-base-plus.a-color-base.a-text-normal",
        ]

        for sel in seletores:
            try: return item.find_element(By.CSS_SELECTOR, sel).text.lower()
            except: pass

        return None

    def get_codigo_asin_produtos(self, produto):
        self.driver.get('https://amazon.com.br')
        
        input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox'))
        )
        input.send_keys(produto, Keys.ENTER)
        
        itens_pesquisa = self.wait.until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR,'div.s-result-item.s-asin')
            )
        )

        codigos = []

        for item in itens_pesquisa:
            titulo = self.pegar_titulo(item)

            if not titulo: continue # Alguns cards podem não ter produto

            if all(k in titulo for k in keywords) and not any(b in titulo for b in block):
                asin = item.get_attribute("data-asin")
                if not asin: continue
                codigos.append(asin)

        return list(set(codigos))
    
    def get_dados_pagina_produto(self, asin):
        self.driver.get(f'https://www.amazon.com.br/dp/{asin}')

        nome = self.driver.find_element(By.ID, 'productTitle').text
        preco = self.converter_preco()
        link = self.driver.current_url
        #imagem = self.driver.find_elements(By.NAME, 'landingImage').get_attribute('href')
        imagem = 'teste'

        produto = {
            'codigo_asin': asin,
            'nome': nome,
            'preco': preco,
            'link': link,
            'imagem': imagem
        }

        return produto

    def get_dados_amazon(self):
        asins = self.get_codigo_asin_produtos('Ipad A16')
        return [self.get_dados_pagina_produto(codigo) for codigo in asins]