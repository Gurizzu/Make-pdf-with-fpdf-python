
from xlsxwriter import Workbook



async def buku_mutasi_penduduk(data:dict):
    workbook = Workbook("download/buku/buku_mutasi_penduduk.xlsx")
    worksheet = workbook.add_worksheet("B.2")




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
    worksheet.set_column('B:B', 18)
    worksheet.set_column('C:C', 19)
    worksheet.set_column('D:D', 19)
    worksheet.set_column('E:E', 21)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 12)
    worksheet.set_column('H:H', 12)
    worksheet.set_column('I:I', 12)
    worksheet.set_column('J:J', 12)
    worksheet.set_column('K:K', 12)
    worksheet.set_column('L:L', 15)
    worksheet.set_column('M:M', 15)
    worksheet.merge_range('A3:M3', 'B.2 BUKU MUTASI PENDUDUK DESA',head)
    worksheet.merge_range('A4:M4', 'DESA CIKONENG KABUPATEN BANDUNG',head)

        
    worksheet.merge_range('A6:A7', 'NO. URUT',addon)
    worksheet.merge_range('B6:B7', 'NAMA LENGKAP',addon)
    worksheet.merge_range('C6:D6', 'TEMPAT & TANGGAL LAHIR',addon)
    worksheet.write('C7', 'TEMPAT',addon)
    worksheet.write('D7', 'TANGGAL',addon)
    worksheet.merge_range('E6:E7', 'JENIS KELAMIN',addon)
    worksheet.merge_range('F6:F7', 'KEWARGANEGARAAN',addon)
    worksheet.merge_range('G6:H6', 'PENAMBAHAN',addon)
    worksheet.write('G7', 'DATANG DARI',addon)
    worksheet.write('H7', 'TANGGAL',addon)
    worksheet.merge_range('I6:L6', 'PENGURANGAN',addon)
    worksheet.write('I7', 'PINDAH KE',addon)
    worksheet.write('J7', 'TANGGAL',addon)
    worksheet.write('K7', 'MENINGGAL',addon)
    worksheet.write('L7', 'TANGGAL',addon)
    worksheet.merge_range('M6:M7', 'KETERANGAN',addon)

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

    bulks = []
    for i in data:
            data2 = {}
            
            data2["nama_lengkap"] ="" if not i.get("nama_lengkap") else i.get("nama_lengkap")
            data2["tempat_tanggal_lahir"] = "" if not i.get("tempat_tanggal_lahir") else i.get("tempat_tanggal_lahir").split(" ")
            data2["jenis_kelamin"] = "" if not i.get("jenis_kelamin") else i.get("jenis_kelamin")
            data2["Meninggal"] = "" if not i.get("Meninggal") else i.get("Meninggal")
            data2["Pindah"] = "" if not i.get("Pindah") else i.get("Pindah")
            data2["kewarganegaraan"] = "" if not i.get("Kewarganegaraan") else i.get("Kewarganegaraan")
            data2["datang_dari"] = "" if not i.get("datang_dari") else i.get("datang_dari")
            
            bulks.append(data2)
            

            

    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1), content)
        worksheet.write(index+7+1, 1, entry.get("nama_lengkap"),content)
        if entry.get("tempat_tanggal_lahir") == "":
            worksheet.write(index+7+1, 2, entry.get("tempat_tanggal_lahir"),content)
            worksheet.write(index+7+1, 3, entry.get("tempat_tanggal_lahir"),content)
        if "" not in entry.get("tempat_tanggal_lahir"): 
            worksheet.write(index+7+1, 2, entry.get("tempat_tanggal_lahir")[0],content)
            worksheet.write(index+7+1, 3, entry.get("tempat_tanggal_lahir")[1],content)
        worksheet.write(index+7+1, 4, entry.get("jenis_kelamin"),content)
        worksheet.write(index+7+1, 5, entry.get("kewarganegaraan"),content)
        worksheet.write(index+7+1, 6, entry.get("datang_dari"),content)
        worksheet.write(index+7+1, 7, entry.get("Pindah"),content)
        worksheet.write(index+7+1, 8, "",content)
        worksheet.write(index+7+1, 9, "",content)
        worksheet.write(index+7+1, 10, "",content)
        worksheet.write(index+7+1, 11, entry.get("Meninggal"),content)
        worksheet.write(index+7+1, 12, "",content)


    workbook.close()
