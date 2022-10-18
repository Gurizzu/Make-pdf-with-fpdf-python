from xlsxwriter import Workbook


async def buku_aparat_pemerintah_desa(data:dict):
    workbook = Workbook("download/buku/buku_aparat_pemerintah_desa.xlsx")
    worksheet = workbook.add_worksheet("A.4")


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
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 15)
    worksheet.set_column('H:H', 20)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 25)
    worksheet.set_column('K:K', 20)
    worksheet.set_column('L:L', 20)
    worksheet.set_column('M:M', 20)
    worksheet.merge_range('A3:G3', 'A.4 BUKU APARAT PEMERINTAH DESA',head)
    worksheet.merge_range('A4:G4', 'DESA CIKONENG KABUPATEN BANDUNG',head)



    worksheet.write("A6","NO. URUT",addon)
    worksheet.write("B6","NAMA",addon)
    worksheet.write("C6","NIAP",addon)
    worksheet.write("D6","NIP",addon)
    worksheet.write("E6","JENIS KELAMIN",addon)
    worksheet.write("F6","TEMPAT DAN TANGGAL LAHIR",addon)
    worksheet.write("G6","AGAMA",addon)
    worksheet.write("H6","PANGKAT GOLONGAN",addon)
    worksheet.write("I6","JABATAN",addon)
    worksheet.write("J6","PENDIDIKAN TERAKHIR",addon)
    worksheet.write("K6","NOMOR DAN TANGGAL KEPUTUSAN PENGANGKATAN",addon)
    worksheet.write("L6","NOMOR DAN TANGGAL KEPUTUSAN PEMBERHENTIAN",addon)
    worksheet.write("M6","KETERANGAN",addon)

    worksheet.write("A7","1",addon)
    worksheet.write("B7","2",addon)
    worksheet.write("C7","3",addon)
    worksheet.write("D7","4",addon)
    worksheet.write("E7","5",addon)
    worksheet.write("F7","6",addon)
    worksheet.write("G7","7",addon)
    worksheet.write("H7","8",addon)
    worksheet.write("I7","9",addon)
    worksheet.write("J7","10",addon)
    worksheet.write("K7","11",addon)
    worksheet.write("L7","12",addon)
    worksheet.write("M7","13",addon)



    bulks = []
    for i in data:
        data2 = {}
        data2["nama"] = i.get("nama")
        data2["niap_nikd_nipd"] = i.get("niap_nikd_nipd")
        data2["nip"] = i.get("nip")
        data2["jenis_kelamin"] = i.get("jenis_kelamin")
        data2["tempat_tanggal_lahir"] = f"{i.get('tempat_lahir')}, {i.get('tanggal_lahir')}"
        data2["agama"] = i.get("agama")
        data2["pangkat_golongan"] = i.get("pangkat_golongan")
        data2["jabatan"] = i.get("jabatan")
        data2["pendidikan_terakhir"] = i.get("pendidikan_terakhir")   
        data2["nomor_dan_tanggal_keputusan_pengangkatan"] =  f"{i.get('nomor_keputusan_pengangkatan')}/{i.get('tanggal_keputusan_pengangkatan')}"
        data2["nomor_dan_tanggal_keputusan_pemberhentian"] =  f"{i.get('nomor_keputusan_pengangkatan')}/{i.get('tanggal_keputusan_pemberhentian')}"   
        data2["keterangan"] = i.get("keterangan")   
        
        

        bulks.append(data2)


    for index, entry in enumerate(bulks):
        worksheet.write(index+6+1, 0, str(index+1),body)
        worksheet.write(index+6+1, 1, entry.get("nama"),body)
        worksheet.write(index+6+1, 2,entry.get('niap_nikd_nipd'),body )
        worksheet.write(index+6+1, 3, entry.get("nip"),body)
        worksheet.write(index+6+1, 4, entry.get("jenis_kelamin"),body)
        worksheet.write(index+6+1, 5, entry.get("tempat_tanggal_lahir"),body)
        worksheet.write(index+6+1, 6, entry.get("agama"),body)
        worksheet.write(index+6+1, 7,entry.get('pangkat_golongan'),body )
        worksheet.write(index+6+1, 8, entry.get("jabatan"),body)
        worksheet.write(index+6+1, 9, entry.get("pendidikan_terakhir"),body)
        worksheet.write(index+6+1, 10, entry.get("nomor_dan_tanggal_keputusan_pengangkatan"),body)
        worksheet.write(index+6+1, 11, entry.get("nomor_dan_tanggal_keputusan_pemberhentian"),body)
        worksheet.write(index+6+1, 12, entry.get("keterangan"),body)
        

    workbook.close()
