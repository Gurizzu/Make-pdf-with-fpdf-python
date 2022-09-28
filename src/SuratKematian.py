from fpdf import FPDF
 
pdf = FPDF(orientation="P", format="A4")

pdf.add_page()
pdf.set_margins(30,30)
pdf.set_font("helvetica","B",15)
pdf.image("kbb.jpg",w=30, h = 30 , x=30 , y=30)

pdf.set_x(60)
pdf.multi_cell(0, h=3 ,align="C",border=0,txt="PEMERINTAH KABUPATEN BANDUNG",ln=1)
pdf.set_font("helvetica","",14)
pdf.set_x(60)
pdf.multi_cell(0, h=10 ,align="C",border=0,txt="KECAMATAN CIPARAY",ln=1)
pdf.set_x(60)
pdf.multi_cell(0, h=3 ,align="C",border=0,txt="DESA CIKONENG",ln=1)




pdf.output("surat_keterangan_kematian.pdf")

