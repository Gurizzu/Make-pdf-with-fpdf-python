import json
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Body
from .. import schema , database
from fpdf import FPDF
from utils import func
from .. import database
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/api",
    tags=["Generete Data"]
)

@router.get("/v1/generate/{form}/{id}")
async def all_surat(form:str, id:str):
    form = form.lower()
    pdf = FPDF()
    data = await database.find_one(form,id)
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    id = data.get('_id')
    data["_id"] = str(id)
    
    nama_pembuat = data.get("nama_pembuat")
    tanggal = data.get("tanggal_print")
    nama_surat = data.get("nama_surat")
    
    
    payload = data
    
    save_download_path = f"download/{form}/"
    file_name = payload.get("_id")
    saved_file_name = save_download_path + "pdf_" + file_name
    response_name = f"{nama_surat}_{nama_pembuat}_{tanggal}"
    footer_surat = await database.get_footer_by_form(form=form)

    if not footer_surat:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cant print")

    footer_surat = {
       "id_tanda_tangan" : footer_surat.get("id_tanda_tangan")[0],
       "createdAt" : footer_surat.get("createdAt"),
       "updatedAt": footer_surat.get("updatedAt")
    }

    await func.run_surat(data=payload, foot=footer_surat , output=saved_file_name ,pdf=pdf, form=form)
    return FileResponse(path=f"{saved_file_name}.pdf", filename=f"{response_name}.pdf")
    # return {"Massage" : "Susses"}
    
    
@router.post("/v2/generate/{form}")
async def all_buku(form:str, filter:dict = Body(...)):
    form = form.lower()
    data_buku = await database.find_buku(form,filter=filter)

    if not data_buku:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    
    save_download_path = f"download/buku/{form}"
    return FileResponse(path=f"{save_download_path}.xlsx", filename=f"{form}.xlsx")


@router.get("/v3/generate/{form}/{id}")
async def buku_with_id(form:str,id:str):
    form = form.lower()
    data_buku = await database.find_buku_with_id(form,id)
    if not data_buku:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    
    save_download_path = f"download/buku/{form}"
    return FileResponse(path=f"{save_download_path}.xlsx", filename=f"{form}.xlsx")




    