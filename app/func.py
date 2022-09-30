from fpdf import FPDF


async def header(pdf:FPDF):
    pdf.set_margins(27, 27)
    pdf.add_page()
    
    pdf.set_font("times","B",15)
    pdf.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Lambang_Kabupaten_Bandung%2C_Jawa_Barat%2C_Indonesia.svg/2458px-Lambang_Kabupaten_Bandung%2C_Jawa_Barat%2C_Indonesia.svg.png",w=30, h = 25, x=30, y=33)
    pdf.set_x(60)
    pdf.multi_cell(0, h=10 ,align="C",border=0,txt="PEMERINTAH KABUPATEN BANDUNG",ln=1)
    pdf.set_font("times","",14)
    pdf.set_x(60)
    pdf.multi_cell(0,align="C",border=0,txt="KECAMATAN CIPARAY",ln=1)
    pdf.ln(1)
    pdf.set_font("times","",14)
    pdf.set_x(60)
    pdf.multi_cell(0,align="C",border=0,txt="DESA CIKONENG",ln=1)
    pdf.ln(3)
    pdf.set_font("times","",12)
    pdf.set_x(60)
    pdf.multi_cell(0,align="C",border=0,txt="Jl.Raya Pacet Km 4.6 Medal Laksana RT. 02/09 Kec. Ciparay Kab.Bandung",ln=1)
    pdf.ln(5)
    pdf.set_fill_color(0,0,0)
    pdf.cell(0,0.5,border=0, fill=1)

async def footer2(pdf:FPDF,data:dict):
    pdf.set_font("arial","",10)
    pdf.ln(2)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt="CIKONENG, 19 September 2022",ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt="KEPALA DESA CIKONENG",ln=1)

    pdf.cell(0,h=17 ,align="L", border=0,ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt=data.get("penanda_tangan_surat"),ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt=data.get("nip_penandatangan_surat"),ln=1)

async def surat_nikah(pdf:FPDF,data:dict):
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT PENGANTAR NIKAH",ln=1)
    
    no_nikah = data.get("nomor_surat") # Can be replace with no nikah in database 
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.set_text_color(255,0,0)
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_nikah)
    pdf.set_text_color(0,0,0)
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\t\tYang bertanda tangan di bawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sesungguhnya bahwa:",ln=1)
    pdf.ln(3)
    
    data1 = [{
        "Nama Lengkap": data.get("nama_mempelai"),
        "Tempat, Tanggal Lahir" : data.get("tempat_tanggal_lahir_mempelai"),
        "Jenis Kelamin" : data.get("jenis_kelamin_mempelai"),
        "Agama": data.get('agama_mempelai'),
        "Pekerjaan" : data.get("pekerjaan_mempelai"),
        "Status" : data.get("status_mempelai"),
        "Dusun" : data.get("dusun_mempelai"),
        
    }]
    data2 = [{
        "Nama Lengkap": data.get("nama_ayah_mempelai"),
        "Tempat, Tanggal Lahir" : data.get("tempat_tanggal_lahir_ayah_mempelai"),
        "Agama": data.get("agama_ayah_mempelai"),
        "Pekerjaan" : data.get("pekerjaan_ayah_mempelai"),
        "Alamat" : data.get("alamat_ayah_mempelai"),
    }]
    data3 = [{
        "Nama Lengkap": data.get("nama_ibu_mempelai"),
        "Tempat, Tanggal Lahir" : data.get("tempat_tanggal_lahir_ibu_mempelai"),
        "Agama": data.get("agama_ibu_mempelai"),
        "Pekerjaan" : data.get("pekerjaan_ibu_mempelai"),
        "Alamat" : data.get("alamat_ibu_mempelai"),
    }]
    for da in data1:
        for key, val in da.items():
                if key =='Nama Lengkap':
                    pdf.cell(25,5,border=0,align="R",txt="I.")
                    pdf.cell(5,5,border=0)
                    pdf.cell(50,5,border=0,align="L",txt=key)
                    pdf.cell(3,5,border=0,align="L", txt=":")
                    pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)
                else:
                    pdf.cell(25,5,border=0,align="R")
                    pdf.cell(5,5,border=0)
                    pdf.cell(50,5,border=0,align="L",txt=key)
                    pdf.cell(3,5,border=0,align="L", txt=":")
                    pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)
    
    pdf.cell(25,5,border=0,align="R",txt="II.")
    pdf.cell(5,5,border=0)
    pdf.cell(50,5,border=0,align="L",txt="AYAH",ln=1)
    for da3 in data2:
        for key, val in da3.items():
                pdf.cell(25,5,border=0,align="R",txt="")
                pdf.cell(5,5,border=0)
                pdf.cell(50,5,border=0,align="L",txt=key)
                pdf.cell(3,5,border=0,align="L", txt=":")
                pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)
    pdf.cell(25,5,border=0,align="R",txt="III.")
    pdf.cell(5,5,border=0)
    pdf.cell(50,5,border=0,align="L",txt="IBU",ln=1)
    for da3 in data3:
        for key, val in da3.items():
                pdf.cell(25,5,border=0,align="R",txt="")
                pdf.cell(5,5,border=0)
                pdf.cell(50,5,border=0,align="L",txt=key)
                pdf.cell(3,5,border=0,align="L", txt=":")
                pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)

async def set_nikah(fpdf:FPDF, data:dict, foot:dict , output:str):
    await header(pdf=fpdf)
    await surat_nikah(pdf=fpdf , data=data)
    await footer2(pdf=fpdf, data=foot)
    fpdf.output(f'{output}.pdf')