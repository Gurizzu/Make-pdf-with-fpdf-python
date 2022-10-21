# buku_inventaris_hasil_hasil_pembangunan
from xlsxwriter import Workbook

async def buku_kader_pemberdayaan_masyarakat(data:dict):
    bulks = []
    for i in data:
        data2 = {}
        data2["nama"] = str(i.get("nama"))
        data2["umur"] = str(i.get("umur"))
        data2["jenis_kelamin"] = str(i.get("jenis_kelamin"))
        data2["pendidikan"] = str(i.get("pendidikan"))
        data2["bidang"] = str(i.get("bidang"))
        data2["alamat"] = str(i.get("alamat"))
        data2["keterangan"] = str(i.get("keterangan"))

        bulks.append(data2)

    workbook = Workbook("download/buku/buku_kader_pemberdayaan_masyarakat.xlsx")
    worksheet = workbook.add_worksheet("D.4")


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
    worksheet.set_column('G:G', 18)
    worksheet.set_column('H:H', 18)
    worksheet.merge_range('A3:H3', 'D.4 BUKU KADER PEMBERDAYAAN MASYARAKAT',head)
    worksheet.merge_range('A4:H4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.write('A6', 'NO. URUT',addon)
    worksheet.write('B6', 'NAMA',addon)
    worksheet.write('C6', 'UMUR',addon)
    worksheet.write('D6', 'JENIS KELAMIN',addon)
    worksheet.write('E6', 'PENDIDIKAN/KURSUS',addon)
    worksheet.write('F6', 'BIDANG',addon)
    worksheet.write('G6', 'ALAMAT',addon)
    worksheet.write('H6', 'KETERANGAN',addon)

    worksheet.write('A7', '1',addon)
    worksheet.write('B7', '2',addon)
    worksheet.write('C7', '3',addon)
    worksheet.write('D7', '4',addon)
    worksheet.write('E7', '5',addon)
    worksheet.write("F7","6",addon)
    worksheet.write("G7","7",addon)
    worksheet.write("H7","8",addon)

    for index, entry in enumerate(bulks):
        worksheet.write(index+6+1, 0, str(index+1), content)
        worksheet.write(index+6+1, 1, entry.get("nama"), content)
        worksheet.write(index+6+1, 2, f"{entry.get('umur')}",content)
        worksheet.write(index+6+1, 3, entry.get('jenis_kelamin'),content)
        worksheet.write(index+6+1, 4, entry.get("pendidikan"),content)
        worksheet.write(index+6+1, 5, entry.get("bidang"),content)
        worksheet.write(index+6+1, 6, f"{entry.get('alamat')}",content)
        worksheet.write(index+6+1, 7, f"{entry.get('keterangan')}",content)


    workbook.close()