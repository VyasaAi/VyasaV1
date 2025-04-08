from fastapi import APIRouter
from app.db import get_db_connection

router = APIRouter()

@router.get("/test-db")
def test_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from Oracle DB!' FROM dual")
    result = cursor.fetchone()
    return {"message": result[0]}
