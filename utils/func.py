from fpdf import FPDF

from .body.surat_keterangan_penghasilan_orang_tua import surat_keterangan_penghasilan_orang_tua
from .body.surat_domisili import surat_domisili
from .body.surat_nikah import surat_nikah
from .body.surat_kematian import surat_keterangan_kematian
from .body.surat_keterangan_usaha import surat_keterangan_usaha
from .body.surat_belum_menikah import surat_belum_nikah
from .body.surat_pindah import surat_pindah
from .body.surat_keterangan_kehilangan import surat_keterangan_kehilangan
from .body.surat_keterangan_tidak_mampu import surat_keterangan_tidak_mampu
from .tmp_footer import footer2
from .tmp_header import header


  
async def run_surat(pdf:FPDF,foot:dict,data:dict,output:str,form:str):
    
    await header(pdf=pdf)
    
    # Surat Pengantar Nikah
    if form == "surat_pengantar_nikah":
        await surat_nikah(pdf=pdf,data=data)

    # Surat Keterangan Kematian
    elif form == "surat_keterangan_kematian":
        await surat_keterangan_kematian(pdf=pdf,data=data)

    # Surat Keterangan Domisli
    elif form == "surat_keterangan_domisili":
        await surat_domisili(pdf=pdf,data=data)

    # Surat Keterangan Usaha
    elif form == "surat_keterangan_usaha":
        await surat_keterangan_usaha(pdf=pdf, data=data)

    # Surat Keterangan Belum Pernah Nikah
    elif form == "surat_keterangan_belum_pernah_nikah":
        await surat_belum_nikah(pdf=pdf,data=data)

    # Surat Keterangan Pindah
    elif form == "surat_keterangan_pindah":
        await surat_pindah(pdf=pdf, data=data)

    # Surat Keterangan Kehilangan
    elif form == "surat_keterangan_kehilangan":
        await surat_keterangan_kehilangan(pdf=pdf, data=data)

    # Surat Keterangan Tidak mampu
    elif form == "surat_keterangan_tidak_mampu":
        await surat_keterangan_tidak_mampu(pdf=pdf, data=data)
        
    # Surat Keterangan penghasilan orang tua
    elif form == "surat_keterangan_penghasilan_orang_tua":
        await surat_keterangan_penghasilan_orang_tua(pdf=pdf, data=data)
        
    await footer2(pdf=pdf, data=foot)
    pdf.output(f"{output}.pdf")
    
    

