from xlsxwriter import Workbook

async def buku_keputusan_kepala_desa(data:dict):
    bulks = []
    for i in data:
        data2 = {}
        data2["nomor_keputusan"] = str(i.get("nomor_keputusan"))
        data2["tanggal_keputusan"] = str(i.get("tanggal_keputusan"))
        data2["tentang"] = str(i.get("tentang"))
        data2["uraian_singkat"] = str(i.get("uraian_singkat"))
        data2["nomor_dilaporkan"] = str(i.get("nomor_dilaporkan"))
        data2["tanggal_dilaporkan"] = str(i.get("tanggal_dilaporkan"))
        data2["keterangan"] = str(i.get("keterangan"))

        bulks.append(data2)

    workbook = Workbook("download/buku/buku_keputusan_kepala_desa.xlsx")
    worksheet = workbook.add_worksheet("A.2")


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
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 23)
    worksheet.set_column('D:D', 25)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('F:F', 25)
    worksheet.merge_range('A3:F3', 'A.2 BUKU KEPUTUSAN KEPALA DESA',head)
    worksheet.merge_range('A4:F4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.write('A6', 'NO. URUT',addon)
    worksheet.write('B6', 'NOMOR DAN TANGGAL KEPUTUSAN KEPALA DESA',addon)
    worksheet.write('C6', 'TENTANG',addon)
    worksheet.write('D6', 'URAIAN SINGKAT',addon)
    worksheet.write('E6', 'NOMOR DAN TANGGAL DILAPORKAN',addon)
    worksheet.write("F6","KETERANGAN",addon)

    worksheet.write('A7', '1',addon)
    worksheet.write('B7', '2',addon)
    worksheet.write('C7', '3',addon)
    worksheet.write('D7', '4',addon)
    worksheet.write('E7', '5',addon)
    worksheet.write("F7","6",addon)

    for index, entry in enumerate(bulks):
        worksheet.write(index+6+1, 0, str(index+1), content)
        worksheet.write(index+6+1, 1, f"{entry.get('nomor_keputusan')} / {entry.get('tanggal_keputusan')}", content)
        worksheet.write(index+6+1, 2, f"{entry.get('tentang')}",content)
        worksheet.write(index+6+1, 3, entry.get('uraian_singkat'),content)
        worksheet.write(index+6+1, 4, f"{entry.get('nomor_dilaporkan')} / {entry.get('tanggal_dilaporkan')}",content)
        worksheet.write(index+6+1, 5, entry.get('keterangan'),content)

    workbook.close()