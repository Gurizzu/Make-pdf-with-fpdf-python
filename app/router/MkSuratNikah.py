from fastapi import APIRouter, HTTPException, status
from .. import schema , database
from fpdf import FPDF
from .. import func


router = APIRouter(
    prefix="/SuratNikah",
    tags=["SuratNikah"]
)

# Surat Nikah EndPoint
@router.post("/")
async def make_surat_Nikah(makesurat:schema.SuratNikahForm):
    pdf = FPDF()
    payload = await database.make_Nikah(makesurat.dict())
    
    save_download_path = "download/"
    file_name = payload.get("_id")
    saved_file_name = save_download_path + "pdf_" + file_name

    footer_surat = {
        "penanda_tangan_surat" : payload.get("penanda_tangan_surat"),
        "nip_penandatangan_surat" : payload.get("nip_penandatangan_surat")
    }

    # await tm.run_nikah(data=payload, foot=footer_surat , output=saved_file_name)
    
    await func.set_nikah(fpdf=pdf , data=payload ,foot=footer_surat , output=saved_file_name)

    return {"massage" : "Thanks for Download"}