from xlsxwriter import Workbook


async def buku_rencana_anggaran_biaya(data:dict):
    workbook = Workbook("download/buku/buku_rencana_anggaran_biaya.xlsx")
    worksheet = workbook.add_worksheet("C.2")


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

    header_topleft = workbook.add_format(
        {
            "align": "left",
            "font": "Cambria",
            "font_size":"9",
            
        }
    )

    header_topright = workbook.add_format(
        {
            "align": "right",
            "font": "Cambria",
            "font_size":"9",
            
        }
    )



    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 10)
    worksheet.set_column('E:E', 25)
    worksheet.set_column('F:F', 25)
    worksheet.set_column('G:G', 25)
    worksheet.set_column('H:H', 25)
    worksheet.merge_range('A3:E3', 'C.2 BUKU RENCANA ANGGARAN BIAYA',head)
    worksheet.merge_range('A4:E4', 'DESA CIKONENG KABUPATEN BANDUNG',head)



    worksheet.merge_range("A7:A8","NO. URUT",addon)
    worksheet.merge_range("B7:B8","JENIS BARANG",addon)
    worksheet.merge_range("C7:C8","VOLUME",addon)
    worksheet.write("D7","HARGA SATUAN",addon)
    worksheet.write("D8","(Rp)",addon)
    worksheet.write("E7","JUMLAH",addon)
    worksheet.write("E8","(Rp)",addon)
    worksheet.merge_range("F7:F8","BIDANG",addon)
    worksheet.merge_range("G7:G8","KEGIATAN",addon)
    worksheet.merge_range("H7:H8","WAKTU",addon)








    worksheet.write("A9","1",addon)
    worksheet.write("B9","2",addon)
    worksheet.write("C9","3",addon)
    worksheet.write("D9","4",addon)
    worksheet.write("E9","5",addon)
    worksheet.write("F9","6",addon)
    worksheet.write("G9","6",addon)
    worksheet.write("G9","6",addon)


    bulks = []
    for i in data:
        data2 = {}
        data2["jenis_barang"] = i.get("jenis_barang")
        data2["volume_barang"] = 0 if not i.get("volume_barang") else i.get("volume_barang")
        data2["harga_satuan_barang"] = 0 if not i.get("harga_satuan_barang") else i.get("harga_satuan_barang")
        data2["bidang"] =i.get("bidang")
        data2["kegiatan"] =i.get("kegiatan")
        data2["tanggal_RAB"] =i.get("tanggal_RAB")
        
        

        bulks.append(data2)


    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1),body)
        worksheet.write(index+7+1, 1, entry.get("jenis_barang"),body)
        worksheet.write(index+7+1, 2,entry.get('volume_barang'),body )
        worksheet.write(index+7+1, 3, entry.get("harga_satuan_barang"),body)
        worksheet.write(index+7+1, 4, entry.get("volume_barang") * entry.get("harga_satuan_barang"),body)
        worksheet.write(index+7+1, 5, entry.get("bidang"),body)
        worksheet.write(index+7+1, 6, entry.get("kegiatan") ,body)
        worksheet.write(index+7+1, 7, entry.get("tanggal_RAB"),body)
        

    workbook.close()
