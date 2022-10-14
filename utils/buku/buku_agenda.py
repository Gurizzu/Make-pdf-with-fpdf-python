
from xlsxwriter import Workbook



async def buku_agenda(data:dict):
    workbook = Workbook("download/buku_agenda/buku_agenda.xlsx")
    worksheet = workbook.add_worksheet("A.7")




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
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 25)
    worksheet.set_column('G:G', 25)
    worksheet.set_column('H:H', 25)
    worksheet.set_column('I:I', 25)
    worksheet.set_column('J:J', 25)
    worksheet.set_column('K:K', 25)
    worksheet.set_column('L:L', 25)
    worksheet.merge_range('A3:G3', 'A.7 BUKU AGENDA',head)
    worksheet.merge_range('A4:G4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.merge_range('A6:A7', 'NO. URUT',addon)
    worksheet.merge_range('B6:B7', 'KODE PERSURATAN',addon)
    worksheet.merge_range('C6:C7', 'TANGGAL PENERIMAAN/ PENGIRIMAN SURAT',addon)
    worksheet.merge_range('D6:G6', 'SURAT MASUK',addon)
    worksheet.write("D7","NOMOR",addon)
    worksheet.write("E7","TANGGAL",addon)
    worksheet.write("F7","PENGIRIM",addon)
    worksheet.write("G7","ISI SINGKAT",addon)
    worksheet.write("H7","NOMOR",addon)
    worksheet.write("I7","TANGGAL",addon)
    worksheet.write("J7","DITUNJUKAN KEPADA",addon)
    worksheet.write("K7","ISI SURAT",addon)
    worksheet.merge_range('H6:K6', 'SURAT KELUAR',addon)
    worksheet.merge_range('L6:L7', 'KETERANGAN',addon)


    worksheet.write("A8","1",addon)
    worksheet.write("B8","2",addon)
    worksheet.write("C8","3",addon)
    worksheet.write("D8","4",addon)
    worksheet.write("E8","5",addon)
    worksheet.write("F8","6",addon)
    worksheet.write("G8","7",addon)
    worksheet.write("H8","8",addon)
    worksheet.write("I8","9",addon)
    worksheet.write("J8","10",addon)
    worksheet.write("K8","11",addon)
    worksheet.write("L8","12",addon)

    bulks = []
    for i in data:
        data2 = {}
        data2["kode_persuratan"] = str(i.get("kode_persuratan"))
        data2["tanggal_terima_kirim_surat"] = str(i.get("tanggal_terima_kirim_surat"))
        data2["nomor_surat_masuk"] = str(i.get("nomor_surat_masuk"))
        data2["tanggal_surat_masuk"] = str(i.get("tanggal_surat_masuk"))
        data2["pengirim"] = str(i.get("pengirim"))
        data2["isi_singkat_surat"] = str(i.get("isi_singkat_surat"))
        data2["nomor_surat_keluar"] = str(i.get("nomor_surat_keluar"))
        data2["tanggal_surat_keluar"] = str(i.get("tanggal_surat_keluar"))
        data2["ditujukan_kepada"] = str(i.get("ditujukan_kepada"))      
        data2["isi_singkat_surat"] = str(i.get("isi_singkat_surat"))   
        data2["keterangan"] = str(i.get("keterangan") )  
        
        

        bulks.append(data2)
        
        

    for index, entry in enumerate(bulks):
        worksheet.write(index+7+1, 0, str(index+1),body)
        worksheet.write(index+7+1, 1, entry.get("kode_persuratan"),body)
        worksheet.write(index+7+1, 2,entry.get('tanggal_terima_kirim_surat'),body )
        worksheet.write(index+7+1, 3, entry.get("nomor_surat_masuk"),body)
        worksheet.write(index+7+1, 4, entry.get("tanggal_surat_masuk"),body)
        worksheet.write(index+7+1, 5, entry.get("pengirim"),body)
        worksheet.write(index+7+1, 6, entry.get("isi_singkat_surat"),body)
        worksheet.write(index+7+1, 7, entry.get("nomor_surat_keluar"),body)
        worksheet.write(index+7+1, 8, entry.get("tanggal_surat_keluar"),body)
        worksheet.write(index+7+1, 9, entry.get("ditujukan_kepada"),body)
        worksheet.write(index+7+1, 10, entry.get("isi_singkat_surat"),body)
        worksheet.write(index+7+1, 11, entry.get("keterangan"),body)
        


    workbook.close()