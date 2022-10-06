from fpdf import FPDF
import datetime

#template for footer    
async def footer2(pdf:FPDF,data:dict):
    timestamp = data.get("createdAt") if not data.get("updatedAt") else data.get("updatedAt")

    if timestamp: 
        your_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)  # using the local timezone
        dt = your_dt.strftime("%Y-%m-%d %H:%M:%S").split()
        date = dt[0]
    else:
        date = str(datetime.datetime.utcnow()).split()[0]

    data_footer = data.get("id_tanda_tangan")
    jabatan = "-" if not data_footer else str(data_footer.get("jabatan"))
    nama_lengkap = "-" if not data_footer else str(data_footer.get("nama_lengkap"))
    nip = "-" if not data_footer else str(data_footer.get("nip"))

    pdf.set_font("arial","",10)
    pdf.ln(2)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt= f"Cikoneng, {date}",ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt=jabatan,ln=1)

    pdf.cell(0,h=17 ,align="L", border=0,ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt=nama_lengkap,ln=1)
    pdf.set_x(125)
    pdf.multi_cell(60,h=4 ,align="C", border=0, txt=f"NIP : {nip}",ln=1)