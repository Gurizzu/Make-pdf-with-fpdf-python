from fpdf import FPDF

async def surat_keterangan_penghasilan_orang_tua(pdf:FPDF,data:dict):
    
    
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN PENGHASILAN ORANGTUA",ln=1)

    no_surat = str(data.get("pemohon").get("nomor_surat")) # Can be replace with no surat in database 
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_surat)
    pdf.set_text_color(0,0,0)
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="Yang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandungmenerangkan dengan sebenarnya, bahwa :",ln=1)
    pdf.ln(3)
    
    #tempat_tanggal_lahir
    tempat_tgl_pemohon = data.get("pemohon").get("tempat_lahir") + ", " + data.get("pemohon").get("tanggal_lahir")
    
    data_pemohon = [{
        "Nama":data.get("pemohon").get("nama_lengkap"),
        "NIK":data.get("pemohon").get("nik"),
        "Tempat, Tanggal Lahir" : tempat_tgl_pemohon,
        "Pekerjaan":data.get("pemohon").get("pekerjaan"),
        "Alamat Asal":data.get("pemohon").get("alamat"),
    }]
    
    tempat_tgl_ortu = data.get("ayah").get("tempat_lahir") + ", " + data.get("ayah").get("tanggal_lahir")
    
    data_orang_tua = [{
        "Nama":data.get("ayah").get("nama_lengkap"),
        "NIK":"" if not data.get("ayah").get("nik") else data.get("ayah").get("nik"),
        "Jenis Kelamin":"" if not data.get("ayah").get("jenis_kelamin") else data.get("ayah").get("jenis_kelamin"),
        "Tempat, Tanggal Lahir" : tempat_tgl_ortu,
        "Pekerjaan":data.get("ayah").get("pekerjaan"),
        "Alamat Asal":data.get("ayah").get("alamat"),
    }]
    
    for pemohon in data_pemohon:
        for key,val in pemohon.items():      
            pdf.cell(10,7,border=0)
            pdf.cell(60,7,border=0,txt=key)
            pdf.cell(3,7,border=0,txt=":")
            pdf.cell(87,7,border=0,txt=val,ln=1)
            
    pdf.cell(0,7,border=0,txt="Adalah Orang Tua / Wali dari:",align="L",ln=1)
    
    for ortu in data_orang_tua:
        for key,val in ortu.items():      
            pdf.cell(10,7,border=0)
            pdf.cell(60,7,border=0,txt=key)
            pdf.cell(3,7,border=0,txt=":")
            pdf.cell(87,7,border=0,txt=val,ln=1)
    
    keperluan = data.get("pemohon").get("keperluan")        
    
    pdf.ln(4)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt=f"Dengan ini menyatakan bahwa yang bersangkutan diatas memang benar berpenghasilan kurang lebih perbulan. Surat Keterangan ini dibuat untuk {keperluan}",ln=1)
    
    
    pdf.ln(4)
    pdf.set_font("arial","",11)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Demikian surat keterangan ini dibuat dengan sebenarnya dan diberikan untuk dapat dipergunakan sebagaimana mestinya.""",ln=1)   