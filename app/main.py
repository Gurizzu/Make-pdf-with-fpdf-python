from fastapi import FastAPI
from app.router import MkSuratDomisili , MkSuratKematian , MkSuratNikah

app = FastAPI()

app.include_router(MkSuratDomisili.router)
app.include_router(MkSuratKematian.router)
app.include_router(MkSuratNikah.router)
@app.get('/')
async def root():
    return {"Massage" : "Welcome To API"}