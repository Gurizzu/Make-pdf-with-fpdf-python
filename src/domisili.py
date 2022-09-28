from fpdf import FPDF
 
pdf = FPDF(orientation="P", format="A4")

pdf.add_page()
pdf.set_font("helvetica","B",15)
pdf.image("kbb.png",w=30, h = 30, x=10, y=10)

pdf.set_x(40)
pdf.multi_cell(0, h=10 ,align="C",border=1,txt="PEMERINTAH PROVINSI KABUPATEN BANDUNG BARAT",ln=1)
pdf.set_font("helvetica","B",20)
pdf.set_x(40)
pdf.multi_cell(0,align="C",border=1,txt="RT. 004 RW. 004 KEC. BATUJAJAR KAB. BANDUNG BARAT - JAWA BARAT")

pdf.ln(10)
pdf.set_fill_color(0,0,0)
pdf.cell(0,2,border=1, fill=1)
pdf.ln(15)
pdf.set_font("helvetica","BU",19)
pdf.cell(0, h=10 ,align="C", border=1, txt="SURAT KETERANGAN DOMISILI",ln=1)
pdf.set_font("helvetica","",17)
pdf.cell(0, h=10 ,align="C", border=1, txt="No.12/Sekrt-RT/III/2018")
pdf.ln(20)
pdf.set_font("helvetica","",13)
pdf.multi_cell(0, h=8 ,align="L", border=1, txt="\t\t\t\t\t\t\t\t\tYang bertanda tangan di bawah ini Ketua RT. 004 RW. 004 Desa Batujajar timur Kecamatan Batujajar Kab Bandung Barat dengan ini menerangkan bahwa:")
pdf.ln(10)


key = ["Nama Lengkap","Tempat, Tgl Lahir", "Jenis Kelamin", "Pekerjaan", "Agama","Status Perkawinan","Warga Negara"]
val = ["Muhamad Yusuf Rifqi Nurfadillah", 'Subang, 8 Maret 1995', "Perempuan", "Bidan", "Islam", "Belum Menikah", "Indonesia"]



pdf.set_font("helvetica","",13)
for iter, i in enumerate(key):
    pdf.cell(20,8, border=1)
    pdf.cell(75,8, align="L", border=1, txt=i)
    pdf.cell(10,8,border=1, align="L" ,txt=":")
    pdf.multi_cell(75,8, align="L", border=1, ln=1, txt=val[iter])
    

pdf.ln(10)
pdf.set_font("helvetica","",13)
pdf.multi_cell(0, h=8 ,align="L", border=1, txt="\t\t\t\t\t\t\t\t\t Orang tersebut diatas, adalah benar benar warga kami dan berdomisili di RT.004 RW.004 Desa Batujajar timur Kecamatan Batujajar Kab Bandung Barat.Surat keterangan ini dibuat sebagai kelengkapan surat tanda registrasi penguruasan.", ln=1)
pdf.ln(2)
pdf.multi_cell(0,h=8 ,align="L", border=1, txt="\t\t\t\t\t\t\t\t\t Dengan demikian surat keterangan ini kami buat, untuk dapat dipergunakan sebagaimana mestinya")
pdf.ln(15)

pdf.cell(60,h=8 ,align="L", border=1)
pdf.cell(120,h=8 ,align="R", border=1, txt="Bandung Barat, 28 September 2022",ln=1)
pdf.cell(60,h=8 ,align="L", border=1)
pdf.cell(120,h=8 ,align="R", border=1, txt="Ketua RT.004 RW.004")




pdf.output("pdf-with-image.pdf")
