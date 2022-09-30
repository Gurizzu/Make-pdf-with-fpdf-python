from fastapi import FastAPI
from app.router import MkSuratDomisili , MkSuratKematian , MkSuratNikah, get_data

app = FastAPI()

app.include_router(MkSuratDomisili.router)
app.include_router(MkSuratKematian.router)
app.include_router(MkSuratNikah.router)
app.include_router(get_data.router)

@app.get('/')
async def root():
    return {"Massage" : "Welcome To API"}