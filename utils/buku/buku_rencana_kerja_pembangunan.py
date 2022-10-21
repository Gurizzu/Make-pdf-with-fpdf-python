# buku_kartu_tanda_penduduk_dan_buku_kartu_keluarga
from xlsxwriter import Workbook

async def buku_rencana_kerja_pembangunan(data:dict):
    bulks = []
    for i in data:
        data2 = {}
        data2["nama_proyek"] = str(i.get("nama_proyek"))
        data2["lokasi"] = str(i.get("lokasi"))
        if i.get("sumber_biaya"):
            data2["pemerintah"] = str(i.get("sumber_biaya").get("pemerintah"))
            data2["provinsi"] = str(i.get("sumber_biaya").get("provinsi"))
            data2["kab_kota"] = str(i.get("sumber_biaya").get("kab_kota"))
            data2["swadaya"] = str(i.get("sumber_biaya").get("swadaya"))
        data2["jumlah_biaya"] = str(i.get("jumlah_biaya"))
        data2["pelaksana"] = str(i.get("pelaksana"))
        data2["manfaat"] = str(i.get("manfaat"))
        data2["keterangan"] = str(i.get("keterangan"))

        bulks.append(data2)

    workbook = Workbook("download/buku/buku_rencana_kerja_pembangunan.xlsx")
    worksheet = workbook.add_worksheet("D.1")


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
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 16)
    worksheet.set_column('E:E', 16)
    worksheet.set_column('F:F', 16)
    worksheet.set_column('G:G', 16)
    worksheet.set_column('H:H', 16)
    worksheet.set_column('I:I', 17)
    worksheet.set_column('J:J', 22)
    worksheet.set_column('K:K', 18)
    worksheet.merge_range('A3:K3', 'D.1 BUKU RENCANA KERJA PEMBANGUNAN',head)
    worksheet.merge_range('A4:K4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.merge_range('A6:A7', 'NO. URUT',addon)
    worksheet.merge_range('B6:B7', 'NAMA PROYEK / KEGIATAN',addon)
    worksheet.merge_range('C6:C7', 'LOKASI',addon)
    worksheet.merge_range('D6:G6', 'SUMBER BIAYA',addon)
    worksheet.write('D7', 'PEMERINTAH',addon)
    worksheet.write('E7', 'PROVINSI',addon)
    worksheet.write('F7', 'KAB/KOTA',addon)
    worksheet.write('G7', 'SWADAYA',addon)
    worksheet.merge_range('H6:H7', 'JUMLAH',addon)
    worksheet.merge_range('I6:I7', 'PELAKSANA',addon)
    worksheet.merge_range('J6:J7', 'MANFAAT',addon)
    worksheet.merge_range('K6:K7', 'KETERANGAN',addon)

    worksheet.write('A8', '1',addon)
    worksheet.write('B8', '2',addon)
    worksheet.write('C8', '3',addon)
    worksheet.write('D8', '4',addon)
    worksheet.write('E8', '5',addon)
    worksheet.write("F8","6",addon)
    worksheet.write("G8","7",addon)
    worksheet.write('H8', '8',addon)
    worksheet.write('I8', '9',addon)
    worksheet.write('J8', '10',addon)
    worksheet.write('K8', '11',addon)

    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1), content)
        worksheet.write(index+7+1, 1, entry.get("nama_proyek"), content)
        worksheet.write(index+7+1, 2, f"{entry.get('lokasi')}",content)
        worksheet.write(index+7+1, 3, entry.get('pemerintah'),content)
        worksheet.write(index+7+1, 4, entry.get("provinsi"),content)
        worksheet.write(index+7+1, 5, entry.get("kab_kota"),content)
        worksheet.write(index+7+1, 6, f"{entry.get('swadaya')}",content)
        worksheet.write(index+7+1, 7, f"{entry.get('jumlah_biaya')}",content)
        worksheet.write(index+7+1, 8, f"{entry.get('pelaksana')}",content)
        worksheet.write(index+7+1, 9, entry.get('manfaat'),content)
        worksheet.write(index+7+1, 10, entry.get('keterangan'),content)

    workbook.close()