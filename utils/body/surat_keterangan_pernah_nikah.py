from fpdf import FPDF


async def surat_keterangan_pernah_nikah(pdf:FPDF,data:dict):

    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN PERNAH NIKAH",ln=1)

    no_surat = data.get("umum").get("nomor_surat") # Can be replace with no nikah in database 
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_surat)
    pdf.set_text_color(0,0,0)
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="Yang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa :",ln=1)
    pdf.ln(3)
    
    tempat_tanggal_lahir_suami = str(data.get("umum").get("tempat_lahir")) + ", " + str(data.get("umum").get("tanggal_lahir"))
    
    data_suami = [{
        "Nama" :data.get("umum").get("nama") if not data.get("umum").get("nama_lengkap") else data.get("umum").get("nama_lengkap"),
        "NIK" :data.get("umum").get("NIK") if not data.get("umum").get("nik") else data.get("umum").get("nik"),
        "Jenis Kelamin" :data.get("umum").get("jenis_kelamin"),
        "Tempat, Tanggal Lahir":tempat_tanggal_lahir_suami,
        "Agama" :data.get("umum").get("agama"),
        "Pekerjaan" :data.get("umum").get("pekerjaan"),
        "Alamat" :data.get("umum").get("alamat"),
    }]
    
    tempat_tanggal_lahir_istri = str(data.get("umum").get("tempat_lahir")) + ", " + str(data.get("umum").get("tanggal_lahir"))
    
    data_istri = [{
        "Nama" :data.get("pasangan").get("nama_pasangan"),
        "NIK" :data.get("pasangan").get("NIK") if not data.get("pasangan").get("nik_pasangan") else data.get("pasangan").get("nik_pasangan"),
        "Jenis Kelamin" :data.get("pasangan").get("jenis_kelamin"),
        "Tempat, Tanggal Lahir":tempat_tanggal_lahir_istri,
        "Agama" :data.get("pasangan").get("agama"),
        "Pekerjaan" :data.get("pasangan").get("pekerjaan"),
        "Alamat" :data.get("pasangan").get("alamat"),
    }]
    
    pdf.cell(20,7,border=0,txt="1.",align="R")
    pdf.cell(50,7,border=0,txt="Data Suami")
    pdf.cell(3,7,border=0)
    pdf.cell(87,7,border=0,ln=1)
    
    for suami in data_suami:
        for key,val in suami.items():
            pdf.cell(20,7,border=0)
            pdf.cell(50,7,border=0,txt=key)
            pdf.cell(3,7,border=0,txt=":")
            pdf.cell(87,7,border=0,txt=val,ln=1)
            
    pdf.cell(20,7,border=0,txt="2.",align="R")
    pdf.cell(50,7,border=0,txt="Data Istri")
    pdf.cell(3,7,border=0)
    pdf.cell(87,7,border=0,ln=1)
    
    for istri in data_istri:
        for key,val in istri.items():
            pdf.cell(20,7,border=0)
            pdf.cell(50,7,border=0,txt=key)
            pdf.cell(3,7,border=0,txt=":")
            pdf.cell(87,7,border=0,txt=val,ln=1)
    
    
    
   
    tanggal = str(data.get("perkawinan").get("tanggal_perkawinan"))   
    
    pdf.ln(4)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt=f"""Adalah benar telah menikah secara agama islam di Kepala Desa Cikoneng, Kecamatan Ciparay,
Kabupaten Bandung pada tanggal {tanggal} yang dilakukan oleh Pemuka Agama/Penghulu Desa
Cikoneng.""",ln=1)
    
    keperluan = data.get("perkawinan").get("keperluan")
    pdf.ln(4)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt=f"""Demikian Surat Keterangan Nikah ini dibuat dan hanya berlaku untuk keperluan {keperluan}""",ln=1)   