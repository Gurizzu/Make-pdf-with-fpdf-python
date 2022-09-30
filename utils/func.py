from fpdf import FPDF
from .body.surat_domisili import surat_domisili
from .body.surat_nikah import surat_nikah
from .body.surat_kematian import surat_keterangan_kematian
from .tmp_footer import footer2
from .tmp_header import header


  
async def run_surat(pdf:FPDF,foot:dict,data:dict,output:str,form:str):
    
    await header(pdf=pdf)
    
    if form == "surat_nikah":
        await surat_nikah(pdf=pdf,data=data)
    elif form == "surat_kematian":
        await surat_keterangan_kematian(pdf=pdf,data=data)
    elif form == "surat_domisili":
        await surat_domisili(pdf=pdf,data=data)
        
    await footer2(pdf=pdf, data=foot)
    pdf.output(f"{output}.pdf")
    
    

