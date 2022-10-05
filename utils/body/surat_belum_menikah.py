from fpdf import FPDF
import datetime

async def surat_belum_nikah(pdf:FPDF,data:dict):

    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT PERNYATAAN BELUM MENIKAH",ln=1)

    no_surat_belum_menikah = data.get("nomor_surat") # Can be replace with no nikah in database 
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_surat_belum_menikah)
    pdf.set_text_color(0,0,0)
    pdf.ln(15)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="Yang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa :",ln=1)
    pdf.ln(3)
    
    tempat_tanggal_lahir = data.get("tempat_lahir") + ", " + data.get("tanggal_lahir")
    
    pindah = [{
        "Nama":"" if not data.get("nama_lengkap") else data.get("nama_lengkap"),
        "NIK":"" if not data.get("nik") else data.get("nik"),
        "Jenis Kelamin":"" if not data.get("jenis_kelamin") else data.get("jenis_kelamin"),
        "Tempat, Tanggal Lahir":"" if not tempat_tanggal_lahir else tempat_tanggal_lahir,
        "Kewarganegaraan":"" ,  #di database belum ada data kewarganegaraan
        "Agama":"" if not data.get("agama") else data.get("agama"),
        "Pekerjaan":"" if not data.get("pekerjaan") else data.get("pekerjaan"),
        "Status Pernikahan":"" if not data.get("status_perkawinan") else data.get("status_perkawinan"),
        "Alamat Asal":"" if not data.get("alamat_asal") else data.get("alamat_asal"),
    }]
    
    
    for i in pindah:
        for key,val in i.items():
            pdf.cell(10,7.5,border=0)
            pdf.cell(55,7.5,border=0,align="L",txt=key)
            pdf.cell(3,7.5,border=0,align="L", txt=":")
            pdf.multi_cell(93,7.5,border=0,align="L",txt=str(val),ln=1)
            
    pdf.ln(4)
    pdf.set_font("arial","",10)
    
    #converting created_at from database
    timestamp = str(data.get("created_at"))
    your_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)  # using the local timezone
    dt = your_dt.strftime("%Y-%m-%d %H:%M:%S").split()
    date = dt[0]
    
    keperluan = data.get("keperluan")
    
    
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt=f"""Nama tersebut diatas adalah benar warga Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung. Berdasarkan pernyataan yang bersangkutan Tanggal {date} dengan ini bahwa benar Belum Pernah Menikah dengan siapapun. Surat Keterangan ini dibuat untuk {keperluan}.""",ln=1)   
    pdf.ln(2)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Demikian surat keterangan ini dibuat, atas perhatian dan kerjasamanya kami ucapkan terimakasih.""",ln=1)
    pdf.ln(8)
    
    # italic description
    # pdf.set_font("arial","",10)
    # pdf.cell(0,h=4 ,align="L",border=1,txt=f"""Nama tersebut diatas adalah benar warga Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung.""",ln=1)
    # pdf.multi_cell(0,h=4 ,align="L",border=1,txt= f"Berdasarkan pernyataan yang bersangkutan Tanggal {date} dengan ini bahwa benar",ln=1) 
    # pdf.set_font("arial","I",10)
    # pdf.cell(68,4,border=1,align="L",txt="Belum Pernah Menikah dengan siapapun, ")
    # pdf.set_font("arial","",10)
    # pdf.multi_cell(0,4,border=1,align="L",txt=f"Surat Keterangan ini dibuat untuk {keperluan}.",ln=1)
    # pdf.set_font("arial","",10)
    # pdf.ln(2)
    # pdf.multi_cell(0,h=4 ,align="L",border=1,txt="""Demikian surat keterangan ini dibuat, atas perhatian dan kerjasamanya kami ucapkan terimakasih.""",ln=1)
    # pdf.ln(8)