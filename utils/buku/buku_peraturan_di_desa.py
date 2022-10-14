from xlsxwriter import Workbook

async def buku_peraturan_di_desa(data:dict):
    bulks = []
    for i in data:
        data2 = {}
        data2["jenis_peraturan"] = str(i.get("jenis_peraturan"))
        data2["nomor_peraturan"] = str(i.get("nomor_peraturan"))
        data2["tanggal_peraturan"] = str(i.get("tanggal_peraturan"))
        data2["tentang"] = str(i.get("tentang"))
        data2["uraian_singkat"] = str(i.get("uraian_singkat"))
        data2["tanggal_kesepakatan"] = str(i.get("tanggal_kesepakatan"))
        data2["nomor_dilaporkan"] = str(i.get("nomor_dilaporkan"))
        data2["tanggal_dilaporkan"] = str(i.get("tanggal_dilaporkan"))
        data2["nomor_lembaran" ] = str(i.get("nomor_lembaran"))
        data2["tanggal_lembaran"] = str(i.get("tanggal_lembaran"))
        data2["nomor_berita_desa"] = str(i.get("nomor_berita_desa"))
        data2["tanggal_berita_desa"] = str(i.get("tanggal_berita_desa"))
        data2["keterangan"] = str(i.get("keterangan"))

        bulks.append(data2)

    workbook = Workbook("download/buku_peraturan_di_desa/buku_peraturan_di_desa.xlsx")
    worksheet = workbook.add_worksheet("A.1")


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
    worksheet.set_column('B:B', 16)
    worksheet.set_column('C:C', 23)
    worksheet.set_column('D:D', 25)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('F:F', 25)
    worksheet.set_column('G:G', 22)
    worksheet.set_column('H:H', 30)
    worksheet.set_column('I:I', 30)
    worksheet.set_column('J:J', 30)
    worksheet.merge_range('A3:J3', 'A.1 BUKU PERATURAN DI DESA',head)
    worksheet.merge_range('A4:J4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.write('A6', 'NO. URUT',addon)
    worksheet.write('B6', 'JENIS PERATURAN DI DESA',addon)
    worksheet.write('C6', 'NOMOR DAN TANGGAL DITETAPKAN',addon)
    worksheet.write('D6', 'TENTANG',addon)
    worksheet.write('E6', 'URAIAN SINGKAT',addon)
    worksheet.write("F6","TANGGAL KESEPAKATAN PERATURAN DESA",addon)
    worksheet.write("G6","NOMOR DAN TANGGAL DILAPORKAN",addon)
    worksheet.write('H6', 'NOMOR DAN TANGGAL DIUNDANGKAN DALAM LEMBARAN DESA',addon)
    worksheet.write('I6', 'NOMOR DAN TANGGAL DIUNDANGKAN DALAM BERITA DESA',addon)
    worksheet.write('J6', 'KETERANGAN',addon)

    worksheet.write('A7', '1',addon)
    worksheet.write('B7', '2',addon)
    worksheet.write('C7', '3',addon)
    worksheet.write('D7', '4',addon)
    worksheet.write('E7', '5',addon)
    worksheet.write("F7","6",addon)
    worksheet.write("G7","7",addon)
    worksheet.write('H7', '8',addon)
    worksheet.write('I7', '9',addon)
    worksheet.write('J7', '10',addon)

    for index, entry in enumerate(bulks):
        worksheet.write(index+6+1, 0, str(index+1), content)
        worksheet.write(index+6+1, 1, entry.get("jenis_peraturan"), content)
        worksheet.write(index+6+1, 2, f"{entry.get('nomor_peraturan')} / {entry.get('tanggal_peraturan')}",content)
        worksheet.write(index+6+1, 3, entry.get('tentang'),content)
        worksheet.write(index+6+1, 4, entry.get("uraian_singkat"),content)
        worksheet.write(index+6+1, 5, entry.get("tanggal_kesepakatan"),content)
        worksheet.write(index+6+1, 6, f"{entry.get('nomor_dilaporkan')} / {entry.get('tanggal_dilaporkan')}",content)
        worksheet.write(index+6+1, 7, f"{entry.get('nomor_lembaran')} / {entry.get('tanggal_lembaran')}",content)
        worksheet.write(index+6+1, 8, f"{entry.get('nomor_berita_desa')} / {entry.get('tanggal_berita_desa')}",content)
        worksheet.write(index+6+1, 9, entry.get('keterangan'),content)

    workbook.close()