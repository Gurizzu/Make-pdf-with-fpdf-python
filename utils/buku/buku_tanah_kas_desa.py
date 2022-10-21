from xlsxwriter import Workbook

async def buku_tanah_kas_desa(data):
    bulks = []
    for i in data:
        data2 = {}
        data2["asal_tanah_kas_desa"] = str(i.get("asal_tanah_kas_desa"))
        data2["nomor_sertifikat_buku_letter"] = str(i.get("nomor_sertifikat_buku_letter"))
        data2["luas"] = str(i.get("luas"))
        data2["kelas"] = str(i.get("kelas"))
        data2["lokasi"] = str(i.get("lokasi"))
        data2["peruntukan"] = str(i.get("peruntukan"))
        data2["mutasi"] = str(i.get("mutasi"))
        data2["keterangan"] = str(i.get("keterangan"))

        if i.get("perolehan_tkd"):
            data2["asal_milik_desa"] = str(i.get("perolehan_tkd").get("asal_milik_desa"))
            data2["bantuan_pemerintah"] = str(i.get("perolehan_tkd").get("bantuan_pemerintah"))
            data2["bantuan_provinsi"] = str(i.get("perolehan_tkd").get("bantuan_provinsi"))
            data2["bantuan_kabupaten_kota"] = str(i.get("perolehan_tkd").get("bantuan_kabupaten_kota"))
            data2["lain_lain"] = str(i.get("perolehan_tkd").get("lain_lain"))
            data2["tanggal_perolehan"] = str(i.get("perolehan_tkd").get("tanggal_perolehan"))

        if i.get("jenis_tkd"):
            data2["sawah"] = str(i.get("jenis_tkd").get("sawah"))
            data2["tambak_kolam"] = str(i.get("jenis_tkd").get("tambak_kolam"))
            data2["tanah_kering_darat"] = str(i.get("jenis_tkd").get("tanah_kering_darat"))
            data2["tegal"] = str(i.get("jenis_tkd").get("tegal"))
            data2["kebun"] = str(i.get("jenis_tkd").get("kebun"))

        if i.get("patok_tanda_batas"):
            data2["patok_tidak_ada"] = str(i.get("patok_tanda_batas").get("tidak_ada"))
            data2["patok_ada"] = str(i.get("patok_tanda_batas").get("ada"))

        if i.get("papan_nama"):
            data2["papan_ada"] = str(i.get("papan_nama").get("ada"))
            data2["papan_tidak_ada"] = str(i.get("papan_nama").get("tidak_ada"))
        bulks.append(data2)

    workbook = Workbook("download/buku/buku_tanah_kas_desa.xlsx")
    worksheet = workbook.add_worksheet("A.5")


    addon = workbook.add_format(
        {
            "font": "Cambria",
            "align": "center",
            "font_size":"9",
            "border":True,
            "bg_color":"#EDEDED",
            "text_wrap" : True
        }
    )
    addon.set_align('vcenter')

    head = workbook.add_format(
        {
            "align": "center",
            "font": "Cambria",
            "font_size": "11",
        }
    )

    content = workbook.add_format(
        {
            "font": "Cambria",
            "align": "center",
            "font_size":"9",
            "border":True,
            "text_wrap" : True
        }
    )
    content.set_align('vcenter')


    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 25)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('F:F', 12)
    worksheet.set_column('G:G', 12)
    worksheet.set_column('H:H', 12)
    worksheet.set_column('I:I', 12)
    worksheet.set_column('J:J', 12)
    worksheet.set_column('K:K', 12)
    worksheet.set_column('L:L', 15)
    worksheet.set_column('M:M', 15)
    worksheet.set_column('N:N', 15)
    worksheet.set_column('O:O', 15)
    worksheet.set_column('P:P', 15)
    worksheet.set_column('Q:Q', 11.5)
    worksheet.set_column('R:R', 11.5)
    worksheet.set_column('S:S', 11.5)
    worksheet.set_column('T:T', 11.5)
    worksheet.set_column('U:U', 15)
    worksheet.set_column('V:V', 17)
    worksheet.set_column('W:W', 15)
    worksheet.set_column('X:X', 15)
    worksheet.merge_range('A3:X3', 'A.5 BUKU TANAH KAS DESA',head)
    worksheet.merge_range('A4:X4', 'DESA CIKONENG KABUPATEN BANDUNG',head)

    
    worksheet.merge_range('A6:A10', 'NO. URUT',addon)
    worksheet.merge_range('B6:B10', 'ASAL TANAH KAS DESA',addon)
    worksheet.merge_range('C6:C10', 'NOMOR SERTIFIKAT BUKU LETTER C/ PERSIL',addon)
    worksheet.merge_range('D6:D10', 'LUAS (m)',addon)
    worksheet.merge_range('E6:E10', 'KELAS',addon)
    worksheet.merge_range('F6:K8', 'PEROLEHAN TANAH KAS DESA',addon)
    worksheet.merge_range('F9:F10', 'ASLI MILIK DESA',addon)
    worksheet.merge_range('G9:I9', 'BANTUAN',addon)
    worksheet.write('G10', 'PEMERINTAH',addon)
    worksheet.write('H10', 'PROV',addon)
    worksheet.write('I10', 'KAB/KOTA',addon)
    worksheet.merge_range('J9:J10', 'LAIN LAIN',addon)
    worksheet.merge_range('K9:K10', 'TANGGAL PEROLEHAN',addon)
    worksheet.merge_range('L6:P8', 'JENIS TANAH KAS DESA',addon)
    worksheet.merge_range('L9:L10', 'SAWAH',addon)
    worksheet.merge_range('M9:M10', 'TEGAL',addon)
    worksheet.merge_range('N9:N10', 'KEBUN',addon)
    worksheet.merge_range('O9:O10', 'TAMBAK/KOLAM',addon)
    worksheet.merge_range('P9:P10', 'TANAH KERING/DARAT',addon)
    worksheet.merge_range('Q6:R8', 'PATOK TANDA BATAS',addon)
    worksheet.merge_range('Q9:Q10', 'ADA',addon)
    worksheet.merge_range('R9:R10', 'TIDAK ADA',addon)
    worksheet.merge_range('S6:T8', 'PAPAN NAMA',addon)
    worksheet.merge_range('S9:S10', 'ADA',addon)
    worksheet.merge_range('T9:T10', 'TIDAK ADA',addon)
    worksheet.merge_range('U6:U10', 'LOKASI',addon)
    worksheet.merge_range('V6:V10', 'PERUNTUKAN',addon)
    worksheet.merge_range('W6:W10', 'MUTASI',addon)
    worksheet.merge_range('X6:X10', 'KETERANGAN',addon)

    worksheet.write('A11', "1",addon)
    worksheet.write('B11', "2",addon)
    worksheet.write('C11', "3",addon)
    worksheet.write('D11', "4",addon)
    worksheet.write('E11', "5",addon)
    worksheet.write('F11', "6",addon)
    worksheet.write('G11', "7",addon)
    worksheet.write('H11', "8",addon)
    worksheet.write('I11', "9",addon)
    worksheet.write('J11', "10",addon)
    worksheet.write('K11', "11",addon)
    worksheet.write('L11', "12",addon)
    worksheet.write('M11', "13",addon)
    worksheet.write('N11', "14",addon)
    worksheet.write('O11', "15",addon)
    worksheet.write('P11', "16",addon)
    worksheet.write('Q11', "17",addon)
    worksheet.write('R11', "18",addon)
    worksheet.write('S11', "19",addon)
    worksheet.write('T11', "20",addon)
    worksheet.write('U11', "21",addon)
    worksheet.write('V11', "22",addon)
    worksheet.write('W11', "23",addon)
    worksheet.write('X11', "24",addon)


    for index, entry in enumerate(bulks):
        worksheet.write(index+10+1, 0, str(index+1), content)
        worksheet.write(index+10+1, 1, entry.get('asal_tanah_kas_desa'), content)
        worksheet.write(index+10+1, 2, entry.get('nomor_sertifikat_buku_letter'),content)
        worksheet.write(index+10+1, 3, entry.get('luas'),content)
        worksheet.write(index+10+1, 4, entry.get('kelas'),content)
        worksheet.write(index+10+1, 5, entry.get('asal_milik_desa'),content)
        worksheet.write(index+10+1, 6, entry.get('bantuan_pemerintah'),content)
        worksheet.write(index+10+1, 7, entry.get('bantuan_provinsi'),content)
        worksheet.write(index+10+1, 8, entry.get('bantuan_kabupaten_kota'),content)
        worksheet.write(index+10+1, 9, entry.get('lain-lain'),content)
        worksheet.write(index+10+1, 10, entry.get('tanggal_perolehan'),content)
        worksheet.write(index+10+1, 11, entry.get('sawah'),content)
        worksheet.write(index+10+1, 12, entry.get('tegal'),content)
        worksheet.write(index+10+1, 13, entry.get('kebun'),content)
        worksheet.write(index+10+1, 14, entry.get('tambak_kolam'),content)
        worksheet.write(index+10+1, 15, entry.get('tambak_kering_darat'),content)
        worksheet.write(index+10+1, 16, entry.get('patok_ada'),content)
        worksheet.write(index+10+1, 17, entry.get('patok_tidak_ada'),content)
        worksheet.write(index+10+1, 18, entry.get('papan_ada'),content)
        worksheet.write(index+10+1, 19, entry.get('papan_tidak_ada'),content)
        worksheet.write(index+10+1, 20, entry.get('lokasi'),content)
        worksheet.write(index+10+1, 21, entry.get('peruntukan'),content)
        worksheet.write(index+10+1, 22, entry.get('mutasi'),content)
        worksheet.write(index+10+1, 23, entry.get('keterangan'),content)

    workbook.close()