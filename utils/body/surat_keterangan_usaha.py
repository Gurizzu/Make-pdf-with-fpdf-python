from fpdf import FPDF

async def surat_keterangan_usaha(pdf:FPDF, data:dict):
    #Add margin,page,and title surat
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=7 ,align="C",border=0,txt="SURAT KETERANGAN USAHA",ln=1)
    
    no_surat_keterangan_usaha = str(data.get("nomor_surat")) # Can be replace with no nikah in database 
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=str(no_surat_keterangan_usaha))
    pdf.set_text_color(0,0,0)
    pdf.ln(13)
    pdf.set_font("arial","",9)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\t\tYang bertanda tangan di bawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa:",ln=1)
    pdf.ln(3)

    # Data From Data_Base
    data1 = [{
        "Nama": data.get("nama"),
        "NIK" : data.get("nik"),
        "Jenis Kelamin" : data.get("jenis_kelamin"),
        "Tempat, tanggal Lahir": str(data.get('tempat_lahir')) + ", " + (data.get('tanggal_lahir')),
        "Kewarganegaraan" : " " if not data.get("kewarganegaraan") else data.get("kewarganegaraan"),
        "Agama" : " " if not data.get("agama") else data.get("agama"),
        "Pekerjaan" : " " if not data.get("pekerjaan") else data.get("pekerjaan"),
        "Alamat Asal" : " " if not data.get("alamat") else data.get("alamat")
        
    }]
    data2 = [{
        "Nama Usaha": " " if not data.get("nama_usaha") else data.get("nama_usaha"),
        "Lama Usaha" : " " if not data.get("lama_usaha") else data.get("lama_usaha"),
        "Alamat Usaha": " " if not data.get("alamat_usaha") else data.get("alamat_usaha"),
        "Tujuan" : data.get("keperluan"),
    }]
    
    for da in data1:
        for key, val in da.items():
                    pdf.cell(8,8,border=0,align="R")
                    pdf.cell(5,8,border=0)
                    pdf.cell(50,8,border=0,align="L",txt=key)
                    pdf.cell(3,8,border=0,align="L", txt=":")
                    pdf.multi_cell(77,8,border=0,align="L",txt=str(val),ln=1)

    pdf.ln(2)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\t\tSesuai dengan keterangan yang bersangkutan benar nama tersebut diatas mempunyai usaha sebagai berikut :",ln=1)
    pdf.ln(2)

    for da in data2:
        for key, val in da.items():
                    pdf.cell(8,8,border=0,align="R")
                    pdf.cell(5,8,border=0)
                    pdf.cell(50,8,border=0,align="L",txt=key)
                    pdf.cell(3,8,border=0,align="L", txt=":")
                    pdf.multi_cell(77,8,border=0,align="L",txt=str(val),ln=1)

    pdf.ln(2)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\tDemikian surat keterangan ini dibuat untuk dipergunakan sebagaimana mestinya",ln=1)
    pdf.ln(8)