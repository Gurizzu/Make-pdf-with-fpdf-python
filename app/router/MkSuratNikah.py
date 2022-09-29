from fastapi import APIRouter, HTTPException, status
from .. import schema , database


router = APIRouter(
    prefix="/SuratNikah",
    tags=["SuratNikah"]
)

@router.post("/")
async def make_surat_Nikah(makesurat:schema.SuratNikahForm):
    return await database.make_Nikah(makesurat.dict())