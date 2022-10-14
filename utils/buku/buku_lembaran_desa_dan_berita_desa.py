from xlsxwriter import Workbook

async def buku_lembaran_desa_dan_berita_desa(data:dict):
    
    workbook = Workbook("download/buku_lembaran_desa_dan_berita_desa/buku_lembaran_desa_dan_berita_desa.xlsx")
    worksheet = workbook.add_worksheet("A.9")
    
    addon = workbook.add_format(
    {
        "font": "Cambria",
        "align": "center",
        "font_size":"9",
        "border":True,
        "bg_color":"#EDEDED",
        "text_wrap":True
    }
    )

    head = workbook.add_format(
        {
            "align": "center",
            "font": "Cambria",
            "font_size": "11",
        }
    )

    body = workbook.add_format(
        {
            "align": "center",
            "font": "Cambria",
            "font_size":"9",
            "border":True
            
        }
    )


    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 25)
    worksheet.set_column('C:C', 35)
    worksheet.set_column('D:D', 25)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 25)
    worksheet.merge_range('A3:G3', 'A.9 BUKU LEMBARAN DESA DAN BERITA DESA',head)
    worksheet.merge_range('A4:G4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.merge_range('A6:A7', 'NO. URUT',addon)
    worksheet.merge_range('B6:B7', 'JENIS PERATURAN DI DESA',addon)
    worksheet.merge_range('C6:C7', 'NOMOR DAN TANGGAL DITETAPKAN',addon)
    worksheet.merge_range('D6:D7', 'TENTANG',addon)
    worksheet.merge_range('E6:F6', 'DIUNDANGKAN',addon)
    worksheet.write("E7","TANGGAL",addon)
    worksheet.write("F7","NOMOR",addon)
    worksheet.merge_range('G6:G7', 'KETERANGAN',addon)


    worksheet.write("A8","1",addon)
    worksheet.write("B8","2",addon)
    worksheet.write("C8","3",addon)
    worksheet.write("D8","4",addon)
    worksheet.write("E8","5",addon)
    worksheet.write("F8","6",addon)
    worksheet.write("G8","7",addon)
    
    bulks = []
    for i in data:
        data2 = {}
        data2["jenis_peraturan"] = i.get("jenis_peraturan")
        data2["nomor_peraturan"] = i.get("nomor_peraturan")
        data2["tanggal_peraturan"] = i.get("tanggal_peraturan")
        data2["tentang"] = i.get("tentang")
        data2["tanggal_diundangkan"] = i.get("tanggal_diundangkan")
        data2["nomor_diundangkan"] = i.get("nomor_diundangkan")
        data2["keterangan"] = i.get("keterangan")   
        

        bulks.append(data2)


    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1),body)
        worksheet.write(index+7+1, 1, entry.get("jenis_peraturan"),body)
        worksheet.write(index+7+1, 2,f"{entry.get('nomor_peraturan')}/{entry.get('tanggal_peraturan')}",body )
        worksheet.write(index+7+1, 3, entry.get("tentang"),body)
        worksheet.write(index+7+1, 4, entry.get("tanggal_diundangkan"),body)
        worksheet.write(index+7+1, 5, entry.get("nomor_diundangkan"),body)
        worksheet.write(index+7+1, 6, entry.get("keterangan"),body)
        
    workbook.close()