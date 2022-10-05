from fpdf import FPDF

async def surat_keterangan_tidak_mampu(pdf:FPDF, data:dict):
    #Add margin,page,and title surat
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=7 ,align="C",border=0,txt="SURAT KETERANGAN TIDAK MAMPU",ln=1)
    
    no_surat_keterangan_tidak_mampu = str(data.get("nomor_surat")) # Can be replace with no_keterangan_tidak_mampu in database

    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_surat_keterangan_tidak_mampu)
    pdf.set_text_color(0,0,0)
    pdf.ln(13)
    pdf.set_font("arial","",9)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\tYang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa :",ln=1)
    pdf.ln(3)

    data1 = [{
        "Nama": data.get("nama_lengkap"),
        "NIK" : data.get("nik"),
        "Jenis Kelamin" : data.get("jenis_kelamin"),
        "Tempat, tanggal Lahir": str(data.get('tempat_lahir')) + ", " + str(data.get("tanggal_lahir")),
        "Kewerganegaraan" : data.get("kewarganegaraan"),
        "Agama" : data.get("agama"),
        "Pekerjaan" : data.get("pekerjaan"),
        "Status Pernikahan" : data.get("status_perkawinan"),
        "Alamat Asal" : data.get("alamat")
        
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
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\tNama tersebut diatas adalah benar warga desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung. Berdasarkan keterangan yang ada pada kami benar bahwa yang bersangkutan tergolong keluarga yang tidak mampu.",ln=1)
    pdf.ln(3)

    pdf.set_font("arial","",9.5)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\tDemikian surat keterangan ini dibuat, atas perhatian dan kerjasamanya kami ucapkan terimakasih.",ln=1)
    pdf.ln(8)