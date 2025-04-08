 
from fastapi import APIRouter
from app.services.oracle_erp import get_orders

order_router = APIRouter()

@order_router.get("/")
def fetch_orders():
    data = get_orders()
    return {"orders": data}
