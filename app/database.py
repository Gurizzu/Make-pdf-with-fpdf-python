import pymongo

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
    
    
# data = {"Menjadi" : "menjadi"}

# domisili.insert_one(data)

