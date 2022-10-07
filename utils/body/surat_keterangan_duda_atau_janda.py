from fpdf import FPDF

async def surat_keterangan_duda_atau_janda(pdf:FPDF,data:dict):
   

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
    
    tempat_tanggal_lahir = data.get("umum").get("tempat_lahir") + ", " + data.get("umum").get("tanggal_lahir")
    
    data_dujan = [{
        "Nama" :data.get("umum").get("nama") if not data.get("umum").get("nama_lengkap") else data.get("umum").get("nama_lengkap"),
        "Jenis Kelamin" :data.get("umum").get("jenis_kelamin"),
        "Tempat, Tanggal Lahir":tempat_tanggal_lahir,
        "Agama" :data.get("umum").get("agama"),
        "Pekerjaan" :data.get("umum").get("pekerjaan"),
        "Alamat" :data.get("umum").get("alamat"),
    }]
    
    
    for dujan in data_dujan:
        for key,val in dujan.items():
            pdf.cell(20,7,border=0)
            pdf.cell(50,7,border=0,txt=key)
            pdf.cell(3,7,border=0,txt=":")
            pdf.cell(87,7,border=0,txt=val,ln=1)
            
    
    
    
   
    tanggal = data.get("perkawinan").get("tanggal_perkawinan")        
    
    pdf.ln(4)
    pdf.set_font("arial","",10)
    pdf.cell(0,h=4 ,align="L",border=0,txt=f"""Benar nama tersebut diatas menurut sepengetahuan kami adalah warga desa kami""",ln=1 )
    pdf.cell(40,h=4 ,align="L",border=0,txt=" yang berstatus seorang ")
    pdf.set_font("arial","B",10)
    pdf.cell(0,h=4,border=0,txt="DUDA / JANDA.",ln=1)
    
    pdf.ln(6)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt=f"""Demikian surat keterangan ini kami buat dengan sebenarnya, dan untuk dipergunakan sebagaimana mestinya.""",ln=1)   
    

    
