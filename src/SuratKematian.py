from fpdf import FPDF
 
pdf = FPDF(orientation="P", format="A4")

pdf.add_page()
pdf.set_margins(20,20)
pdf.set_font("helvetica","B",15)
pdf.image("kbb.jpg",w=30, h = 30 , x=20 , y=20)

# Surat Kematian Header
pdf.set_x(60)
pdf.multi_cell(0, h=6.5 ,align="C",border=0,txt="PEMERINTAH KABUPATEN BANDUNG",ln=1)
pdf.set_font("helvetica","",14)
pdf.set_x(60)
pdf.multi_cell(0, h=6.5 ,align="C",border=0,txt="KECAMATAN CIPARAY",ln=1)
pdf.set_x(60)
pdf.multi_cell(0, h=6.5 ,align="C",border=0,txt="DESA CIKONENG",ln=1)
pdf.set_x(60)
pdf.set_font("helvetica","",12)
pdf.multi_cell(0, h=6.5 ,align="C",border=0,txt="JL.Raya Pecet Km.4.6 Medal Laksana RT. 02/09 Kec.Ciparay Kab. Bandung",ln=1)
pdf.ln(8)
pdf.set_fill_color(0,0,0)
pdf.cell(0,1.5,border=0, fill=True)
pdf.ln(6)

# Surat Kematian Body
pdf.set_font(family='times', style="UB",size=12)
pdf.multi_cell(0,h=5,txt='SURAT KETERANGAN KEMATIAN',align="C", ln=True)
pdf.set_font(family='times', style="",size=12)
pdf.multi_cell(0,h=5,txt=f'Nomor : {"Nomor"}',align="C", ln=True)
pdf.set_font(family='times', style="",size=10)
pdf.ln(4)
pdf.multi_cell(0,h=5,align="C", txt='Kepala Desa Cikoneng, Kecamatan Ciparay, Kabupaten Bandung, dengan ini menerangkan bahwa :', ln=True)    

# Form In Surat Kematian
row1 = ["Nama" , "Tempat, Tanggal Lahir" , "Jenis Kelamin" , "Alamat" , "Agama" , "Status Perkawinan" , "Pekerjaan" , "Kewarganegaraan" , "NIK"]
row2 = ["Tanggal" , "Pukul/Jam" , "Bertempat di" , "Penyebab Kematian"]
row3 = ["Nama" , "Jenis Kelamin" , "Alamat" , "Hubungan Dengan Alm/Almh"]
for i in row1:
    pdf.cell(50,7, align="L", border=0, txt=i)
    pdf.cell(10,7,border=0, align="R" ,txt=":")
    pdf.multi_cell(0,7, align="L", border=0, ln=1, txt="Ega")

pdf.ln(1)
# Some Text
pdf.cell(txt='            Orang tersebut diatas benar' , border=0)
pdf.set_font(family='times', style="B" , size=10)
pdf.cell(txt="Meninggal Dunia", border=0)
pdf.set_font(family='times', style="" , size=10)
pdf.cell(txt="pada :", border=0 , ln=True)
pdf.ln(1)

# Second Form In Surat Kematian
for i in row2:
    pdf.cell(50,7, align="L", border=0, txt=i)
    pdf.cell(10,7,border=0, align="R" ,txt=":")
    pdf.multi_cell(0,7, align="L", border=0, ln=1, txt="Ega")
pdf.ln(1)

# Some Text
pdf.multi_cell(0,h=3,align="L", txt='            Surat keterangan ini di buat berdasarkan laporan dari :', ln=True)
pdf.ln(1)

# Third Form in Surat Kematina
for i in row3:
    pdf.cell(50,7, align="L", border=0, txt=i)
    pdf.cell(10,7,border=0, align="R" ,txt=":")
    pdf.multi_cell(0,7, align="L", border=0, ln=1, txt="Ega")
pdf.ln(1)
# Surat Kematia Footer
pdf.multi_cell(0,h=3,align="L", txt='            Demikian surat keterangan ini kami buat, untuk dipergunakan sebagaimana mestinya.', ln=True)
pdf.ln(5)
# Bertanda tangan

pdf.set_x(120)
pdf.multi_cell(0,h=4,align="C", txt='CIKONENG, 19 September 2022', ln=True)
pdf.set_x(120)
pdf.multi_cell(0,h=4,align="C", txt='KEPALA DESA CIKONENG', ln=True)
pdf.set_x(120)
pdf.multi_cell(0,h=27,align="C", txt='', ln=True)
pdf.set_x(120)
pdf.multi_cell(0,h=4,align="C", txt='Mustahiq, S.Adm', ln=True)
pdf.set_x(120)
pdf.multi_cell(0,h=4,align="C", txt='NIP : 1918718001902981920', ln=True)

pdf.output("surat_keterangan_kematian.pdf")