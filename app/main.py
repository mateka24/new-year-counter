from fastapi import FastAPI
from datetime import datetime
import math

app = FastAPI(title="New Year Counter API")

@app.get("/")
async def root():
    return {
        "message": "New Year Counter API",
        "usage": "GET /info - получить количество дней до Нового года"
    }

@app.get("/info")
async def get_days_before_new_year():
    # Получаем текущую дату и время
    now = datetime.now()
    
    # Определяем дату следующего Нового года
    next_year = now.year + 1
    new_year = datetime(next_year, 1, 1, 0, 0, 0)
    
    # Вычисляем разницу в днях
    delta = new_year - now
    days_before = math.ceil(delta.total_seconds() / (24 * 60 * 60))
    
    return {
        "days_before_new_year": days_before
    }