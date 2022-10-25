from xlsxwriter import Workbook

async def buku_rekapitulasi_jumlah_penduduk(data):
    workbook = Workbook("download/buku/buku_rekapitulasi_jumlah_penduduk.xlsx")
    worksheet = workbook.add_worksheet("B.3")

    addon = workbook.add_format(
        {
            "font": "Cambria",
            "align": "center",
            "font_size":"9",
            "border":True,
            "bg_color":"#EDEDED",
            "text_wrap" : True
        }
    )
    addon.set_align('vcenter')

    head = workbook.add_format(
        {
            "align": "center",
            "font": "Cambria",
            "font_size": "11",
        }
    )

    content = workbook.add_format(
        {
            "font": "Cambria",
            "align": "center",
            "font_size":"9",
            "border":True,
            "text_wrap" : True
        }
    )
    content.set_align('vcenter')


    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 24)
    worksheet.set_column('C:C', 18)
    worksheet.set_column('D:D', 18)
    worksheet.set_column('E:E', 18)
    worksheet.set_column('F:F', 18)
    worksheet.merge_range('A3:F3', 'B.3 BUKU REKAPITULASI JUMLAH PENDUDUK',head)
    worksheet.merge_range('A4:F4', 'DESA CIKONENG KABUPATEN BANDUNG',head)

    worksheet.merge_range('A6:A9', 'NO. URUT',addon)
    worksheet.merge_range('B6:B9', 'NAMA DUSUN/LINGKUNGAN',addon)
    worksheet.merge_range('C6:F6', 'JUMLAH TOTAL PENDUDUK',addon)
    worksheet.merge_range('C7:D8', 'WNI',addon)
    worksheet.merge_range('E7:F8', 'WNA',addon)
    worksheet.write("C9","LAKI-LAKI",addon)
    worksheet.write("D9","PEREMPUAN",addon)
    worksheet.write('E9', 'LAKI-LAKI',addon)
    worksheet.write('F9', 'PEREMPUAN',addon)

    worksheet.write('A10', '1',addon)
    worksheet.write('B10', '2',addon)
    worksheet.write('C10', '3',addon)
    worksheet.write('D10', '4',addon)
    worksheet.write('E10', '5',addon)
    worksheet.write("F10","6",addon)

    for index, entry in enumerate(data):
        worksheet.write(index+9+1, 0, str(index+1), content)
        worksheet.write(index+9+1, 1, entry.get("dusun"), content)
        worksheet.write(index+9+1, 2, entry.get("wni_laki"),content)
        worksheet.write(index+9+1, 3, entry.get("wni_perempuan"),content)
        worksheet.write(index+9+1, 4, entry.get("wna_laki"),content)
        worksheet.write(index+9+1, 5, entry.get("wna_perempuan"),content)

    workbook.close()