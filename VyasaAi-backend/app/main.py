 
from fastapi import FastAPI
from app.routes.order_routes import order_router

app = FastAPI(title="VyasaAi-backend")

app.include_router(order_router, prefix="/api/orders")
