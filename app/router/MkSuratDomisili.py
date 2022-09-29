from fastapi import APIRouter, HTTPException, status
from .. import schema , database


router = APIRouter(
    prefix="/SuratDomisili",
    tags=["SuratDomisili"]
)

@router.post("/")
async def make_surat_domisili(makesurat:schema.SuratDomisiliForm):
    return await database.make_domisisli(makesurat.dict())
