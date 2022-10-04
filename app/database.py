import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://userdesa:desa123@192.168.247.22:27017/?authSource=dev-sidesa&directConnection=true")

mydb = myclient["dev-sidesa"]

surat_keterangan_domisili = mydb["surat_keterangan_domisili"]
surat_keterangan_kematian = mydb["surat_keterangan_kematian"]
surat_pengantar_nikah = mydb["surat_pengantar_nikah"]
surat_keterangan_usaha = mydb["surat_keterangan_usaha"]

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
        return data_nikah
    
    elif form == "surat_keterangan_kematian":
        _id = id
        data_kematian =  surat_keterangan_kematian.find_one({"_id": _id})
        if not data_kematian:
            return False
        return data_kematian
        
    elif form == "surat_keterangan_domisili":
        _id = id
        data_domisili = surat_keterangan_domisili.find_one({"_id": _id})
        if not data_domisili:
            return False
        return data_domisili

    elif form == "surat_keterangan_usaha":
        _id = id
        data_surat_ketarangan_usaha = surat_keterangan_usaha.find_one({"_id": _id})
        if not data_surat_ketarangan_usaha:
            return False
        return data_surat_ketarangan_usaha
    
    else:
        return False
        
    
# data = {"Menjadi" : "menjadi"}

# domisili.insert_one(data)

