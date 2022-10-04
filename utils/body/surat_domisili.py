from fpdf import FPDF



async def surat_domisili(pdf:FPDF,data:dict):
    
    
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN DOMISILI",ln=1)
    no_surat_domisili = data.get("nomor_surat") # Can be replace with no nikah in database 
    
    pdf.set_font("arial","",13)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_surat_domisili)
    
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Yang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa :""",ln=1)
    pdf.ln(5)
    
    
    #receive data from database
    data_diri = [{
        "Nama":data.get('nama'),
        "Jenis Kelamin":data.get("jenis_kelamin"),
        "Tempat, Tanggal Lahir": str(data.get("tempat_lahir")) + ", " + str(data.get("tanggal_lahir")),
        "Agama":data.get("agama"),
        "Pekerjaan":data.get("pekerjaan"),
        "Status Perkawinan":data.get("status_perkawinan"),
        "Alamat" : data.get("dusun"),
    }]
    
    #looping through list of dict
    for datdir in data_diri:
        for key, val in datdir.items():
            pdf.cell(10,8,border=0)
            pdf.cell(50,8,border=0,align="L",txt=key)
            pdf.cell(3,8,border=0,align="L", txt=":")
            pdf.multi_cell(97,8,border=0,align="L",ln=1,txt=str(val))
    
        
    pdf.ln(5)
    dusun = data.get("dusun")
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt=f"""Dengan ini menerangkan bahwa benar yang bersangkuta berdomisili di {dusun}, Surat keterangan ini dibuat untuk keperluan bekerja.""",ln=1)
    pdf.ln(3)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Demikian surat keterangan ini dibuat, atas perhatian dan kerjasamanya kami ucapkan terimakasih.""",ln=1)
    pdf.ln(5)
 