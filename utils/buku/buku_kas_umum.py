from xlsxwriter import Workbook

async def buku_kas_umum(data:dict):
    workbook = Workbook("download/buku/buku_kas_umum.xlsx")
    worksheet = workbook.add_worksheet("C.4")




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
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('F:F', 30)
    worksheet.set_column('G:G', 30)
    worksheet.set_column('H:H', 30)
    worksheet.set_column('I:I', 30)

    worksheet.merge_range('A3:I3', 'C.4 BUKU KAS UMUM',head)
    worksheet.merge_range('A4:I4', 'DESA CIKONENG KABUPATEN BANDUNG',head)




    worksheet.write("A7","NO. URUT",addon)
    worksheet.write("B7","TANGGAL",addon)
    worksheet.write("C7","KODE REKENING",addon)
    worksheet.write("D7","URAIAN",addon)
    worksheet.write("E7","PENERIMAAN (Rp)",addon)
    worksheet.write("F7","PENGELUARAN (Rp)",addon)
    worksheet.write("G7","NO. BUKTI",addon)
    worksheet.write("H7","JUMLAH PENGELUARAN KOMULATIF",addon)
    worksheet.write("I7","SALDO",addon)

    worksheet.write("A8","1",addon)
    worksheet.write("B8","2",addon)
    worksheet.write("C8","3",addon)
    worksheet.write("D8","4",addon)
    worksheet.write("E8","5",addon)
    worksheet.write("F8","6",addon)
    worksheet.write("G8","7",addon)
    worksheet.write("H8","8",addon)
    worksheet.write("I8","9",addon)




    bulks = []
    for i in data:
        data2 = {}
        data2["tanggal"] = i.get("tanggal")
        data2["kode_rekening"] = i.get("kode_rekening")
        data2["uraian"] = i.get("uraian")
        data2["penerimaan"] = i.get("penerimaan")
        data2["pengeluaran"] = i.get("pengeluaran")
        data2["nomor_bukti"] = i.get("nomor_bukti")
        data2["jumlah_pengeluaran_komulatif"] = i.get("jumlah_pengeluaran_komulatif")
        data2["saldo"] = i.get("saldo")
        
        

        bulks.append(data2)
        


    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1),body)
        worksheet.write(index+7+1, 1, entry.get("tanggal"),body)
        worksheet.write(index+7+1, 2,entry.get('kode_rekening'),body )
        worksheet.write(index+7+1, 3, entry.get("uraian"),body)
        worksheet.write(index+7+1, 4, entry.get("penerimaan"),body)
        worksheet.write(index+7+1, 5, entry.get("pengeluaran"),body)
        worksheet.write(index+7+1, 6, entry.get("nomor_bukti"),body)
        worksheet.write(index+7+1, 7, entry.get("jumlah_pengeluaran_komulatif"),body)
        worksheet.write(index+7+1, 8, entry.get("saldo"),body)
        

    workbook.close()