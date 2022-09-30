import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["surat"]

domisili = mydb["SuratDomisili"]
kematian = mydb["SuratKematian"]
nikah = mydb["SuratNikah"]

async def make_domisisli(data:dict):
    domisili.insert_one(data)
    id = data.get('_id')
    data["_id"] = str(id)
    return data

async def make_kematian(data:dict):
    kematian.insert_one(data)
    id = data.get('_id')
    data["_id"] = str(id)
    return data

async def make_Nikah(data:dict):
    nikah.insert_one(data)
    id = data.get('_id')
    data["_id"] = str(id)
    return data

async def find_one(form:str,id:str):
    
    if form == "surat_nikah":
        _id = ObjectId(id)
        data_nikah = nikah.find_one({"_id": _id})
        if not data_nikah:
            return False
        return data_nikah
    
    elif form == "surat_kematian":
        _id = ObjectId(id)
        data_kematian =  kematian.find_one({"_id": _id})
        if not data_kematian:
            return False
        return data_kematian
        
    elif form == "surat_domisili":
        _id = ObjectId(id)
        data_domisili = domisili.find_one({"_id": _id})
        if not data_domisili:
            return False
        return data_domisili
    
    else:
        return False
        
    
# data = {"Menjadi" : "menjadi"}

# domisili.insert_one(data)

