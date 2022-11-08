from fastapi import FastAPI
from app.router import get_data

app = FastAPI()

app.include_router(get_data.router)

@app.get('/')
async def root():
    return {"Massage" : "Welcome To API"}