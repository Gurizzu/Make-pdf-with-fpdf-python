from xlsxwriter import Workbook

async def buku_kas_pembantu(data:dict):
    workbook = Workbook("download/buku/buku_kas_pembantu.xlsx")
    worksheet = workbook.add_worksheet("C.5")




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
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 20)
    worksheet.set_column('H:H', 20)

    worksheet.merge_range('A3:H3', 'C.4 BUKU KAS PEMBANTU',head)
    worksheet.merge_range('A4:H4', 'DESA CIKONENG KABUPATEN BANDUNG',head)




    worksheet.merge_range("A6:A7","NO. URUT",addon)
    worksheet.merge_range("B6:B7","TANGGAL",addon)
    worksheet.merge_range("C6:E6","URAIAN",addon)
    worksheet.write("C7","PAJAK",addon)
    worksheet.write("D7","RET",addon)
    worksheet.write("E7","PL",addon)
    worksheet.write("F6","PEMOTONGAN",addon)
    worksheet.write("G6","PENYETORAN",addon)
    worksheet.write("H6","SALDO",addon)
    worksheet.write("F7","(Rp.)",addon)
    worksheet.write("G7","(Rp.)",addon)
    worksheet.write("H7","(Rp.)",addon)


    worksheet.write("A8","1",addon)
    worksheet.write("B8","2",addon)
    worksheet.write("C8","3",addon)
    worksheet.write("D8","4",addon)
    worksheet.write("E8","5",addon)
    worksheet.write("F8","6",addon)
    worksheet.write("G8","7",addon)
    worksheet.write("H8","8",addon)



    bulks = []
    for i in data:
        data2 = {}
        data2["tanggal"] = i.get("tanggal")
        data2["pajak"] = i.get("uraian").get("pajak")
        data2["RET"] = i.get("uraian").get("RET")
        data2["PL"] = i.get("uraian").get("PL")
        data2["pemotongan"] = i.get("pemotongan")
        data2["penyetoran"] = i.get("penyetoran")
        data2["saldo"] = i.get("saldo")
        
        

        bulks.append(data2)


    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1),body)
        worksheet.write(index+7+1, 1, entry.get("tanggal"),body)
        worksheet.write(index+7+1, 2,entry.get('pajak'),body )
        worksheet.write(index+7+1, 3, entry.get("RET"),body)
        worksheet.write(index+7+1, 4, entry.get("PL"),body)
        worksheet.write(index+7+1, 5, entry.get("pemotongan"),body)
        worksheet.write(index+7+1, 6, entry.get("penyetoran"),body)
        worksheet.write(index+7+1, 7, entry.get("saldo"),body)
        

    workbook.close()
