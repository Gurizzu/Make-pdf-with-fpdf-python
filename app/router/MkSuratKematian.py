from fastapi import APIRouter, HTTPException, status
from .. import schema , database


router = APIRouter(
    prefix="/SuratKematian",
    tags=["SuratKematian"]
)

@router.post("/")
async def make_surat_kematian(makesurat:schema.SuratKematianForm):
    return await database.make_kematian(makesurat.dict())