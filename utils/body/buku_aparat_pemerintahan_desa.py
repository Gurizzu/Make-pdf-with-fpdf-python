from fpdf import FPDF

async def buku_aparat_pemerintah_desa(pdf:FPDF, data:dict):
    pdf.add_page()
    pdf.set_fill_color(224, 222, 222)
    pdf.set_font('times',"B", size=12)
    pdf.cell(0,8,border=0,txt="A.4 BUKU APARAT PEMERINTAH DESA",align="C",ln=1)
    pdf.cell(0,8,border=0,txt="DESA CIKONENG KABUPATEN BANDUNG BARAT",align="C",ln=1)
    pdf.ln(4)
    pdf.set_font(family="arial",style="B",size=9)
    line_height = pdf.font_size * 6
    col_width = pdf.epw / 8  # distribute content evenly 
    no_urut = 1
    pdf.multi_cell(20, line_height, "NO URUT", border=1, new_x="RIGHT", new_y="TOP", max_line_height=20, align="C", fill=True)
    pdf.multi_cell(col_width - 13, line_height, "NAMA", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 20, line_height, "NIAP", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 20, line_height, "NIP", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 30, line_height, "JENIS KELAMIN", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 20, line_height, "TEMPAT DAN TANGGAL LAHIR", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 30, line_height, "AGAMA", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 20, line_height, "PANGKAT GOLONGAN", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 20, line_height, "JABATAN", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 18, line_height, "PENDIDIKAN TERAKHIR", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C", fill=True)
    pdf.multi_cell(col_width - 10, line_height, "NOMOR DAN TANGGAL KEPUTUSAN PENGANGKATAN", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 4, align="C", fill=True)
    pdf.multi_cell(col_width - 10, line_height, "NOMOR DAN TANGGAL KEPUTUSAN PEMBERHENTIAN", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 4, align="C", fill=True)
    pdf.multi_cell(col_width - 5, line_height, "KETERANGAN", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 4, align="C",ln=True, fill=True)

    data_line_height = pdf.font_size * 7.9
    data_col_width = pdf.epw / 8
    for i in data:
      pdf.multi_cell(20, data_line_height, str(no_urut), border=1, new_x="RIGHT", new_y="TOP", max_line_height=20, align="C")
      pdf.multi_cell(data_col_width - 13, data_line_height, str(i.get("nama")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C")
      pdf.multi_cell(data_col_width - 20, data_line_height, str(i.get("niap_nikd_nipd")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C")
      pdf.multi_cell(data_col_width - 20, data_line_height, str(i.get("nip")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C")
      pdf.multi_cell(data_col_width - 30, data_line_height, str(i.get("jenis_kelamin")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C")
      pdf.multi_cell(data_col_width - 20, data_line_height, f"{i.get('tempat_lahir')}, {i.get('tanggal_lahir')}", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C",)
      pdf.multi_cell(data_col_width - 30, data_line_height, str(i.get("agama")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C",)
      pdf.multi_cell(data_col_width - 20, data_line_height, str(i.get("pangkat_golongan")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C",)
      pdf.multi_cell(data_col_width - 20, data_line_height, str(i.get("jabatan")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C",)
      pdf.multi_cell(data_col_width - 18, data_line_height, str(i.get("pendidikan_terakhir")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 5, align="C",)
      pdf.multi_cell(data_col_width - 10, data_line_height, f"{i.get('nomor_keputusan_pengangkatan')} / {i.get('tanggal_keputusan_pengangkatan')}", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 4, align="C",)
      pdf.multi_cell(data_col_width - 10, data_line_height, f"{i.get('nomor_keputusan_pemberhentian')} / {i.get('tanggal_keputusan_pemberhentian')}", border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 4, align="C",)
      pdf.multi_cell(data_col_width - 5, data_line_height, str(i.get("keterangan")), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size + 4, align="C",ln=1)
      no_urut += 1