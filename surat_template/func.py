from fpdf import FPDF
 
pdf = FPDF(orientation="P", format="A4")


def surat_nikah(data:dict):
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
        
    
def surat_domisili(data:dict):
    
    data_diri = ["Nama","NIK", "Jenis Kelamin", "Tempat, Tanggal Lahir", "Agama", "Pekerjaan", "Status Perkawinan", "Alamat"]
    
    
    pdf.set_margins(25, 25)
    pdf.ln(5)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN DOMISILI",ln=1)
    no_nikah = "202/0013/TR/1/2021" # Can be replace with no nikah in database 
    
    pdf.set_font("arial","",13)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.cell(90,h=8 ,align="L",border=0,txt=no_nikah)
    
    pdf.ln(10)
    pdf.set_font("arial","",10)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Yang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa :""",ln=1)
    pdf.ln(5)
    
    for datdir in data_diri:
        pdf.cell(10,8,border=0)
        pdf.cell(50,8,border=0,align="L",txt=datdir)
        pdf.cell(3,8,border=0,align="L", txt=":")
        pdf.multi_cell(97,8,border=0,align="L",ln=1,txt="Contoh")
        
    pdf.ln(5)
    dusun = "Dusun Sukamaju RT 11 RW 001"
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt=f"""Dengan ini menerangkan bahwa benar yang bersangkuta berdomisili di {dusun}, Surat keterangan ini dibuat untuk keperluan bekerja.""",ln=1)
    pdf.ln(3)
    pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Demikian surat keterangan ini dibuat, atas perhatian dan kerjasamanya kami ucapkan terimakasih.""",ln=1)
    pdf.ln(5)
    
def surat_keterangan_kematian():
    
    data_orang_meninggal = ["Nama","Tempat, Tanggal Lahir", "Jenis Kelamin","Alamat", "Agama", "Status Perkawinan", "Pekerjaan", "Kewarganegaraan", "NIK"]
    waktu = ["Tanggal" , "Pukul/Jam" , "Bertempat di" , "Penyebab Kematian"]
    pelapor = ["Nama" , "Jenis Kelamin" , "Alamat" , "Hubungan Dengan Alm/Almh"]
    
    pdf.ln(1)
    pdf.set_font("arial","BU",10)
    pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN KEMATIAN",ln=1)
    
    no_nikah = "202/0013/TR/1/2021" # Can be replace with no nikah in database 
    
    pdf.set_font("arial","",10)
    pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
    pdf.cell(80,h=8 ,align="L",border=0,txt=no_nikah)
    
    pdf.set_font("arial","",8)
    pdf.set_margins(27, 27)
    pdf.ln(5)
    pdf.cell(0,h=8 ,align="L",border=0,ln=1,txt="Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung, dengan ini menerangkan bahwa :")
    pdf.ln(2)
    
    pdf.set_margins(25, 25)
    
    pulan = "Pulan" #Placeholder for database
    
    for datorgal in data_orang_meninggal:
        if datorgal == "Nama":
            pdf.cell(50,h=6,border=0,align="L",txt=datorgal)
            pdf.cell(3,6,border=0,align="L", txt=":")
            pdf.multi_cell(107,h=6,border=0,align="L",txt=f"Contoh bin {pulan}",ln=1)
        else:
            pdf.cell(50,h=6,border=0,align="L",txt=datorgal)
            pdf.cell(3,6,border=0,align="L", txt=":")
            pdf.multi_cell(107,h=6,border=0,align="L",txt="Contoh",ln=1)
    
    
    pdf.ln(1)
    # Some Text
    pdf.cell(txt='            Orang tersebut diatas benar' , border=0)
    pdf.set_font(family='arial', style="B" , size=8)
    pdf.cell(txt="Meninggal Dunia", border=0)
    pdf.set_font(family='arial', style="" , size=8)
    pdf.cell(txt="pada :", border=0 , ln=True)
    pdf.ln(1)
    # Second Form In Surat Kematian
    for wak in waktu:
        pdf.cell(50,6, align="L", border=0, txt=wak)
        pdf.cell(3,6,border=0, align="R" ,txt=":")
        pdf.multi_cell(0,6, align="L", border=0, ln=1, txt="Contoh")
    pdf.ln(1)
    # Some Text
    pdf.multi_cell(0,h=3,align="L", txt='            Surat keterangan ini di buat berdasarkan laporan dari :', ln=True)
    pdf.ln(1)
    # Third Form in Surat Kematina
    for pel in pelapor:
        pdf.cell(50,6, align="L", border=0, txt=pel)
        pdf.cell(3,6,border=0, align="R" ,txt=":")
        pdf.multi_cell(0,6, align="L", border=0, ln=1, txt="Contoh")
    pdf.ln(1)
    # Surat Kematia Footer
    pdf.multi_cell(0,h=3,align="L", txt='            Demikian surat keterangan ini kami buat, untuk dipergunakan sebagaimana mestinya.', ln=True)
    pdf.ln(1)
                
    
def header():
    pdf.set_margins(27, 27)
    pdf.add_page()
    
    pdf.set_font("times","B",15)
    pdf.image("kab_bandung.png",w=30, h = 25, x=30, y=33)
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


    
def footer2(data:dict):
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
    
    
def run_nikah(foot:dict,data:dict,output:str):
    header()
    surat_nikah(data)
    footer2(foot)
    pdf.output(f"{output}.pdf")
    
    

