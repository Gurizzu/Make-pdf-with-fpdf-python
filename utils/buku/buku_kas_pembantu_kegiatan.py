from xlsxwriter import Workbook

async def buku_kas_pembantu_kegiatan(data):
    workbook = Workbook("download/buku/buku_kas_pembantu_kegiatan.xlsx")
    worksheet = workbook.add_worksheet("C.3")




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


    worksheet.merge_range('A3:H3', 'C.3 BUKU KAS PEMBANTU KEGIATAN',head)
    worksheet.merge_range('A4:H4', 'DESA CIKONENG KABUPATEN BANDUNG',head)




    worksheet.merge_range("A7:A8","NO. URUT",addon)
    worksheet.merge_range("B7:B8","TANGGAL",addon)
    worksheet.merge_range("C7:C8","KETERANGAN",addon)
    worksheet.merge_range("D7:E7","PENERIMAAN (Rp.)",addon)
    worksheet.merge_range("F7:F8","NOMOR BUKTI",addon)
    worksheet.merge_range("G7:H7","PENGELUARAN",addon)
    worksheet.merge_range("I7:I8","JUMLAH PENGEMBALIAN KE BENDAHARA",addon)
    worksheet.merge_range("J7:J8","SALDO KAS (Rp.)",addon)

    worksheet.write("D8","DARI BENDAHARA",addon)
    worksheet.write("E8","SWADAYA MASYARAKAT",addon)
    worksheet.write("G8","BELANJA BARANG DAN JASA",addon)
    worksheet.write("H8","BELANJA MODAL",addon)


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
        data2["tanggal"] = i.get("tanggal")
        data2["keterangan"] = i.get("keterangan")
        data2["dari_bendahara"] = i.get("penerimaan_kegiatan").get("dari_bendahara")
        data2["swadaya_masyarakat"] = i.get("penerimaan_kegiatan").get("swadaya_masyarakat")
        data2["nomor_bukti"] = i.get("nomor_bukti")
        data2["belanja_barang_dan_jasa"] = i.get("pengeluaran_kegiatan").get("belanja_barang_dan_jasa")
        data2["belanja_modal"] = i.get("pengeluaran_kegiatan").get("belanja_modal")
        data2["jumlah_pengembalian_ke_bendahara"] = i.get("jumlah_pengembalian_ke_bendahara")
        data2["saldo"] = i.get("saldo")
        
        

        bulks.append(data2)


    for index, entry in enumerate(bulks):
        worksheet.write(index+8+1, 0, str(index+1),body)
        worksheet.write(index+8+1, 1, entry.get("tanggal"),body)
        worksheet.write(index+8+1, 2,entry.get('keterangan'),body )
        worksheet.write(index+8+1, 3, entry.get("dari_bendahara"),body)
        worksheet.write(index+8+1, 4, entry.get("swadaya_masyarakat"),body)
        worksheet.write(index+8+1, 5, entry.get("nomor_bukti"),body)
        worksheet.write(index+8+1, 6, entry.get("belanja_barang_dan_jasa"),body)
        worksheet.write(index+8+1, 7, entry.get("belanja_modal"),body)
        worksheet.write(index+8+1, 8, entry.get("jumlah_pengembalian_ke_bendahara"),body)
        worksheet.write(index+8+1, 9, entry.get("saldo"),body)
        
        

    workbook.close()
