from fpdf import FPDF
 
pdf = FPDF(orientation="P", format="A4")
pdf.set_margins(30, 30)
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


pdf.set_margins(25, 25)
pdf.ln(10)
pdf.set_font("arial","BU",10)
pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT PENGANTAR NIKAH",ln=1)

no_nikah = "202/0013/TR/1/2021"
pdf.set_font("arial","",10)
pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
pdf.set_text_color(255,0,0)
pdf.cell(90,h=8 ,align="L",border=0,txt=no_nikah)


pdf.set_text_color(0,0,0)

pdf.ln(10)
pdf.set_font("arial","",10)
pdf.multi_cell(0,h=4 ,align="L",border=0,txt="\t\t\t\t\t\t\t\t\tYang bertanda tangan di bawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sesungguhnya bahwa:",ln=1)

pdf.ln(3)

data = [{
    "Nama Lengkap": "Ibnu Muhammad Arbain",
    "Tempat, Tanggal Lahir" : "Samarinda, 14 Maret 1989",
    "Jenis Kelamin" : "Laki-Laki",
    "Agama": "Islam",
    "Pekerjaan" : "Wiraswasta",
    "Status" : "Belum Kawin",
    "Dusun" : "Dusun Sukamaju",
    "Adalah anak kandung dari":""
}]

data2 = [{
    "Nama Lengkap": "Muhammad Sahid",
    "Tempat, Tanggal Lahir" : "Nganjuk, 31 Desember 1954",
    "Agama": "Islam",
    "Pekerjaan" : "Karyawan Swasta",
    "Alamat" : "Jl. Niaga Baru no 24",

}]

data3 = [{
    "Nama Lengkap": "Sukini",
    "Tempat, Tanggal Lahir" : "Kediri, 05 September 1955",
    "Agama": "Islam",
    "Pekerjaan" : "Ibu Rumah Tangga",
    "Alamat" : "Jl. Niaga Baru no 24",

}]

for da in data:
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

for da3 in data3:
    for key, val in da3.items():
            pdf.cell(25,5,border=0,align="R",txt="")
            pdf.cell(5,5,border=0)
            pdf.cell(50,5,border=0,align="L",txt=key)
            pdf.cell(3,5,border=0,align="L", txt=":")
            pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)
            

pdf.cell(25,5,border=0,align="R",txt="III.")
pdf.cell(5,5,border=0)
pdf.cell(50,5,border=0,align="L",txt="IBU",ln=1)

for da2 in data2:
    for key, val in da2.items():
            pdf.cell(25,5,border=0,align="R",txt="")
            pdf.cell(5,5,border=0)
            pdf.cell(50,5,border=0,align="L",txt=key)
            pdf.cell(3,5,border=0,align="L", txt=":")
            pdf.multi_cell(77,5,border=0,align="L",txt=str(val),ln=1)
            
pdf.ln(3)
pdf.set_font("arial","",10)
pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""\t\t\t\t\t\t\t\t\tPemilik nama tersebut di atas adalah benar warga kami Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung dan sepengatuhan kami yang bersangkutan berkelakuan baik. Surat keterangan pengantar ini diberikan untuk keperluan pengurusan surat nikah.""",ln=1)

pdf.ln(3)
pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""\t\t\t\t\t\t\t\t\tDemikian surat keterangan ini dibuat dengan sebenarnya dan diberikan untuk dapat 
dipergunakan sebagaimana mestinya.""",ln=1)


pdf.set_x(125)
# pdf.cell(100,h=8 ,align="L", border=0)
pdf.multi_cell(60,h=4 ,align="C", border=0, txt="CIKONENG, 19 September 2022",ln=1)
# pdf.cell(100,h=7 ,align="L", border=0)
pdf.set_x(125)
pdf.multi_cell(60,h=4 ,align="C", border=0, txt="KEPALA DESA CIKONENG",ln=1)

pdf.cell(0,h=15 ,align="L", border=0,ln=1)
# pdf.cell(100,h=8 ,align="L", border=0)
pdf.set_x(125)
pdf.multi_cell(60,h=4 ,align="C", border=0, txt="Mustahiq, S.Adm",ln=1)
# pdf.cell(100,h=7 ,align="L", border=0)
pdf.set_x(125)
pdf.multi_cell(60,h=4 ,align="C", border=0, txt="NIP : 1918718001902981920",ln=1)





        
    
    
    



pdf.output("template.pdf")