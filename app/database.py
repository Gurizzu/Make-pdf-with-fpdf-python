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
        data_nikah['nama_pembuat'] = data_nikah.get("umum").get("nama_lengkap")
        data_nikah['nama_surat'] = form.replace("_","-")
        data_nikah["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        if not data_nikah:
            return False
        return data_nikah
    
    elif form == "surat_keterangan_kematian":
        _id = id
        data_kematian =  surat_keterangan_kematian.find_one({"_id": _id})
        data_kematian['nama_pembuat'] = data_kematian.get("umum").get("nama_lengkap")
        data_kematian['nama_surat'] = form.replace("_","-")
        data_kematian["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        if not data_kematian:
            return False
        return data_kematian
        
    elif form == "surat_keterangan_domisili":
        
        _id = id
        data_domisili = surat_keterangan_domisili.find_one({"_id": _id})
        data_domisili['nama_pembuat'] = data_domisili.get("nama")
        data_domisili['nama_surat'] = form.replace("_","-")
        data_domisili["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        if not data_domisili:
            return False
        return data_domisili

    elif form == "surat_keterangan_belum_pernah_nikah":
        _id = id
        data_surat_keterangan_belum_pernah_nikah = surat_keterangan_belum_pernah_nikah.find_one({"_id": _id})
        data_surat_keterangan_belum_pernah_nikah['nama_pembuat'] = data_surat_keterangan_belum_pernah_nikah.get("nama_lengkap")
        data_surat_keterangan_belum_pernah_nikah['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_belum_pernah_nikah["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        if not data_surat_keterangan_belum_pernah_nikah:
            return False
        return data_surat_keterangan_belum_pernah_nikah
    
    elif form == "surat_keterangan_pindah":
        _id = id
        data_surat_keterangan_pindah = surat_keterangan_pindah.find_one({"_id": _id})
        data_surat_keterangan_pindah['nama_pembuat'] = data_surat_keterangan_pindah.get("umum").get("nama")
        data_surat_keterangan_pindah['nama_surat'] = form.replace("_","-")
        data_surat_keterangan_pindah["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        if not data_surat_keterangan_pindah:
            return False
        return data_surat_keterangan_pindah
    
    elif form == "surat_keterangan_usaha":
        _id = id
        data_surat_ketarangan_usaha = surat_keterangan_usaha.find_one({"_id": _id})
        data_surat_ketarangan_usaha['nama_pembuat'] = data_surat_ketarangan_usaha.get("nama")
        data_surat_ketarangan_usaha['nama_surat'] = form.replace("_","-")
        data_surat_ketarangan_usaha["tanggal_print"] = datetime.today().strftime('%m%d%Y')
        if not data_surat_ketarangan_usaha:
            return False
        return data_surat_ketarangan_usaha
    
    else:
        return False
        
    
# data = {"Menjadi" : "menjadi"}

# domisili.insert_one(data)

