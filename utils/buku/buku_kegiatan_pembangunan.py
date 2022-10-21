# buku_kartu_tanda_penduduk_dan_buku_kartu_keluarga
from xlsxwriter import Workbook

async def buku_kegiatan_pembangunan(data:dict):
    bulks = []
    for i in data:
        data2 = {}
        data2["nama_proyek"] = str(i.get("nama_proyek"))
        data2["volume"] = str(i.get("volume"))
        if i.get("besaran_biaya"):
            data2["pemerintah"] = str(i.get("besaran_biaya").get("pemerintah"))
            data2["provinsi"] = str(i.get("besaran_biaya").get("provinsi"))
            data2["kab_kota"] = str(i.get("besaran_biaya").get("kab_kota"))
            data2["swadaya"] = str(i.get("besaran_biaya").get("swadaya"))
        data2["jumlah_biaya"] = str(i.get("jumlah_biaya"))
        data2["waktu_pengerjaan"] = str(i.get("waktu_pengerjaan"))
        data2["sifat_proyek"] = str(i.get("sifat_proyek"))
        data2["pelaksana"] = str(i.get("pelaksana"))
        data2["keterangan"] = str(i.get("keterangan"))

        bulks.append(data2)

    workbook = Workbook("download/buku/buku_kegiatan_pembangunan.xlsx")
    worksheet = workbook.add_worksheet("D.2")


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
    worksheet.set_column('J:J', 16)
    worksheet.set_column('K:K', 16)
    worksheet.set_column('L:L', 17)
    worksheet.set_column('M:M', 17)
    worksheet.merge_range('A3:K3', 'D.2 BUKU KEGIATAN PEMBANGUNAN',head)
    worksheet.merge_range('A4:K4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.merge_range('A6:A8', 'NO. URUT',addon)
    worksheet.merge_range('B6:B8', 'NAMA PROYEK / KEGIATAN',addon)
    worksheet.merge_range('C6:C8', 'VOLUME',addon)
    worksheet.merge_range('D6:G6', 'SUMBER DANA/BESARANA BIAYA',addon)
    worksheet.merge_range('D7:D8', 'PEMERINTAH',addon)
    worksheet.merge_range('E7:E8', 'PROVINSI',addon)
    worksheet.merge_range('F7:F8', 'KAB/KOTA',addon)
    worksheet.merge_range('G7:G8', 'SWADAYA',addon)
    worksheet.merge_range('H6:H8', 'JUMLAH',addon)
    worksheet.merge_range('I6:I8', 'WAKTU',addon)
    worksheet.merge_range('J6:K6', 'SIFAT PROYEK',addon)
    worksheet.merge_range('J7:J8', 'BARU',addon)
    worksheet.merge_range('K7:K8', 'LANJUTAN',addon)
    worksheet.merge_range('L6:L8', 'PELAKSANA',addon)
    worksheet.merge_range('M6:M8', 'KETERANGAN',addon)


    worksheet.write('A9', '1',addon)
    worksheet.write('B9', '2',addon)
    worksheet.write('C9', '3',addon)
    worksheet.write('D9', '4',addon)
    worksheet.write('E9', '5',addon)
    worksheet.write("F9","6",addon)
    worksheet.write("G9","7",addon)
    worksheet.write('H9', '8',addon)
    worksheet.write('I9', '9',addon)
    worksheet.write('J9', '10',addon)
    worksheet.write('K9', '11',addon)
    worksheet.write('L9', '12',addon)
    worksheet.write('M9', '13',addon)

    for index, entry in enumerate(bulks):
        worksheet.write(index+8+1, 0, str(index+1), content)
        worksheet.write(index+8+1, 1, entry.get("nama_proyek"), content)
        worksheet.write(index+8+1, 2, f"{entry.get('volume')}",content)
        worksheet.write(index+8+1, 3, entry.get('pemerintah'),content)
        worksheet.write(index+8+1, 4, entry.get("provinsi"),content)
        worksheet.write(index+8+1, 5, entry.get("kab_kota"),content)
        worksheet.write(index+8+1, 6, f"{entry.get('swadaya')}",content)
        worksheet.write(index+8+1, 7, f"{entry.get('jumlah_biaya')}",content)
        worksheet.write(index+8+1, 8, f"{entry.get('waktu_pengerjaan')}",content)
        if str(entry.get('sifat_proyek')).lower() == "baru":
            worksheet.write(index+8+1, 9, f"{entry.get('sifat_proyek')}",content)
            worksheet.write(index+8+1, 10, f" ",content)
        elif str(entry.get('sifat_proyek')).lower() == "lanjutan":
            worksheet.write(index+8+1, 9, f" ",content)
            worksheet.write(index+8+1, 10, f"{entry.get('sifat_proyek')}",content)
        else:
            worksheet.write(index+8+1, 9, f" ",content)
            worksheet.write(index+8+1, 10, f" ",content)
        worksheet.write(index+8+1, 11, f"{entry.get('pelaksana')}",content)
        worksheet.write(index+8+1, 12, f"{entry.get('keterangan')}",content)

    workbook.close()