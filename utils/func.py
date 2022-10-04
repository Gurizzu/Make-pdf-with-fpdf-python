from fpdf import FPDF
from .body.surat_domisili import surat_domisili
from .body.surat_nikah import surat_nikah
from .body.surat_kematian import surat_keterangan_kematian
from .body.surat_keterangan_usaha import surat_keterangan_usaha
from .tmp_footer import footer2
from .tmp_header import header


  
async def run_surat(pdf:FPDF,foot:dict,data:dict,output:str,form:str):
    
    await header(pdf=pdf)
    
    if form == "surat_pengantar_nikah":
        await surat_nikah(pdf=pdf,data=data)
    elif form == "surat_keterangan_kematian":
        await surat_keterangan_kematian(pdf=pdf,data=data)
    elif form == "surat_keterangan_domisili":
        await surat_domisili(pdf=pdf,data=data)
    elif form == "surat_keterangan_usaha":
        await surat_keterangan_usaha(pdf=pdf, data=data)
        
    await footer2(pdf=pdf, data=foot)
    pdf.output(f"{output}.pdf")
    
    

