from fpdf import FPDF

from .buku.buku_agenda import buku_agenda
from .buku.buku_ekspedisi import buku_ekspedisi

from .buku.buku_lembaran_desa_dan_berita_desa import buku_lembaran_desa_dan_berita_desa
from .buku.buku_inventaris_kekayaan_desa import buku_inventaris_kekayaan_desa

from .buku.buku_keputusan_kepala_desa import buku_keputusan_kepala_desa

from .body.surat_keterangan_penghasilan_orang_tua import surat_keterangan_penghasilan_orang_tua
from .body.surat_domisili import surat_domisili
from .body.surat_nikah import surat_nikah
from .body.surat_kematian import surat_keterangan_kematian
from .body.surat_keterangan_usaha import surat_keterangan_usaha
from .body.surat_belum_menikah import surat_belum_nikah
from .body.surat_pindah import surat_pindah
from .body.surat_keterangan_kehilangan import surat_keterangan_kehilangan
from .body.surat_keterangan_tidak_mampu import surat_keterangan_tidak_mampu
from .body.surat_keterangan_pernah_nikah import surat_keterangan_pernah_nikah
from .body.surat_keterangan_kelakuan_baik import surat_keterangan_kelakuan_baik
from .body.surat_keterangan_duda_atau_janda import surat_keterangan_duda_atau_janda
from .buku.buku_peraturan_di_desa import buku_peraturan_di_desa
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
        
    # Surat Keterangan pernah nikah
    elif form == "surat_keterangan_pernah_nikah":
        await surat_keterangan_pernah_nikah(pdf=pdf, data=data)

    # surat_keterangan_kelakuan_baik
    elif form == "surat_keterangan_kelakuan_baik":
        await surat_keterangan_kelakuan_baik(pdf=pdf, data=data)
        
    elif form == "surat_keterangan_duda_atau_janda":
        await surat_keterangan_duda_atau_janda(pdf=pdf, data=data)

    await footer2(pdf=pdf, data=foot)
    pdf.output(f"{output}.pdf")
    
async def run_buku(form:str,data:dict):
    if form == "buku_peraturan_di_desa":
        await buku_peraturan_di_desa(data=data)
        
    elif form == "buku_lembaran_desa_dan_berita_desa":
        await buku_lembaran_desa_dan_berita_desa(data=data)
        
    elif form == "buku_inventaris_kekayaan_desa":
        await buku_inventaris_kekayaan_desa(data=data)
        
    elif form == "buku_agenda":
        await buku_agenda(data=data)
        
    elif form == "buku_ekspedisi":
        await buku_ekspedisi(data=data)
    
    elif form == "buku_keputusan_kepala_desa":
        await buku_keputusan_kepala_desa(data=data)
