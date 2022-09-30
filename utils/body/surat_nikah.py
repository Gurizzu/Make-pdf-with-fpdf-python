from fpdf import FPDF

async def surat_nikah(pdf:FPDF,data:dict):
    
    #Add margin,page,and title surat
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT PENGANTAR NIKAH",ln=1)
    
    no_nikah = data.get("nomor_surat") # Can be replace with no nikah in database 
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_nikah)
    pdf.set_text_color(0,0,0)
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\t\tYang bertanda tangan di bawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sesungguhnya bahwa:",ln=1)
    pdf.ln(3)
    
    
    # receive data from database
    data1 = [{
        "Nama Lengkap": data.get("nama_mempelai"),
        "Tempat, Tanggal Lahir" : data.get("tempat_tanggal_lahir_mempelai"),
        "Jenis Kelamin" : data.get("jenis_kelamin_mempelai"),
        "Agama": data.get('agama_mempelai'),
        "Pekerjaan" : data.get("pekerjaan_mempelai"),
        "Status" : data.get("status_mempelai"),
        "Dusun" : data.get("dusun_mempelai"),
        
    }]
    data2 = [{
        "Nama Lengkap": data.get("nama_ayah_mempelai"),
        "Tempat, Tanggal Lahir" : data.get("tempat_tanggal_lahir_ayah_mempelai"),
        "Agama": data.get("agama_ayah_mempelai"),
        "Pekerjaan" : data.get("pekerjaan_ayah_mempelai"),
        "Alamat" : data.get("alamat_ayah_mempelai"),
    }]
    data3 = [{
        "Nama Lengkap": data.get("nama_ibu_mempelai"),
        "Tempat, Tanggal Lahir" : data.get("tempat_tanggal_lahir_ibu_mempelai"),
        "Agama": data.get("agama_ibu_mempelai"),
        "Pekerjaan" : data.get("pekerjaan_ibu_mempelai"),
        "Alamat" : data.get("alamat_ibu_mempelai"),
    }]
    
    #looping data from list of dict
    for da in data1:
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
    for da3 in data2:
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
    for da3 in data3:
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