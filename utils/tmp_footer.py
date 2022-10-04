from fpdf import FPDF
import datetime

#template for footer    
async def footer2(pdf:FPDF,data:dict):
    timestamp = str(data.get("created_at")) if not str(data.get("updatedAt")) else str(data.get("updatedAt"))
    your_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)  # using the local timezone
    dt = your_dt.strftime("%Y-%m-%d %H:%M:%S").split()
    date = dt[0]
    pdf.set_font("arial","",10)
    pdf.ln(2)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt= f"Cikoneng, {date}",ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt=str(data.get("jabatan")),ln=1)

    pdf.cell(0,h=17 ,align="L", border=0,ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt=str(data.get("nama_lengkap")),ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt=f"NIP : {str(data.get('nip'))}",ln=1)