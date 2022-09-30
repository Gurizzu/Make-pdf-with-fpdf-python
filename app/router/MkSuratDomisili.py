from fastapi import APIRouter, HTTPException, status
from .. import schema , database
from fpdf import FPDF
from utils import func
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/SuratDomisili",
    tags=["SuratDomisili"]
)

@router.post("/")
async def make_surat_domisili(makesurat:schema.SuratDomisiliForm):

    try:
        pdf = FPDF()
        payload = await database.make_domisisli(makesurat.dict())
        
        save_download_path = "download/surat_domisili/"
        file_name = payload.get("_id")
        saved_file_name = save_download_path + "pdf_" + file_name

        footer_surat = {
            "penanda_tangan_surat" : payload.get("penanda_tangan_surat"),
            "nip_penandatangan_surat" : payload.get("nip_penandatangan_surat")
        }
        
        await func.run_domisili(data=payload, foot=footer_surat , output=saved_file_name ,pdf=pdf)
        # return FileResponse(path=f"{saved_file_name}.pdf",filename=f"{saved_file_name}.pdf")
    
    except:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="Not connected")
