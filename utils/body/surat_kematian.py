from fpdf import FPDF
 
async def surat_keterangan_kematian(pdf:FPDF,data:dict):
    
 
    pdf.ln(1)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN KEMATIAN",ln=1)
    
    no_nikah = data.get("nomor_surat") # Can be replace with no nikah in database 
    
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.cell(80,h=8 ,align="L",border=0,txt=no_nikah)
    
    pdf.set_font("arial","",8)
    pdf.set_margins(27, 27)
    pdf.ln(5)
    pdf.cell(0,h=8 ,align="L",border=0,ln=1,txt="Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung, dengan ini menerangkan bahwa :")
    pdf.ln(2)
    
    pdf.set_margins(25, 25)
    
    #get data from database
    data_orang_meninggal = [{
        "Nama" : data.get("nama_almarhum"),
        "Tempat, Tanggal Lahir" : data.get("tempat_tanggal_lahir_almarhum"),
        "Jenis Kelamin" : data.get("jenis_kelamin_almarhum"),
        "Alamat" : data.get("alamat_lengkap_almarhum"),
        "Agama" : data.get("agama_almarhum"),
        "Status Perkawinan": data.get("status_perkawinan_almarhum"),
        "Pekerjaan" : data.get("pekerjaan_almarhum"),
        "Kewarganegaraan" : data.get("kewarganegaraan_almarhum"),
        "nik_almarhum" : data.get("nik_almarhum")
        
    }]
    
    waktu = [{
        "Tanggal": data.get("tanggal_meninggal_almarhum"),
        "Pukul/Jam": data.get("jam_meninggal_almarhum"),
        "Bertempat di": data.get("tempat_meninggal_almarhum"),
        "Penyebab Kematian": data.get("penyebab_kematian_almarhum"),
    }]
    
    pelapor = [{
        "Nama": data.get("nama_pelapor_kematian"),
        "Jenis": data.get("jenis_kelamin_pelapor"),
        "Alamat": data.get("alamat_lengkap_pelapor"),
        "Hubungan Dengan Alm/Almh": data.get("hubungan_pelapor_dengan_almarhum"),
        
    }]
    
    pulan = data.get("nama_bapak_almarhum") #Placeholder for database
    
    #looping through list of dict
    for datorgal in data_orang_meninggal:
        for key, val in datorgal.items():
            if key == "Nama":
                pdf.cell(50,h=6,border=0,align="L",txt=key)
                pdf.cell(3,6,border=0,align="L", txt=":")
                pdf.multi_cell(107,h=6,border=0,align="L",txt=f"{val} bin {pulan}",ln=1)
            else:
                pdf.cell(50,h=6,border=0,align="L",txt=key)
                pdf.cell(3,6,border=0,align="L", txt=":")
                pdf.multi_cell(107,h=6,border=0,align="L",txt=str(val),ln=1)
    
    
    
    pdf.ln(1)
    # Some Text
    pdf.cell(txt='            Orang tersebut diatas benar' , border=0)
    pdf.set_font(family='arial', style="B" , size=8)
    pdf.cell(txt="Meninggal Dunia", border=0)
    pdf.set_font(family='arial', style="" , size=8)
    pdf.cell(txt="pada :", border=0 , ln=True)
    pdf.ln(1)
    
    
    # Second Form In Surat Kematian
    for wak in waktu:
        for key,val in wak.items():
            pdf.cell(50,6, align="L", border=0, txt=key)
            pdf.cell(3,6,border=0, align="R" ,txt=":")
            pdf.multi_cell(0,6, align="L", border=0, ln=1, txt=str(val))
            
    pdf.ln(1)
    # Some Text
    pdf.multi_cell(0,h=3,align="L", txt='            Surat keterangan ini di buat berdasarkan laporan dari :', ln=True)
    pdf.ln(1)
    
    
    # Third Form in Surat Kematian
    for pel in pelapor:
        for key,val in pel.items():
            pdf.cell(50,6, align="L", border=0, txt=key)
            pdf.cell(3,6,border=0, align="R" ,txt=":")
            pdf.multi_cell(0,6, align="L", border=0, ln=1, txt=str(val))
            
            
    pdf.ln(1)
    # Surat Kematia Footer
    pdf.multi_cell(0,h=3,align="L", txt='            Demikian surat keterangan ini kami buat, untuk dipergunakan sebagaimana mestinya.', ln=True)
    pdf.ln(1)