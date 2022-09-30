from fpdf import FPDF


#template for header     
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