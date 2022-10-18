from xlsxwriter import Workbook

async def buku_tanah_di_desa(data:dict):
    workbook = Workbook("download/buku/buku_tanah_di_desa.xlsx")
    worksheet = workbook.add_worksheet("A.6")




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
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 25)
    worksheet.set_column('E:E', 15)
    worksheet.merge_range('A3:G3', 'A.6 BUKU TANAH DI DESA',head)
    worksheet.merge_range('A4:G4', 'DESA CIKONENG KABUPATEN BANDUNG',head)



    worksheet.write("A6","NO. URUT",addon)
    worksheet.write("B6","NAMA PERORANGAN / BADAN HUKUM",addon)
    worksheet.write("C6","LUAS TANAH (M2)",addon)
    worksheet.write("D6","STATUS HAK TANAH",addon)
    worksheet.write("E6","PENGGUNAAN TANAH",addon)

    worksheet.write("A7","1",addon)
    worksheet.write("B7","2",addon)
    worksheet.write("C7","3",addon)
    worksheet.write("D7","4",addon)
    worksheet.write("E7","5",addon)



    bulks = []
    for i in data:
        data2 = {}
        data2["nama_perorangan_badan_hukum"] = i.get("pemilik").get("nama_perorangan_badan_hukum")
        data2["luas_tanah"] = i.get("tanah").get("luas_tanah")
        data2["status_hak_tanah"] = i.get("tanah").get("status_hak_tanah")
        data2["penggunaan_tanah"] = i.get("tanah").get("penggunaan_tanah")  
        

        bulks.append(data2)


    for index, entry in enumerate(bulks):
        worksheet.write(index+6+1, 0, str(index+1),body)
        worksheet.write(index+6+1, 1, entry.get("nama_perorangan_badan_hukum"),body)
        worksheet.write(index+6+1, 2,entry.get('luas_tanah'),body )
        worksheet.write(index+6+1, 3, entry.get("status_hak_tanah"),body)
        worksheet.write(index+6+1, 4, entry.get("penggunaan_tanah"),body)
        

    workbook.close()