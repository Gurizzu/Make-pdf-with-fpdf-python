# buku_kartu_tanda_penduduk_dan_buku_kartu_keluarga
from xlsxwriter import Workbook

async def buku_kartu_tanda_penduduk_dan_buku_kartu_keluarga(kepala_cursor,angota_cursor):
    bulks = []

    for i in kepala_cursor:
        data = {}
        try:
            data["nama_lengkap"] = i.get("kepala").get("umum").get("nama_lengkap")
            data["kedudukan_dalam_keluarga"] = i.get("kepala").get("kelahiran").get("kedudukan_dalam_keluarga")
            data["jenis_kelamin"] = i.get("kepala").get("umum").get("jenis_kelamin")
            data["nik"] = i.get("kepala").get("umum").get("nik")
            data["tempat_lahir"] = i.get("kepala").get("kelahiran").get("tempat_lahir")
            data["tanggal_lahir"] = i.get("kepala").get("kelahiran").get("tanggal_lahir")
            data["golongan_darah"] = i.get("kepala").get("umum").get("golongan_darah")
            data["agama"] = i.get("kepala").get("umum").get("agama")
            data["pendidikan_terakhir"] = i.get("kepala").get("umum").get("pendidikan_terakhir")
            data["pekerjaan"] = i.get("kepala").get("umum").get("pekerjaan")
            data["alamat_rumah"] = i.get("kepala").get("umum").get("alamat_rumah")
            data["status_perkawinan"] = i.get("kepala").get("nikah_cerai").get("status_perkawinan")
            data["kewarganegaraan"] = i.get("kepala").get("umum").get("kewarganegaraan")
            data["nama_ibu_kandung"] = i.get("kepala").get("kelahiran").get("nama_ibu_kandung")
            data["nama_ayah_kandung"] = i.get("kepala").get("kelahiran").get("nama_ayah_kandung")
            data["no_kk"] = i.get("no_kk")
            data["keterangan"] = i.get("kepala").get("lain_lain").get("keterangan")
            bulks.append(data)
        except:
            continue

    for i in angota_cursor:
        data = {}
        try:
            data["nama_lengkap"] = i.get("anggota").get("umum").get("nama_lengkap")
            data["kedudukan_dalam_keluarga"] = i.get("anggota").get("kelahiran").get("kedudukan_dalam_keluarga")
            data["jenis_kelamin"] = i.get("anggota").get("umum").get("jenis_kelamin")
            data["nik"] = i.get("anggota").get("umum").get("nik")
            data["tempat_lahir"] = i.get("anggota").get("kelahiran").get("tempat_lahir")
            data["tanggal_lahir"] = i.get("anggota").get("kelahiran").get("tanggal_lahir")
            data["golongan_darah"] = i.get("anggota").get("umum").get("golongan_darah")
            data["agama"] = i.get("anggota").get("umum").get("agama")
            data["pendidikan_terakhir"] = i.get("anggota").get("umum").get("pendidikan_terakhir")
            data["pekerjaan"] = i.get("anggota").get("umum").get("pekerjaan")
            data["alamat_rumah"] = i.get("anggota").get("umum").get("alamat_rumah")
            data["status_perkawinan"] = i.get("anggota").get("nikah_cerai").get("status_perkawinan")
            data["kewarganegaraan"] = i.get("anggota").get("umum").get("kewarganegaraan")
            data["nama_ibu_kandung"] = i.get("anggota").get("kelahiran").get("nama_ibu_kandung")
            data["nama_ayah_kandung"] = i.get("anggota").get("kelahiran").get("nama_ayah_kandung")
            data["no_kk"] = i.get("no_kk")
            data["keterangan"] = i.get("anggota").get("lain_lain").get("keterangan")
            bulks.append(data)
        except:
            continue
            

    workbook = Workbook("download/buku/buku_kartu_tanda_penduduk_dan_buku_kartu_keluarga.xlsx")
    worksheet = workbook.add_worksheet("B.5")

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
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 27)
    worksheet.set_column('E:E', 18)
    worksheet.set_column('F:F', 22)
    worksheet.set_column('G:G', 11)
    worksheet.set_column('H:H', 16)
    worksheet.set_column('I:I', 17)
    worksheet.set_column('J:J', 22)
    worksheet.set_column('K:K', 18)
    worksheet.set_column('L:L', 17)
    worksheet.set_column('M:M', 17)
    worksheet.set_column('N:N', 22)
    worksheet.set_column('O:O', 16)
    worksheet.set_column('P:P', 16)
    worksheet.set_column('Q:Q', 22)
    worksheet.merge_range('A3:Q3', 'B.5 BUKU KARTU TANDA PENDUDUK DAN BUKU KARTU KELUARGA',head)
    worksheet.merge_range('A4:Q4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.merge_range('A6:A7', 'NO. URUT',addon)
    worksheet.merge_range('B6:B7', 'NO.KK',addon)
    worksheet.merge_range('C6:C7', 'NAMA LENGKAP',addon)
    worksheet.merge_range('D6:D7', 'NIK',addon)
    worksheet.merge_range('E6:E7', 'JENIS KELAMIN',addon)
    worksheet.merge_range("F6:F7","TEMPAT TANGGAL LAHIR",addon)
    worksheet.merge_range("G6:G7","GOLONGAN DARAH",addon)
    worksheet.merge_range("H6:H7","AGAMA",addon)
    worksheet.merge_range("I6:I7","PENDIDIKAN",addon)
    worksheet.merge_range("J6:J7","PEKERJAAN",addon)
    worksheet.merge_range("K6:K7","ALAMAT",addon)
    worksheet.merge_range("L6:L7","STATUS PERKAWINAN",addon)
    worksheet.merge_range("M6:M7","STATUS HUBUNGAN KELUARGA",addon)
    worksheet.merge_range("N6:N7","KEWARANEGARAAN",addon)
    worksheet.merge_range("O6:P6","ORANG TUA",addon)
    worksheet.write("O7","AYAH",addon)
    worksheet.write("P7","IBU",addon)
    worksheet.merge_range("Q6:Q7","KETERANGAN",addon)

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
    worksheet.write('L8', '12',addon)
    worksheet.write('M8', '13',addon)
    worksheet.write('N8', '14',addon)
    worksheet.write('O8', '15',addon)
    worksheet.write('P8', '16',addon)
    worksheet.write('Q8', '17',addon)

    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1), content)
        worksheet.write(index+7+1, 1, entry.get("no_kk"), content)
        worksheet.write(index+7+1, 2, entry.get("nama_lengkap"),content)
        worksheet.write(index+7+1, 3, entry.get("nik"),content)
        worksheet.write(index+7+1, 4, entry.get("jenis_kelamin"),content)
        worksheet.write(index+7+1, 5, f"{entry.get('tempat_lahir')}, {entry.get('tanggal_lahir')}",content)
        worksheet.write(index+7+1, 6, entry.get("golongan_darah"),content)
        worksheet.write(index+7+1, 7, entry.get("agama"),content)
        worksheet.write(index+7+1, 8, entry.get("pendidikan_terakhir"),content)
        worksheet.write(index+7+1, 9, entry.get("pekerjaan"),content)
        worksheet.write(index+7+1, 10, entry.get("alamat_rumah"),content)
        worksheet.write(index+7+1, 11, entry.get("status_perkawinan"),content)
        worksheet.write(index+7+1, 12, entry.get("kedudukan_dalam_keluarga"),content)
        worksheet.write(index+7+1, 13, entry.get("kewarganegaraan"),content)
        worksheet.write(index+7+1, 14, entry.get("nama_ayah_kandung"),content)
        worksheet.write(index+7+1, 15, entry.get("nama_ibu_kandung"),content)
        worksheet.write(index+7+1, 16, entry.get("keterangan"),content)

    workbook.close()

