from typing import List
from xlsxwriter import Workbook

async def buku_induk_penduduk(data):
    bulks = []
    for i in data:
        data2 = {}
        if i.get("umum"):
            data2["nama_lengkap"] = i.get("umum").get("nama_lengkap")
            data2["jenis_kelamin"] = i.get("umum").get("jenis_kelamin")
            data2["agama"] = i.get("umum").get("agama")
            data2["pendidikan_terakhir"] = i.get("umum").get("pendidikan_terakhir")
            data2["pekerjaan"] = i.get("umum").get("pekerjaan")
            data2["dapat_membaca_huruf"] = i.get("umum").get("dapat_membaca_huruf")
            data2["kewarganegaraan"] = i.get("umum").get("kewarganegaraan")
            data2["alamat_rumah"] = i.get("umum").get("alamat_rumah")
            data2["nik"] = i.get("umum").get("nik")

        if i.get("nikah_cerai"):
            data2["status_perkawinan"] = i.get("nikah_cerai").get("status_perkawinan")

        if i.get("kelahiran"):
            data2["tempat_lahir"] = i.get("kelahiran").get("tempat_lahir")
            data2["tanggal_lahir"] = i.get("kelahiran").get("tanggal_lahir")
            data2["kedudukan_dalam_keluarga"] = i.get("kelahiran").get("kedudukan_dalam_keluarga")
            data2["nomor_kk"] = i.get("kelahiran").get("nomor_kk")
        
        if i.get("lain_lain"):
            data2["keterangan"] = i.get("kelahiran").get("keterangan")
        bulks.append(data2)

    workbook = Workbook("download/buku/buku_induk_penduduk.xlsx")
    worksheet = workbook.add_worksheet("B.1")


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
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 17)
    worksheet.set_column('D:D', 15)
    worksheet.set_column('E:E', 14)
    worksheet.set_column('F:F', 14)
    worksheet.set_column('G:G', 12)
    worksheet.set_column('H:H', 20)
    worksheet.set_column('I:I', 12)
    worksheet.set_column('J:J', 21)
    worksheet.set_column('K:K', 17)
    worksheet.set_column('L:L', 17)
    worksheet.set_column('M:M', 19)
    worksheet.set_column('N:N', 19)
    worksheet.set_column('O:O', 19)
    worksheet.set_column('P:P', 19)
    worksheet.merge_range('A3:P3', 'B.1 BUKU INDUK PENDUDUK',head)
    worksheet.merge_range('A4:P4', 'DESA CIKONENG KABUPATEN BANDUNG',head)

    
    worksheet.merge_range('A6:A7', 'NO. URUT',addon)
    worksheet.merge_range('B6:B7', 'NAMA LENGKAP',addon)
    worksheet.merge_range('C6:C7', 'JENIS KELAMIN',addon)
    worksheet.merge_range('D6:D7', 'STATUS PERKAWINAN',addon)
    worksheet.merge_range('E6:F6', 'TEMPAT TANGGAL LAHIR',addon)
    worksheet.write('E7', 'TEMPAT LAHIR',addon)
    worksheet.write('F7', 'TANGGAL LAHIR',addon)
    worksheet.merge_range('G6:G7', 'AGAMA',addon)
    worksheet.merge_range('H6:H7', 'PENDIDIKAN TERAKHIR',addon)
    worksheet.merge_range('I6:I7', 'PEKERJAAN',addon)
    worksheet.merge_range('J6:J7', 'DAPAT MEMBACA HURUF',addon)
    worksheet.merge_range('K6:K7', 'KEWARGANEGARAAN',addon)
    worksheet.merge_range('L6:L7', 'ALAMAT LENGKAP',addon)
    worksheet.merge_range('M6:M7', 'KEDUDUKAN DALAM KELUARGA',addon)
    worksheet.merge_range('N6:N7', 'NIK',addon)
    worksheet.merge_range('O6:O7', 'NO KK',addon)
    worksheet.merge_range('P6:P7', 'KETERANGAN',addon)

    worksheet.write('A8', "1",addon)
    worksheet.write('B8', "2",addon)
    worksheet.write('C8', "3",addon)
    worksheet.write('D8', "4",addon)
    worksheet.write('E8', "5",addon)
    worksheet.write('F8', "6",addon)
    worksheet.write('G8', "7",addon)
    worksheet.write('H8', "8",addon)
    worksheet.write('I8', "9",addon)
    worksheet.write('J8', "10",addon)
    worksheet.write('K8', "11",addon)
    worksheet.write('L8', "12",addon)
    worksheet.write('M8', "13",addon)
    worksheet.write('N8', "14",addon)
    worksheet.write('O8', "15",addon)
    worksheet.write('P8', "16",addon)

    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1), content)
        worksheet.write(index+7+1, 1, f"{entry.get('nama_lengkap')}", content)
        worksheet.write(index+7+1, 2, f"{entry.get('jenis_kelamin')}",content)
        worksheet.write(index+7+1, 3, entry.get('status_perkawinan'),content)
        worksheet.write(index+7+1, 4, f"{entry.get('tempat_lahir')}",content)
        worksheet.write(index+7+1, 5, entry.get('tanggal_lahir'),content)
        worksheet.write(index+7+1, 6, entry.get('agama'),content)
        worksheet.write(index+7+1, 7, entry.get('pendidikan_terakhir'),content)
        worksheet.write(index+7+1, 8, entry.get('pekerjaan'),content)
        worksheet.write(index+7+1, 9, entry.get('dapat_membaca_huruf'),content)
        worksheet.write(index+7+1, 10, entry.get('kewarganegaraan'),content)
        worksheet.write(index+7+1, 11, entry.get('alamat_rumah'),content)
        worksheet.write(index+7+1, 12, entry.get('kedudukan_dalam_keluarga'),content)
        worksheet.write(index+7+1, 13, entry.get('nik'),content)
        worksheet.write(index+7+1, 14, entry.get('nomor_kk'),content)
        worksheet.write(index+7+1, 15, entry.get('keterangan'),content)
    workbook.close()