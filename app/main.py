# API
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Logging / LifeSpan
from app.core.logging_config import setup_logging
from app.lifespan import lifespan

# Routers
from app.routes.produto_router import router as router_produtos
from app.routes.historico_router import router as router_historico
from app.routes.frontend_router import router as router_frontend
from app.routes.scrap_router import router as router_scrap

setup_logging()

app = FastAPI(
    title='Amazon Price Tracker - Ipad Monitor',
    version='1.0.0',
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router_produtos)
app.include_router(router_frontend)
app.include_router(router_historico)
app.include_router(router_scrap)