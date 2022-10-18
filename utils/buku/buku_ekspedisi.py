from xlsxwriter import Workbook


async def buku_ekspedisi(data:dict):
    workbook = Workbook("download/buku/buku_ekspedisi.xlsx")
    worksheet = workbook.add_worksheet("A.8")




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
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 35)
    worksheet.set_column('E:E', 25)
    worksheet.set_column('F:F', 20)

    worksheet.merge_range('A3:G3', 'A.7 BUKU EKSPEDISI',head)
    worksheet.merge_range('A4:G4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.write("A6","NO. URUT",addon)
    worksheet.write("B6","TANGGAL PENGIRIMAN",addon)
    worksheet.write("C6","TANGGAL DAN NOMOR SURAT",addon)
    worksheet.write("D6","ISI SINGKAT SURAT YANG DIKIRIM",addon)
    worksheet.write("E6","DITUNJUKAN KEPADA",addon)
    worksheet.write("F6","KETERANGAN",addon)

    worksheet.write("A7","1",addon)
    worksheet.write("B7","2",addon)
    worksheet.write("C7","3",addon)
    worksheet.write("D7","4",addon)
    worksheet.write("E7","5",addon)
    worksheet.write("F7","6",addon)



    bulks = []
    for i in data:
        data2 = {}
        data2["tanggal_pengiriman"] = str(i.get("tanggal_pengiriman"))
        data2["tanggal_surat"] = str(i.get("tanggal_surat"))
        data2["nomor_surat"] = str(i.get("nomor_surat"))
        data2["ditujukan_kepada"] = str(i.get("ditujukan_kepada"))
        data2["isi_singkat_surat"] = str(i.get("isi_singkat_surat"))
        data2["keterangan"] = str(i.get("keterangan"))
        
        

        bulks.append(data2)
        
        

    for index, entry in enumerate(bulks):
        worksheet.write(index+6+1, 0, str(index+1),body)
        worksheet.write(index+6+1, 1, entry.get("tanggal_pengiriman"),body)
        worksheet.write(index+6+1, 2,f"{entry.get('tanggal_surat')}/{entry.get('nomor_surat')}",body )
        worksheet.write(index+6+1, 3, entry.get("isi_singkat_surat"),body)
        worksheet.write(index+6+1, 4, entry.get("ditujukan_kepada"),body)
        worksheet.write(index+6+1, 5, entry.get("keterangan"),body)
        


    workbook.close()