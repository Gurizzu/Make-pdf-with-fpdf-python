from xlsxwriter import Workbook


async def buku_inventaris_kekayaan_desa(data:dict):
    workbook = Workbook("download/buku/buku_inventaris_kekayaan_desa.xlsx")
    worksheet = workbook.add_worksheet("A.3")



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
            "text_wrap": True
        }
    )

    body = workbook.add_format(
        {
            "align": "center",
            "font": "Cambria",
            "font_size":"9",
            "border":True,
            "text_wrap": True
            
        }
    )


    worksheet.set_column('A:P', 18)
    worksheet.merge_range('A3:P3', 'A.3 BUKU INVENTARIS DAN KEKAYAAN DESA',head)
    worksheet.merge_range('A4:P4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.merge_range('A6:A8', 'NO. URUT',addon)
    worksheet.merge_range('B6:B8', 'JENIS BARANG/BANGUNAN',addon)
    worksheet.merge_range('C6:G6', 'ASAL BARANG/BANGUNAN',addon)
    worksheet.merge_range('H6:I6', 'KEADAAN BARANG/BANGUNAN',addon)
    worksheet.merge_range('J6:M6', 'PENGHAPUSAN BARANG DAN BANGUNAN',addon)
    worksheet.merge_range('N6:O6', 'KEADAAN BARANG/BANGUNAN',addon)
    worksheet.merge_range('P6:P8', 'KETERANGAN',addon)
    worksheet.merge_range('C7:C8', 'DIBELI SENDIRI',addon)
    worksheet.merge_range('D7:F7', 'BANTUAN',addon)
    worksheet.write("D8","PEMERINTAH",addon)
    worksheet.write("E8","PROVINSI",addon)
    worksheet.write("F8","KAB/KOTA",addon)
    worksheet.merge_range('G7:G8', 'SUMBANGAN',addon)
    worksheet.merge_range('H7:H8', 'BAIK',addon)
    worksheet.merge_range('I7:I8', 'RUSAK',addon)
    worksheet.merge_range('J7:J8', 'RUSAK',addon)
    worksheet.merge_range('K7:K8', 'DIJUAL',addon)
    worksheet.merge_range('L7:L8', 'DISUMBANGKAN',addon)
    worksheet.merge_range('M7:M8', 'TANGGAL PENGHAPUSAN',addon)
    worksheet.merge_range('N7:N8', 'BAIK',addon)
    worksheet.merge_range('O7:O8', 'RUSAK',addon)


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
    worksheet.write("K9","11",addon)
    worksheet.write("L9","12",addon)
    worksheet.write("M9","13",addon)
    worksheet.write("N9","14",addon)
    worksheet.write("O9","15",addon)
    worksheet.write("P9","16",addon)


    bulks = []
    for i in data:
        data2 = {}
        
        data2["jenis_barang"] = i.get("jenis_barang")
        data2["keterangan"] = i.get("keterangan")
        
        if i.get("penghapusan_barang_dan_bangunan"):
            data2["disumbangkan"] = i.get("penghapusan_barang_dan_bangunan").get("disumbangkan")
            data2["dijual"] = i.get("penghapusan_barang_dan_bangunan").get("dijual")
            data2["penghapusan_barang_dan_bangunan_rusak"] = i.get("penghapusan_barang_dan_bangunan").get("rusak")
            data2["tanggal_dihapus"] = i.get("penghapusan_barang_dan_bangunan").get("tanggal_dihapus")
            
            

        if i.get("keadaan_barang_bangunan_awal_tahun"):
            data2["keadaan_barang_bangunan_awal_tahun_baik"] = i.get("keadaan_barang_bangunan_awal_tahun").get("baik")
            data2["keadaan_barang_bangunan_awal_tahun_rusak"] = i.get("keadaan_barang_bangunan_awal_tahun").get("rusak")
        
        if i.get("keadaan_barang_bangunan_akhir_tahun"):
            data2["keadaan_barang_bangunan_akhir_tahun_baik"] = i.get("keadaan_barang_bangunan_akhir_tahun").get("baik")
            data2["keadaan_barang_bangunan_akhir_tahun_rusak"] = i.get("keadaan_barang_bangunan_akhir_tahun").get("rusak")
            
        
        if i.get("asal_barang_bangunan"):
            data2["dibeli_sendiri"] = i.get("asal_barang_bangunan").get("dibeli_sendiri")
            data2["bantuan_pemerintah"] = i.get("asal_barang_bangunan").get("bantuan_pemerintah")
            data2["bantuan_provinsi"] = i.get("asal_barang_bangunan").get("bantuan_provinsi")
            data2["bantuan_kabupaten_kota"] = i.get("asal_barang_bangunan").get("bantuan_kabupaten_kota")
            data2["sumbangan"] = i.get("asal_barang_bangunan").get("sumbangan")
            
        
        bulks.append(data2)
            

    for index, entry in enumerate(bulks):
        worksheet.write(index+8+1, 0, str(index+1),body)
        worksheet.write(index+8+1, 1, entry.get("jenis_barang"),body)
        worksheet.write(index+8+1, 2,entry.get('dibeli_sendiri'),body )
        worksheet.write(index+8+1, 3, entry.get("bantuan_pemerintah"),body)
        worksheet.write(index+8+1, 4, entry.get("bantuan_provinsi"),body)
        worksheet.write(index+8+1, 5, entry.get("bantuan_kabupaten_kota"),body)
        worksheet.write(index+8+1, 6, entry.get("sumbangan"),body)
        worksheet.write(index+8+1, 7, entry.get("keadaan_barang_bangunan_awal_tahun_baik"),body)
        worksheet.write(index+8+1, 8, entry.get("keadaan_barang_bangunan_akhir_tahun_rusak"),body)
        worksheet.write(index+8+1, 9, entry.get("penghapusan_barang_dan_bangunan_rusak"),body)
        worksheet.write(index+8+1, 10, entry.get("dijual"),body)
        worksheet.write(index+8+1, 11, entry.get("disumbangkan"),body)
        worksheet.write(index+8+1, 12, entry.get("tanggal_dihapus"),body)
        worksheet.write(index+8+1, 13, entry.get("keadaan_barang_bangunan_akhir_tahun_baik"),body)
        worksheet.write(index+8+1, 14, entry.get("keadaan_barang_bangunan_akhir_tahun_rusak"),body)
        worksheet.write(index+8+1, 15, entry.get("keterangan"),body)
        
    workbook.close()