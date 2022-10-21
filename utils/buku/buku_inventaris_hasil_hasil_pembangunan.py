# buku_inventaris_hasil_hasil_pembangunan
from xlsxwriter import Workbook

async def buku_inventaris_hasil_hasil_pembangunan(data:dict):
    bulks = []
    for i in data:
        data2 = {}
        data2["nama_proyek"] = str(i.get("nama_proyek"))
        data2["volume"] = str(i.get("volume"))
        data2["biaya"] = str(i.get("biaya"))
        data2["lokasi"] = str(i.get("lokasi"))
        data2["keterangan"] = str(i.get("keterangan"))

        bulks.append(data2)

    workbook = Workbook("download/buku/buku_inventaris_hasil_hasil_pembangunan.xlsx")
    worksheet = workbook.add_worksheet("D.3")


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
    worksheet.set_column('B:B', 25)
    worksheet.set_column('C:C', 16)
    worksheet.set_column('D:D', 16)
    worksheet.set_column('E:E', 16)
    worksheet.set_column('F:F', 18)
    worksheet.merge_range('A3:F3', 'D.3 BUKU INVENTARIS HASIL - HASIL PEMBANGUNAN',head)
    worksheet.merge_range('A4:F4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.write('A6', 'NO. URUT',addon)
    worksheet.write('B6', 'NAMA PROYEK PEMBANGUNAN',addon)
    worksheet.write('C6', 'VOLUME',addon)
    worksheet.write('D6', 'BIAYA',addon)
    worksheet.write('E6', 'LOKASI',addon)
    worksheet.write('F6', 'KETERANGAN',addon)

    worksheet.write('A7', '1',addon)
    worksheet.write('B7', '2',addon)
    worksheet.write('C7', '3',addon)
    worksheet.write('D7', '4',addon)
    worksheet.write('E7', '5',addon)
    worksheet.write("F7","6",addon)

    for index, entry in enumerate(bulks):
        worksheet.write(index+6+1, 0, str(index+1), content)
        worksheet.write(index+6+1, 1, entry.get("nama_proyek"), content)
        worksheet.write(index+6+1, 2, f"{entry.get('volume')} / {entry.get('tanggal_peraturan')}",content)
        worksheet.write(index+6+1, 3, entry.get('biaya'),content)
        worksheet.write(index+6+1, 4, entry.get("lokasi"),content)
        worksheet.write(index+6+1, 5, entry.get("keterangan"),content)
    workbook.close()