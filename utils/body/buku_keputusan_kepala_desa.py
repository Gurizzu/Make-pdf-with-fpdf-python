from fpdf import FPDF

async def buku_keputusan_kepala_desa(pdf:FPDF, data:dict):
    pdf.add_page()
    pdf.set_fill_color(209, 207, 207)
    pdf.set_fill_color(246,246,246)
    pdf.set_font('times',"B", size=12)
    pdf.cell(0,8,border=0,txt="A.2 BUKU KEPUTUSAN KEPALA DESA",align="C",ln=1)
    pdf.cell(0,8,border=0,txt="DESA CIKONENG KABUPATEN BANDUNG BARAT",align="C",ln=1)
    pdf.ln(4)
    pdf.set_font('times',"B", size=7.5)
    pdf.set_font(family="arial",style="B",size=9)
    line_height = pdf.font_size * 6
    col_width = pdf.epw / 8  # distribute content evenly 
    no_urut = 1
    pdf.multi_cell(20, line_height, "NO URUT", border=1, new_x="RIGHT", new_y="TOP", max_line_height=20, align="C", fill=True)
    pdf.multi_cell(col_width + 10, line_height, "NOMOR DAN TANGGAL KEPUTUSAN KEPALA DESA", border=1, new_x="RIGHT", new_y="TOP",fill=True, max_line_height=pdf.font_size + 5, align="C")
    pdf.multi_cell(col_width + 50, line_height, "TENTANG", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width + 50, line_height, "URAIAN SINGKAT", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width, line_height, "NOMOR DAN TANGGAL DILAPORKAN", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width + 10, line_height, "KETERANGAN", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", ln=True, fill=True)

    for i in data:
        pdf.set_font(family="arial",style="",size=9)
        pdf.multi_cell(20, line_height, str(no_urut), border=1, new_x="RIGHT", new_y="TOP", max_line_height=20, align="C")
        pdf.multi_cell(col_width + 10, line_height, str(i.get("nomor_keputusan")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 3, align="C")
        pdf.multi_cell(col_width + 50, line_height, str(i.get("tentang")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 3, align="C")
        pdf.multi_cell(col_width + 50, line_height, str(i.get("uraian_singkat")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 3, align="C")
        pdf.multi_cell(col_width, line_height, str(i.get("nomor_dilaporkan")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 3, align="C")
        pdf.multi_cell(col_width + 10, line_height, str(i.get("keterangan")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 3, align="C", ln=True)
        no_urut += 1
