from fpdf import FPDF

async def surat_pindah(pdf:FPDF,data:dict):
    

    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN PINDAH",ln=1)

    no_surat_pindah = data.get("umum").get("nomor_surat") # Can be replace with no nikah in database 
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_surat_pindah)
    pdf.set_text_color(0,0,0)
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="Yang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandungmenerangkan dengan sebenarnya, bahwa :",ln=1)
    pdf.ln(3)
    
    tempat_tanggal_lahir = data.get("umum").get("tempat_lahir") + ", " + data.get("umum").get("tanggal_lahir")
    pengikut = data.get("pengikut")
    
    if type(pengikut) == list:
        len_pengikut = str(len(pengikut)) + " ORANG"
    elif type(pengikut) == dict:
        len_pengikut = "1 ORANG"

    

    pindah = [{
        "Nama":"" if not data.get("umum").get("nama") else data.get("umum").get("nama"),
        "NIK":"" if not data.get("umum").get("nik") else data.get("umum").get("nik"),
        "Jenis Kelamin":"" if not data.get("umum").get("jenis_kelamin") else data.get("umum").get("jenis_kelamin"),
        "Tempat, Tanggal Lahir":"" if not tempat_tanggal_lahir else tempat_tanggal_lahir,
        "Agama":"" if not data.get("umum").get("agama") else data.get("umum").get("agama"),
        "Pekerjaan":"" if not data.get("umum").get("pekerjaan") else data.get("umum").get("pekerjaan"),
        "Status Pernikahan":"" if not data.get("umum").get("status_perkawinan") else data.get("umum").get("status_perkawinan"),
        "Pendidikan":"" if not data.get("umum").get("pendidikan_terakhir") else data.get("umum").get("pendidikan_terakhir"),
        "Alamat Asal":"" if not data.get("umum").get("alamat_asal") else data.get("umum").get("alamat_asal"),
        "Nomor KK":"" if not data.get("umum").get("nomor_kk") else data.get("umum").get("nomor_kk"),
        "Alamat Tujuan Pindah":"" if not data.get("pindah_ke").get("alamat_pindah") else data.get("pindah_ke").get("alamat_pindah"),
        "Pengikut/Keluarga Yang Pindah":"" if not len_pengikut else len_pengikut,
    }]
    
    p = data.get("pengikut")
    
    
    for i in pindah:
        for key,val in i.items():
            pdf.cell(10,6,border=0)
            pdf.cell(55,6,border=0,align="L",txt=key)
            pdf.cell(3,6,border=0,align="L", txt=":")
            pdf.multi_cell(93,6,border=0,align="L",txt=str(val),ln=1)
    
    if len(pengikut) > 0:         
        pdf.ln(1)
        pdf.cell(10,6,border=1,txt="NO",align="C")
        pdf.cell(55,6,border=1,txt="NIK",align="C")
        pdf.multi_cell(96,6,border=1,txt="NAMA LENGKAP",ln=1,align="C")

        if type(p) == list:
            for nu,i in enumerate(p):
                pdf.cell(10,6,border=1,txt=str(nu + 1),align="C")
                pdf.cell(55,6,border=1,txt=str(i.get("nik")),align="C")
                pdf.multi_cell(96,6,border=1,txt=i.get("nama_lengkap"),ln=1,align="C")
        elif type(p) == dict:
            pdf.cell(10,6,border=1,txt=str(1),align="C")
            pdf.cell(55,6,border=1,txt=str(p.get("nik")),align="C")
            pdf.multi_cell(96,6,border=1,txt=p.get("nama_lengkap"),ln=1,align="C")
    
    pdf.ln(4)
    pdf.set_font("arial","",11)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Demikian surat keterangan ini dibuat dengan sebenarnya dan diberikan untuk dapat dipergunakan sebagaimana mestinya.""",ln=1)   
    
    
