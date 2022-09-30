from fpdf import FPDF

#template for footer    
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