from fpdf import FPDF

async def surat_keterangan_kelakuan_baik(pdf:FPDF, data:dict):
    #Add margin,page,and title surat
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=7 ,align="C",border=0,txt="SURAT KETERANGAN KELAKUAN BAIK",ln=1)
    
    no_surat_keterangan_kelakuan_baik = str(data.get("nomor_surat")) # Can be replace with no_keterangan_usaha in database

    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_surat_keterangan_kelakuan_baik)
    pdf.set_text_color(0,0,0)
    pdf.ln(13)
    pdf.set_font("arial","",9)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\tYang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa :",ln=1)
    pdf.ln(3)

    data1 = [{
        "Nama": data.get("nama_lengkap"),
        "NIK" : data.get("nik"),
        "Jenis Kelamin" : data.get("jenis_kelamin"),
        "Tempat, tanggal Lahir": str(data.get('tempat_lahir')) + ", " + str(data.get("tanggal_lahir")) ,
        "Agama" : data.get("agama"),
        "Pekerjaan" : data.get("pekerjaan"),
        "Status Perkawinan" : data.get("status_perkawinan"),
        "Alamat" : data.get("alamat")
        
    }]

    for da in data1:
        for key, val in da.items():
                    pdf.cell(8,8,border=0,align="R")
                    pdf.cell(5,8,border=0)
                    pdf.cell(50,8,border=0,align="L",txt=key)
                    pdf.cell(3,8,border=0,align="L", txt=":")
                    pdf.multi_cell(77,8,border=0,align="L",txt=str(val),ln=1)

    pdf.ln(3)
    pdf.set_font("arial","",9.5)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\tBenar yang Namanya tersebut diatas adalah Penduduk Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung dan sepanjang pengetahuan kami hingga dikeluarkan surat keterangan ini yang bersangkutan dinyatakan:",ln=1)
    pdf.ln(3)

    point = ["Berkelakuan baik dan tidak pernah terlibat tindak kriminal","Tidak termasuk pecandu narkotika dan minuman keras","Tidak pernah terlibat tindak pidana maupun perdata"]
    alpha = ["a","b","c"]
    for i in range(3):
        pdf.cell(8,5,border=0,align="R")
        pdf.cell(5,5,border=0)
        pdf.cell(4,5,border=0,align="L",txt=f"{alpha[i]}")
        pdf.cell(3,5,border=0)
        pdf.multi_cell(130,5,border=0,align="L",txt=str(point[i]),ln=1)
    
    pdf.ln(3)
    pdf.set_font("arial","",9.5)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\tSurat Keterangan ini dikeluarkan sebagai kelengkapan persyaratan administrasi.",ln=1)

    pdf.ln(3)
    pdf.set_font("arial","",9.5)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\tDemikian surat keterangan ini dibuat dengan sebenarnya dan untuk dapat dipergunakan seperlunya.",ln=1)
    pdf.ln(3)