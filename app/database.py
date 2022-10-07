import pymongo
from bson.objectid import ObjectId
from datetime import datetime

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
    
        
    
# data = {"Menjadi" : "menjadi"}

# domisili.insert_one(data)

