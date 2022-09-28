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
pdf.cell(0,h=8 ,align="C",border=0,txt="SURAT KETERANGAN DOMISILI",ln=1)

no_nikah = "202/0013/TR/1/2021"
pdf.set_font("arial","",10)
pdf.cell(70,h=8 ,align="R",border=0,txt="Nomor :")
pdf.set_text_color(255,0,0)
pdf.cell(90,h=8 ,align="L",border=0,txt=no_nikah)


data = [{
    "Nama": "ALEX NOERDIN",
    "NIK" : "3120910992820001",
    "Jenis Kelamin" : "LAKI-LAKI",  
    "Tempat, Tanggal Lahir" : "BANDUNG, 12-08-1992",
    "Agama": "ISLAM",
    "Pekerjaan" : "PEGAWAI NEGERI SIPIL",
    "Status Perkawinan" : "BELUM KAWIN",
    "Alamat" : "DUSUN SUKAMAJU, RT 11 RW 001",
}]
pdf.set_text_color(0,0,0)

pdf.ln(10)
pdf.set_font("arial","",10)
pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Yang bertanda tangan dibawah ini Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung menerangkan dengan sebenarnya, bahwa :""",ln=1)

pdf.ln(5)

for i in data:
    for key,val in i.items():  
        pdf.cell(10,8,border=0)
        pdf.cell(50,8,border=0,align="L",txt=key)
        pdf.cell(3,8,border=0,align="L", txt=":")
        pdf.multi_cell(97,8,border=0,align="L",ln=1,txt=str(val))
        
pdf.ln(5)
pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Dengan ini menerangkan bahwa benar yang bersangkuta berdomisili di Dusun Sukamaju RT 11 RW 
001, Surat keterangan ini dibuat untuk keperluan bekerja.""",ln=1)

pdf.ln(5)
pdf.multi_cell(0,h=4 ,align="L",border=0,txt="""Demikian surat keterangan ini dibuat, atas perhatian dan kerjasamanya kami ucapkan terimakasih.""",ln=1)

pdf.ln(10)
pdf.set_x(125)
pdf.multi_cell(60,h=4 ,align="C", border=0, txt="CIKONENG, 19 September 2022",ln=1)
pdf.set_x(125)
pdf.multi_cell(60,h=4 ,align="C", border=0, txt="KEPALA DESA CIKONENG",ln=1)

pdf.cell(0,h=15 ,align="L", border=0,ln=1)
pdf.set_x(125)
pdf.multi_cell(60,h=4 ,align="C", border=0, txt="Mustahiq, S.Adm",ln=1)
pdf.set_x(125)
pdf.multi_cell(60,h=4 ,align="C", border=0, txt="NIP : 1918718001902981920",ln=1)




pdf.output("template_domisili.pdf")