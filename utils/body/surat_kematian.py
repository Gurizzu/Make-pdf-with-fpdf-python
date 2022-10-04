from fpdf import FPDF
 
async def surat_keterangan_kematian(pdf:FPDF,data:dict):
    
 
    pdf.ln(1)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN KEMATIAN",ln=1)
    
    no_surat_kematian = data.get("nomor_surat") # Can be replace with no nikah in database 
    
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.cell(80,h=8 ,align="L",border=0,txt=str(no_surat_kematian))
    
    pdf.set_font("arial","",8)
    pdf.set_margins(27, 27)
    pdf.ln(5)
    pdf.cell(0,h=8 ,align="L",border=0,ln=1,txt="Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung, dengan ini menerangkan bahwa :")
    pdf.ln(2)
    
    pdf.set_margins(25, 25)
    
    #get data from database
    data_orang_meninggal = [{
        "Nama" : data.get("umum").get("nama_lengkap"),
        "Tempat, Tanggal Lahir" : data.get("umum").get("tempat_lahir") + ", " + data.get("umum").get("tanggal_lahir"),
        "Jenis Kelamin" : data.get("umum").get("jenis_kelamin"),
        "Alamat" : data.get("umum").get("alamat"),
        "Agama" : data.get("umum").get("agama"),
        "Status Perkawinan": data.get("umum").get("status_perkawinan"),
        "Pekerjaan" : data.get("umum").get("pekerjaan"),
        "Kewarganegaraan" : data.get("umum").get("kewarganegaraan"),
        "NIK" : data.get("umum").get("nik")
        
    }]
    
    waktu = [{
        "Tanggal": data.get("kematian").get("tanggal_kematian"),
        "Pukul/Jam": data.get("kematian").get("jam_kematian"),
        "Bertempat di": data.get("kematian").get("tempat_kematian"),
        "Penyebab Kematian": data.get("kematian").get("sebab_kematian"),
    }]
    
    pelapor = [{
        "Nama": data.get("pelapor").get("nama_lengkap"),
        "Jenis": data.get("pelapor").get("jenis_kelamin"),
        "Alamat": data.get("pelapor").get("alamat"),
        "Hubungan Dengan Alm/Almh": data.get("pelapor").get("hubungan_dengan_yang_meninggal"),
        
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