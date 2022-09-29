from fpdf import FPDF
 
pdf = FPDF(orientation="P", format="A4")


class Body():
    def surat_nikah():
        
        data_diri = ["Nama Lengkap","Tempat, Tanggal Lahir", "Jenis Kelamin", "Agama", "Pekerjaan", "Status", "Dusun", "Adalah anak kandung dari"]
        data_orang_tua = ["Nama Lengkap","Tempat, Tanggal Lahir", "Agama", "Pekerjaan", "Alamat"]
        
        
        pdf.set_margins(25, 25)
        pdf.ln(5)
        pdf.set_font("arial","BU",10)
        pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT PENGANTAR NIKAH",ln=1)

        no_nikah = "202/0013/TR/1/2021" # Can be replace with no nikah in database 
        pdf.set_font("arial","",10)
        pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
        pdf.set_text_color(255,0,0)
        pdf.cell(90,h=8 ,align="L",border=0,txt=no_nikah)


        pdf.set_text_color(0,0,0)

        pdf.ln(10)
        pdf.set_font("arial","",10)
        pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\t\tYang bertanda tangan di bawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sesungguhnya bahwa:",ln=1)

        pdf.ln(3)
        
        
        for datdir in data_diri:
            if datdir == "Nama Lengkap":
                pdf.cell(25,5,border=0,align="R",txt="I.")
                pdf.cell(5,5,border=0)
                pdf.cell(50,5,border=0,align="L",txt=datdir)
                pdf.cell(3,5,border=0,align="L", txt=":")
                pdf.multi_cell(77,5,border=0,align="L",txt="Muhamad Yusuf Rifqi Nurfadillah",ln=1)    
            else:
                pdf.cell(25,5,border=0,align="R")
                pdf.cell(5,5,border=0)
                pdf.cell(50,5,border=0,align="L",txt=datdir)
                pdf.cell(3,5,border=0,align="L", txt=":")
                pdf.multi_cell(77,5,border=0,align="L",txt="contoh",ln=1)
        
        pdf.cell(25,5,border=0,align="R",txt="II.")
        pdf.cell(5,5,border=0)
        pdf.cell(50,5,border=0,align="L",txt="AYAH",ln=1) 
        
        for dartu in data_orang_tua:
            pdf.cell(25,5,border=0,align="R",txt="")
            pdf.cell(5,5,border=0)
            pdf.cell(50,5,border=0,align="L",txt=dartu)
            pdf.cell(3,5,border=0,align="L", txt=":")
            pdf.multi_cell(77,5,border=0,align="L",txt="contoh",ln=1)  
            
        pdf.cell(25,5,border=0,align="R",txt="III.")
        pdf.cell(5,5,border=0)
        pdf.cell(50,5,border=0,align="L",txt="IBU",ln=1)
        
        for dartu in data_orang_tua:
            pdf.cell(25,5,border=0,align="R",txt="")
            pdf.cell(5,5,border=0)
            pdf.cell(50,5,border=0,align="L",txt=dartu)
            pdf.cell(3,5,border=0,align="L", txt=":")
            pdf.multi_cell(77,5,border=0,align="L",txt="contoh",ln=1)                 
            
        pdf.ln(3)
        pdf.set_font("arial","",10)
        pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""\t\t\t\t\t\t\t\t\tPemilik nama tersebut di atas adalah benar warga kami Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung dan sepengatuhan kami yang bersangkutan berkelakuan baik. Surat keterangan pengantar ini diberikan untuk keperluan pengurusan surat nikah.""",ln=1)

        pdf.ln(3)
        pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""\t\t\t\t\t\t\t\t\tDemikian surat keterangan ini dibuat dengan sebenarnya dan diberikan untuk dapat 
        dipergunakan sebagaimana mestinya.""",ln=1)        
        
    
    def surat_domisili():
        
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
    
    
    
def footer2():
    pdf.set_font("arial","",10)
    pdf.ln(2)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt="CIKONENG, 19 September 2022",ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt="KEPALA DESA CIKONENG",ln=1)

    pdf.cell(0,h=17 ,align="L", border=0,ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt="Mustahiq, S.Adm",ln=1)
    # pdf.ln(5)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt="NIP : 1918718001902981920",ln=1)


def opsi(surat: int,output:str):
    """
    surat:  input must be integer
            (1) for surat domisili 
            (2) for surat nikah 
            (3) for surat kematian
            
    output: input must be string, input will be output name of pdf files
            
    """
    if surat >3:
        raise ValueError("first param must be greater than 3")
    elif surat <=0:
        raise ValueError("first param must be greater than 0")
    else:
        if surat == 1:
            pdf.set_margins(27, 27)
            pdf.add_page()
            header()
            Body.surat_domisili()
            footer2()
        elif surat == 2:
            pdf.set_margins(27, 27)
            pdf.add_page()
            header()
            Body.surat_nikah()
            footer2()
        elif surat == 3:
            pdf.set_margins(27, 27)
            pdf.add_page()
            header()
            Body.surat_keterangan_kematian()
            footer2()      
        pdf.output(f"{output}.pdf")
    
    
opsi(2,"nikah")
