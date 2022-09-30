from fastapi import APIRouter, HTTPException, status
from .. import schema , database
from fpdf import FPDF
from utils import func

router = APIRouter(
    prefix="/SuratKematian",
    tags=["SuratKematian"]
)

@router.post("/")
async def make_surat_kematian(makesurat:schema.SuratKematianForm):
    try:
        pdf = FPDF()
        payload = await database.make_kematian(makesurat.dict())
        
        save_download_path = "download/surat_kematian/"
        file_name = payload.get("_id")
        saved_file_name = save_download_path + "pdf_" + file_name

        footer_surat = {
            "penanda_tangan_surat" : payload.get("penanda_tangan_surat"),
            "nip_penandatangan_surat" : payload.get("nip_penandatangan_surat")
        }
    except:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="Not connected")
    
    await func.run_kematian(pdf=pdf , data=payload ,foot=footer_surat , output=saved_file_name)
    return {"Massage" : "Thanks For Download"}