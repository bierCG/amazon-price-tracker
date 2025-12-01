# Amazon Price Tracker – iPad Monitor

Sistema para monitoramento automático de preços de iPads na Amazon, com scraping via Selenium, histórico de preços, detecção de mudança, e dashboard visual consumindo a API em tempo real.

# Visão Geral

O projeto realiza o scraping diário dos preços de iPads na Amazon, registra cada alteração no banco de dados PostgreSQL, e atualiza o cadastro do produto quando ocorre redução de valor.

Além disso, expõe uma API REST em FastAPI e um dashboard frontend HTML + JS + Chart.js, permitindo visualizar histórico de preços e acompanhar os produtos monitorados.

# Tecnologias Utilizadas

Python
FastAPI
Selenium WebDriver
APScheduler (agendador interno)
PostgreSQL
SQLAlchemy
Pydantic / Pydantic Settings
HTML / CSS / JS
Chart.js
RotatingFileHandler (logging profissional)
Arquivo .env para configuração

# Principais Funcionalidades

Web Scraping
- Coleta dos preços de iPads diretamente da Amazon usando Selenium.
- Tratamento automático de falhas e timeouts.
- Normalização dos dados recebidos.

Scheduler (APScheduler)
- Job agendado diariamente às 06:00.
- Tarefas não dependem do Windows Task Scheduler → multiplataforma.

Banco de Dados
- PostgreSQL
- SQLAlchemy (ORM + Models)
- Registro de histórico de preços
- Atualização automática do produto quando o preço muda

API REST
- CRUD completo de produtos
- Endpoint para histórico de preços
- Endpoint consumido pelo dashboard

Dashboard Frontend
- HTML + CSS + JS
- Chart.js para gráficos de histórico
- Consumo direto dos endpoints da API

Logging
- RotatingFileHandler gerando:
logs/app.log
logs/app.log.1
logs/app.log.2

Registro de:
- info (execução rotina)
- warning (condições inesperadas)
- error (falhas no Selenium ou banco)

Arquivo .env
- Variáveis sensíveis configuradas fora do código.

# Estrutura de Pastas
Amazon Price Tracker/
│── main.py
│── lifespan.py
│── .env
│── requirements.txt
│── Core/
│     ├── logging_config.py
│     └── settings.py
│
│── database/
│     ├── models/
│     |      ├── historico.py
|     |      └── produtos.py
│     ├── repositories/
|     |      ├── historico_repository.py
|     |      ├── produto_repository.py
|     |      └── scraping_repository.py
│     └── database.py
│
│── logs/
│     └── app.log
│
│── routes/
│     ├── produto_router.py
│     ├── historico_router.py
│     └── frontend_router.py
│
│── schemas/
│     └── produtos.py
│
│── services/
│     ├── produto_service.py
│     ├── historico_service.py
│     └── scraper_service.py
│
│── tasks/
│     ├── jobs.py
│     └── scheduler.py
│
│── static/
│     ├── dashboard.js
│     └── styles.css
│
│── templates/
│     └── dashboard.html
│
└── venv/

# Fluxo Geral do Sistema

- APScheduler dispara o job às 06:00.
- O scraper Selenium abre a página dos produtos na Amazon.
- Sistema coleta: nome, preço, ASIN
- O repositório verifica: se o preço mudou → salva histórico, atualiza cadastro do produto
- A API FastAPI expõe os dados.
- O dashboard consome a API e mostra gráficos em Chart.js.
- Logs são gerados e rotacionados automaticamente.

# Como Rodar o Projeto
1- Criar virtualenv
python -m venv venv

2 - Ativar

Windows: venv\Scripts\activate

3 - Instalar dependências
pip install -r requirements.txt

4 - Configurar o .env
Crie um arquivo .env com:

DATABASE_URL=postgresql://user:senha@localhost:5432/amz_tracker
EMAIL_HOST=smtp.gmail.com
EMAIL_USER=...
EMAIL_PASS=...
EMAIL_PORT=587
AMAZON_BASE_URL=https://www.amazon.com.br/dp/

5 - Iniciar API
uvicorn app.main:app --reload

Acesse:

http://localhost:8000/docs

6️ - Dashboard
http://localhost:8000/dashboard

# Endpoints Principais

Produtos
- GET/produtos/ -> Lista produtos monitorados
- PUT/produtos/{asin} -> Atualiza
- DELETE/produtos/{asin} -> Exclui produto

Histórico

- GET/historico/{asin} -> Histórico de produto espeçifico
- GET/historico/ -> Histórico de preços

Scrap
- POST/scrap/monitorar -> Executar manualmente scraping

Frontend

- GET/frontend/ -> Painel visual HTML/Chart.js

Autor

Gabriel Schlumberger