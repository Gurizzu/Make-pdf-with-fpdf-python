import pymongo
from bson.objectid import ObjectId
from datetime import datetime
from utils.buku.buku_agenda import buku_agenda
from utils.buku.buku_bank_desa import buku_bank_desa
from utils.buku.buku_ekspedisi import buku_ekspedisi
from utils.buku.buku_inventaris_hasil_hasil_pembangunan import buku_inventaris_hasil_hasil_pembangunan
from utils.buku.buku_inventaris_kekayaan_desa import buku_inventaris_kekayaan_desa
from utils.buku.buku_kader_pemberdayaan_masyarakat import buku_kader_pemberdayaan_masyarakat
from utils.buku.buku_kas_pembantu import buku_kas_pembantu
from utils.buku.buku_kas_pembantu_kegiatan import buku_kas_pembantu_kegiatan
from utils.buku.buku_kas_umum import buku_kas_umum
from utils.buku.buku_kegiatan_pembangunan import buku_kegiatan_pembangunan
from utils.buku.buku_keputusan_kepala_desa import buku_keputusan_kepala_desa
from utils.buku.buku_lembaran_desa_dan_berita_desa import buku_lembaran_desa_dan_berita_desa
from utils.buku.buku_peraturan_di_desa import buku_peraturan_di_desa
from utils.buku.buku_aparat_pemerintah_desa import buku_aparat_pemerintah_desa
from utils.buku.buku_rencana_kerja_pembangunan import buku_rencana_kerja_pembangunan
from utils.buku.buku_tanah_di_desa import buku_tanah_di_desa


myclient = pymongo.MongoClient("mongodb://userdesa:desa123@192.168.247.22:27017/?authSource=dev-sidesa&directConnection=true")

mydb = myclient["dev-sidesa"]

surat_keterangan_domisili = mydb["surat_keterangan_domisili"]
surat_keterangan_kematian = mydb["surat_keterangan_kematian"]
surat_pengantar_nikah = mydb["surat_pengantar_nikah"]
surat_keterangan_usaha = mydb["surat_keterangan_usaha"]
surat_keterangan_belum_pernah_nikah = mydb["surat_keterangan_belum_pernah_nikah"]
surat_keterangan_pindah = mydb["surat_keterangan_pindah"]
pengaturan_footer_surat = mydb["v_pengaturan_surat"]
surat_keterangan_kehilangan = mydb["surat_kehilangan"]
surat_keterangan_tidak_mampu = mydb["surat_keterangan_tidak_mampu"]
surat_keterangan_penghasilan_orang_tua = mydb["surat_keterangan_penghasilan_orang_tua"]
surat_keterangan_pernah_nikah = mydb["surat_keterangan_pernah_nikah"]
surat_keterangan_kelakuan_baik = mydb["surat_keterangan_kelakuan_baik"]
surat_keterangan_duda_atau_janda = mydb["surat_keterangan_duda_atau_janda"]
col_buku_peraturan_di_desa = mydb["buku_peraturan_di_desa"]
col_buku_lembaran_desa_dan_berita_desa = mydb["buku_lembaran_desa_dan_berita_desa"]
col_buku_inventaris_kekayaan_desa = mydb["buku_inventaris_kekayaan_desa"]
col_buku_agenda = mydb["buku_agenda"]
col_buku_ekspedisi = mydb["buku_ekspedisi"]
col_buku_keputusan_kepala_desa = mydb["buku_keputusan_kepala_desa"]
col_buku_aparat_pemerintah_desa = mydb["buku_aparat_pemerintah_desa"]
col_buku_tanah_di_desa = mydb["buku_tanah_di_desa"]
col_buku_kas_pembantu_kegiatan = mydb["buku_kas_pembantu_kegiatan"]
col_buku_kas_umum = mydb["buku_kas_umum"]
col_buku_kas_pembantu = mydb["buku_kas_pembantu"]
col_buku_bank_desa = mydb["buku_bank_desa"]
col_buku_rencana_kerja_pembangunan = mydb["buku_rencana_kerja_pembangunan"]
col_buku_kegiatan_pembangunan = mydb["buku_kegiatan_pembangunan"]
col_buku_inventaris_hasil_hasil_pembangunan = mydb["buku_inventaris_hasil_hasil_pembangunan"]
col_buku_kader_pemberdayaan_masyarakat = mydb["buku_kader_pemberdayaan_masyarakat"]

async def make_domisisli(data:dict):
    surat_keterangan_domisili.insert_one(data)
    id = data.get('_id')
    data["_id"] = str(id)
    return data

async def make_kematian(data:dict):
    surat_keterangan_kematian.insert_one(data)
    id = data.get('_id')
    data["_id"] = str(id)
    return data

async def make_Nikah(data:dict):
    surat_pengantar_nikah.insert_one(data)
    id = data.get('_id')
    data["_id"] = str(id)
    return data

async def find_one(form:str,id:str):
    
    if form == "surat_pengantar_nikah":
        _id = id
        data_nikah = surat_pengantar_nikah.find_one({"_id": _id})
        if not data_nikah:
            return False
        data_nikah['nama_pembuat'] = data_nikah.get("umum").get("nama_lengkap")
        data_nikah['nama_surat'] = form.replace("_","-")
        data_nikah["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_nikah
    
    elif form == "surat_keterangan_kematian":
        _id = id
        data_kematian = surat_keterangan_kematian.find_one({"_id": _id})
        if not data_kematian:
            return False
        data_kematian['nama_pembuat'] = data_kematian.get("umum").get("nama_lengkap")
        data_kematian['nama_surat'] = form.replace("_","-")
        data_kematian["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_kematian
        
    elif form == "surat_keterangan_domisili":
        
        _id = id
        data_domisili = surat_keterangan_domisili.find_one({"_id": _id})
        if not data_domisili:
            return False
        data_domisili['nama_pembuat'] = data_domisili.get("nama")
        data_domisili['nama_surat'] = form.replace("_","-")
        data_domisili["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_domisili

    elif form == "surat_keterangan_belum_pernah_nikah":
        _id = id
        data_surat_keterangan_belum_pernah_nikah = surat_keterangan_belum_pernah_nikah.find_one({"_id": _id})
        if not data_surat_keterangan_belum_pernah_nikah:
            return False
        data_surat_keterangan_belum_pernah_nikah['nama_pembuat'] = data_surat_keterangan_belum_pernah_nikah.get("nama_lengkap")
        data_surat_keterangan_belum_pernah_nikah['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_belum_pernah_nikah["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_keterangan_belum_pernah_nikah
    
    elif form == "surat_keterangan_pindah":
        _id = id
        data_surat_keterangan_pindah = surat_keterangan_pindah.find_one({"_id": _id})
        if not data_surat_keterangan_pindah:
            return False
        data_surat_keterangan_pindah['nama_pembuat'] = data_surat_keterangan_pindah.get("umum").get("nama")
        data_surat_keterangan_pindah['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_pindah["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_keterangan_pindah
    
    elif form == "surat_keterangan_usaha":
        _id = id
        data_surat_ketarangan_usaha = surat_keterangan_usaha.find_one({"_id": _id})
        if not data_surat_ketarangan_usaha:
            return False
        data_surat_ketarangan_usaha['nama_pembuat'] = data_surat_ketarangan_usaha.get("nama")
        data_surat_ketarangan_usaha['nama_surat'] = form.replace("_","-")
        data_surat_ketarangan_usaha["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_ketarangan_usaha
    
    elif form == "surat_keterangan_kehilangan":
        _id = id
        data_surat_ketarangan_kehilangan = surat_keterangan_kehilangan.find_one({"_id": _id})
        if not data_surat_ketarangan_kehilangan:
            return False
        data_surat_ketarangan_kehilangan['nama_pembuat'] = data_surat_ketarangan_kehilangan.get("nama_lengkap")
        data_surat_ketarangan_kehilangan['nama_surat'] = form.replace("_","-")
        data_surat_ketarangan_kehilangan["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_ketarangan_kehilangan

    elif form == "surat_keterangan_tidak_mampu":
        _id = id
        data_surat_keterangan_tidak_mampu = surat_keterangan_tidak_mampu.find_one({"_id": _id})
        if not data_surat_keterangan_tidak_mampu:
            return False
        data_surat_keterangan_tidak_mampu['nama_pembuat'] = data_surat_keterangan_tidak_mampu.get("nama_lengkap")
        data_surat_keterangan_tidak_mampu['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_tidak_mampu["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_keterangan_tidak_mampu
    
    elif form == "surat_keterangan_penghasilan_orang_tua":
        _id = id
        data_surat_keterangan_penghasilan_orang_tua = surat_keterangan_penghasilan_orang_tua.find_one({"_id": _id})
        if not data_surat_keterangan_penghasilan_orang_tua:
            return False
        data_surat_keterangan_penghasilan_orang_tua['nama_pembuat'] = data_surat_keterangan_penghasilan_orang_tua.get("nama_lengkap")
        data_surat_keterangan_penghasilan_orang_tua['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_penghasilan_orang_tua["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_keterangan_penghasilan_orang_tua
    
    elif form == "surat_keterangan_pernah_nikah":
        _id = id
        data_surat_keterangan_pernah_nikah = surat_keterangan_pernah_nikah.find_one({"_id": _id})
        if not data_surat_keterangan_pernah_nikah:
            return False
        data_surat_keterangan_pernah_nikah['nama_pembuat'] = data_surat_keterangan_pernah_nikah.get("umum").get("nama") if not data_surat_keterangan_pernah_nikah.get("umum").get("nama_lengkap") else data_surat_keterangan_pernah_nikah.get("umum").get("nama_lengkap")
        data_surat_keterangan_pernah_nikah['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_pernah_nikah["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_keterangan_pernah_nikah
    
    elif form == "surat_keterangan_kelakuan_baik":
        _id = id
        data_surat_keterangan_kelakuan_baik = surat_keterangan_kelakuan_baik.find_one({"_id": _id})
        if not data_surat_keterangan_kelakuan_baik:
            return False
        data_surat_keterangan_kelakuan_baik['nama_pembuat'] = data_surat_keterangan_kelakuan_baik.get("nama_lengkap")
        data_surat_keterangan_kelakuan_baik['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_kelakuan_baik["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_keterangan_kelakuan_baik
    
    elif form == "surat_keterangan_duda_atau_janda":
        _id = id
        data_surat_keterangan_duda_atau_janda = surat_keterangan_duda_atau_janda.find_one({"_id": _id})
        if not data_surat_keterangan_duda_atau_janda:
            return False
        data_surat_keterangan_duda_atau_janda['nama_pembuat'] = data_surat_keterangan_duda_atau_janda.get("nama_lengkap")
        data_surat_keterangan_duda_atau_janda['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_duda_atau_janda["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        return data_surat_keterangan_duda_atau_janda

    else:
        return False
    
async def get_footer_by_form(form:str) -> dict:
    query = {"form" : form}
    
    footer = pengaturan_footer_surat.find_one(query)
    if not footer:
        return pengaturan_footer_surat.find_one({"form" : "default"})

    return footer
    

async def find_buku(form:str):
    if form == "buku_peraturan_di_desa":
        cursor = col_buku_peraturan_di_desa.find()
        if not cursor:
            return False
        await buku_peraturan_di_desa(data=cursor)
        return True
    elif form == "buku_lembaran_desa_dan_berita_desa":
        cursor = col_buku_lembaran_desa_dan_berita_desa.find()
        if not cursor:
            return False
        await buku_lembaran_desa_dan_berita_desa(data=cursor)
        return True

    elif form == "buku_inventaris_kekayaan_desa":
        cursor = col_buku_inventaris_kekayaan_desa.find()
        if not cursor:
            return False
        await buku_inventaris_kekayaan_desa(data=cursor)
        return True
    elif form == "buku_agenda":
        cursor = col_buku_agenda.find()
        if not cursor:
            return False
        await buku_agenda(data=cursor)
        return True
    elif form == "buku_ekspedisi":
        cursor = col_buku_ekspedisi.find()
        if not cursor:
            return False
        await buku_ekspedisi(data=cursor)
        return True
    elif form == "buku_keputusan_kepala_desa":
        cursor = col_buku_keputusan_kepala_desa.find()
        if not cursor:
            return False
        await buku_keputusan_kepala_desa(data=cursor)
        return True
    elif form == "buku_aparat_pemerintah_desa":
        cursor = col_buku_aparat_pemerintah_desa.find()
        if not cursor:
            return False
        await buku_aparat_pemerintah_desa(data=cursor)
        return True
    elif form == "buku_tanah_di_desa":
        cursor = col_buku_tanah_di_desa.find()
        if not cursor:
            return False
        await buku_tanah_di_desa(data=cursor)
        return True
    elif form == "buku_kas_pembantu_kegiatan":
        cursor = col_buku_kas_pembantu_kegiatan.find()
        if not cursor:
            return False
        await buku_kas_pembantu_kegiatan(data=cursor)
        return True
    elif form == "buku_kas_umum":
        cursor = col_buku_kas_umum.find()
        if not cursor:
            return False
        await buku_kas_umum(data=cursor)
        return True
    elif form == "buku_kas_pembantu":
        cursor = col_buku_kas_pembantu.find()
        if not cursor:
            return False
        await buku_kas_pembantu(data=cursor)
        return True
    elif form == "buku_bank_desa":
        cursor = col_buku_bank_desa.find()
        if not cursor:
            return False
        await buku_bank_desa(data=cursor)
        return True
    elif form == "buku_rencana_kerja_pembangunan":
        cursor = col_buku_rencana_kerja_pembangunan.find()
        if not cursor:
            return False
        await buku_rencana_kerja_pembangunan(data=cursor)
        return True
    elif form == "buku_kegiatan_pembangunan":
        cursor = col_buku_kegiatan_pembangunan.find()
        if not cursor:
            return False
        await buku_kegiatan_pembangunan(data=cursor)
        return True
    elif form == "buku_inventaris_hasil_hasil_pembangunan":
        cursor = col_buku_inventaris_hasil_hasil_pembangunan.find()
        if not cursor:
            return False
        await buku_inventaris_hasil_hasil_pembangunan(data=cursor)
        return True
    elif form == "buku_kader_pemberdayaan_masyarakat":
        cursor = col_buku_kader_pemberdayaan_masyarakat.find()
        if not cursor:
            return False
        await buku_kader_pemberdayaan_masyarakat(data=cursor)
        return True
    else:
        return False
    
    
# data = {"Menjadi" : "menjadi"}

# domisili.insert_one(data)

