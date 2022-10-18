from xlsxwriter import Workbook

async def buku_bank_desa(data:dict):
    workbook = Workbook("download/buku/buku_bank_desa.xlsx")
    worksheet = workbook.add_worksheet("C.6")




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
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 25)
    worksheet.set_column('E:E', 15)
    worksheet.set_column('F:F', 15)
    worksheet.set_column('G:G', 15)
    worksheet.set_column('H:H', 15)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)


    worksheet.merge_range('A3:H3', 'C.6 BUKU BANK DESA',head)
    worksheet.merge_range('A4:H4', 'DESA CIKONENG KABUPATEN BANDUNG',head)




    worksheet.merge_range("A6:A8","NO. URUT",addon)
    worksheet.merge_range("B6:B8","TANGGAL TRANSAKSI",addon)
    worksheet.merge_range("C6:C8","URAIAN TRANSAKSI",addon)
    worksheet.merge_range("D6:D8","BUKTI TRANSAKSI",addon)
    worksheet.merge_range("E6:F6","PEMASUKAN",addon)
    worksheet.merge_range("G6:I6","PENGELUARAN",addon)
    worksheet.merge_range("J6:J8","SALDO",addon)
    worksheet.write("E7","SETORAN",addon)
    worksheet.write("F7","BUNGA BANK",addon)
    worksheet.write("G7","PENARIKAN",addon)
    worksheet.write("H7","PAJAK",addon)
    worksheet.write("I7","BIAYA ADMINISTRASI",addon)
    worksheet.write("E8","(Rp.)",addon)
    worksheet.write("F8","(Rp.)",addon)
    worksheet.write("G8","(Rp.)",addon)
    worksheet.write("H8","(Rp.)",addon)
    worksheet.write("I8","(Rp.)",addon)





    worksheet.write("A9","1",addon)
    worksheet.write("B9","2",addon)
    worksheet.write("C9","3",addon)
    worksheet.write("D9","4",addon)
    worksheet.write("E9","5",addon)
    worksheet.write("F9","6",addon)
    worksheet.write("G9","7",addon)
    worksheet.write("H9","8",addon)
    worksheet.write("I9","9",addon)
    worksheet.write("J9","10",addon)





    bulks = []
    for i in data:
        data2 = {}
        data2["tanggal_transaksi"] = i.get("tanggal_transaksi")
        data2["uraian_transaksi"] = i.get("uraian_transaksi")
        data2["bukti_transaksi"] = i.get("bukti_transaksi")
        data2["setoran"] = i.get("pemasukan").get("setoran")
        data2["bunga_bank"] = i.get("pemasukan").get("bunga_bank")
        data2["penarikan"] = i.get("pengeluaran").get("penarikan")
        data2["pajak"] = i.get("pengeluaran").get("pajak")
        data2["biaya_administrasi"] = i.get("pengeluaran").get("biaya_administrasi")
        data2["saldo"] = i.get("saldo")
        
        

        bulks.append(data2)


    for index, entry in enumerate(bulks):
        worksheet.write(index+8+1, 0, str(index+1),body)
        worksheet.write(index+8+1, 1, entry.get("tanggal_transaksi"),body)
        worksheet.write(index+8+1, 2,entry.get('uraian_transaksi'),body )
        worksheet.write(index+8+1, 3, entry.get("bukti_transaksi"),body)
        worksheet.write(index+8+1, 4, entry.get("setoran"),body)
        worksheet.write(index+8+1, 5, entry.get("bunga_bank"),body)
        worksheet.write(index+8+1, 6, entry.get("penarikan"),body)
        worksheet.write(index+8+1, 7, entry.get("pajak"),body)
        worksheet.write(index+8+1, 8, entry.get("biaya_administrasi"),body)
        worksheet.write(index+8+1, 9, entry.get("saldo"),body)
        
        

    workbook.close()