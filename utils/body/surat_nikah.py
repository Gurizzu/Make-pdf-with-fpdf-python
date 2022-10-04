from fpdf import FPDF

async def surat_nikah(pdf:FPDF,data:dict):
    
    #Add margin,page,and title surat
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT PENGANTAR NIKAH",ln=1)
    
    no_surat_nikah = data.get("umum").get("nomor_surat") # Can be replace with no nikah in database 
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=str(no_surat_nikah))
    pdf.set_text_color(0,0,0)
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\t\tYang bertanda tangan di bawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sesungguhnya bahwa:",ln=1)
    pdf.ln(3)
    
    
    # receive data from database
    mempelai = [{
        "Nama Lengkap": data.get("umum").get("nama_lengkap"),
        "Tempat, Tanggal Lahir" : str(data.get("umum").get("tempat_lahir")) + ", " + str(data.get("umum").get("tanggal_lahir")),
        "Jenis Kelamin" : data.get("umum").get("jenis_kelamin"),
        "Agama": data.get('umum').get("agama"),
        "Pekerjaan" : data.get("umum").get("pekerjaan"),
        "Status" : data.get("umum").get("status_perkawinan"),
        "Dusun" : data.get("umum").get("dusun"),
        
    }]
    ayah = [{
        "Nama Lengkap": data.get("ayah").get("nama_lengkap"),
        "Tempat, Tanggal Lahir" : str(data.get("ayah").get("tempat_lahir")) + ", " + str(data.get("ayah").get("tanggal_lahir")),
        "Agama": data.get("ayah").get("agama"),
        "Pekerjaan" : data.get("ayah").get("pekerjaan"),
        "Alamat" : data.get("ayah").get("alamat"),
    }]
    ibu = [{
        "Nama Lengkap": data.get("ibu").get("nama_lengkap"),
        "Tempat, Tanggal Lahir" : str(data.get("ibu").get("tempat_lahir")) + ", " + data.get("ibu").get("tanggal_lahir"),
        "Agama": data.get("ibu").get("agama"),
        "Pekerjaan" : data.get("ibu").get("pekerjaan"),
        "Alamat" : data.get("ibu").get("alamat"),
    }]
    
    #looping data from list of dict
    for da in mempelai:
        for key, val in da.items():
                if key =='Nama Lengkap':
                    pdf.cell(25,5,border=0,align="R",txt="I.")
                    pdf.cell(5,5,border=0)
                    pdf.cell(50,5,border=0,align="L",txt=key)
                    pdf.cell(3,5,border=0,align="L", txt=":")
                    pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)
                else:
                    pdf.cell(25,5,border=0,align="R")
                    pdf.cell(5,5,border=0)
                    pdf.cell(50,5,border=0,align="L",txt=key)
                    pdf.cell(3,5,border=0,align="L", txt=":")
                    pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)
    
    pdf.cell(25,5,border=0,align="R",txt="II.")
    pdf.cell(5,5,border=0)
    pdf.cell(50,5,border=0,align="L",txt="AYAH",ln=1)
    
    #looping data ayah
    for da3 in ayah:
        for key, val in da3.items():
                pdf.cell(25,5,border=0,align="R",txt="")
                pdf.cell(5,5,border=0)
                pdf.cell(50,5,border=0,align="L",txt=key)
                pdf.cell(3,5,border=0,align="L", txt=":")
                pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)
                
                
    pdf.cell(25,5,border=0,align="R",txt="III.")
    pdf.cell(5,5,border=0)
    pdf.cell(50,5,border=0,align="L",txt="IBU",ln=1)
    
    #looping data ibu
    for da3 in ibu:
        for key, val in da3.items():
                pdf.cell(25,5,border=0,align="R",txt="")
                pdf.cell(5,5,border=0)
                pdf.cell(50,5,border=0,align="L",txt=key)
                pdf.cell(3,5,border=0,align="L", txt=":")
                pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1) 
                
    pdf.ln(3)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""\t\t\t\t\t\t\t\t\tPemilik nama tersebut di atas adalah benar warga kami Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung dan sepengatuhan kami yang bersangkutan berkelakuan baik. Surat keterangan pengantar ini diberikan untuk keperluan pengurusan surat nikah.""",ln=1)

    pdf.ln(3)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""\t\t\t\t\t\t\t\t\tDemikian surat keterangan ini dibuat dengan sebenarnya dan diberikan untuk dapat 
    dipergunakan sebagaimana mestinya.""",ln=1)