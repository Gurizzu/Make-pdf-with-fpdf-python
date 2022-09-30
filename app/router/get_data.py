from fastapi import APIRouter, HTTPException, status
from .. import schema , database
from fpdf import FPDF
from utils import func
from .. import database
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/api",
    tags=["get data"]
)

@router.get("/v1/generate/{form}/{id}")
async def all_surat(form:str, id:str):
    pdf = FPDF()
    data = await database.find_one(form,id)
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    id = data.get('_id')
    data["_id"] = str(id)
    
    
    payload = data
    
    save_download_path = f"download/{form}/"
    file_name = payload.get("_id")
    saved_file_name = save_download_path + "pdf_" + file_name
    footer_surat = {
        "penanda_tangan_surat" : payload.get("penanda_tangan_surat"),
        "nip_penandatangan_surat" : payload.get("nip_penandatangan_surat")
    }
    
    
    await func.run_surat(data=payload, foot=footer_surat , output=saved_file_name ,pdf=pdf, form=form)
    return FileResponse(f"{saved_file_name}.pdf")
    