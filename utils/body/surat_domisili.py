from fpdf import FPDF



async def surat_domisili(pdf:FPDF,data:dict):
    
    
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN DOMISILI",ln=1)
    no_nikah = data.get("nomor_surat") # Can be replace with no nikah in database 
    
    pdf.set_font("arial","",13)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_nikah)
    
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Yang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa :""",ln=1)
    pdf.ln(5)
    
    
    #receive data from database
    data_diri = [{
        "Nama":data.get('nama_pembuat_surat'),
        "Jenis Kelamin":data.get("jenis_kelamin_pembuat_surat"),
        "Tempat, Tanggal Lahir":data.get("tempat_tanggal_lahir_pembuat_surat"),
        "Agama":data.get("agama_pembuat_surat"),
        "Pekerjaan":data.get("pekerjaan_pembuat_surat"),
        "Status Perkawinan":data.get("status_perkawinan_pembuat_surat"),
        "Alamat" : data.get("alamat_pembuat_surat"),
    }]
    
    #looping through list of dict
    for datdir in data_diri:
        for key, val in datdir.items():
            pdf.cell(10,8,border=0)
            pdf.cell(50,8,border=0,align="L",txt=key)
            pdf.cell(3,8,border=0,align="L", txt=":")
            pdf.multi_cell(97,8,border=0,align="L",ln=1,txt=str(val))
    
        
    pdf.ln(5)
    dusun = "Dusun Sukamaju RT 11 RW 001"
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt=f"""Dengan ini menerangkan bahwa benar yang bersangkuta berdomisili di {dusun}, Surat keterangan ini dibuat untuk keperluan bekerja.""",ln=1)
    pdf.ln(3)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Demikian surat keterangan ini dibuat, atas perhatian dan kerjasamanya kami ucapkan terimakasih.""",ln=1)
    pdf.ln(5)
 