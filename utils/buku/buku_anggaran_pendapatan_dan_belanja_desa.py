from xlsxwriter import Workbook


async def buku_anggaran_pendapatan_dan_belanja_desa(data:dict):
    workbook = Workbook("download/buku/buku_anggaran_pendapatan_dan_belanja_desa.xlsx")
    worksheet = workbook.add_worksheet("C.1")


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
            "text_wrap":True
        }
    )

    bodyleft = workbook.add_format(
        {
            "align": "left",
            "font": "Cambria",
            "font_size":"9",
            "border":True,
            "text_wrap":True
            
        }
    )

    bodyright = workbook.add_format(
        {
            "align": "right",
            "font": "Cambria",
            "font_size":"9",
            "text_wrap":True,
            "border":True
            
        }
    )

    body_head = workbook.add_format(
        {
            "align": "left",
            "font": "Cambria",
            "font_size":"9",
            "bg_color": "EFF8FF",
            "text_wrap":True,
            "border":True
            
        }
    )

    body_head2 = workbook.add_format(
        {
            "align": "left",
            "font": "Cambria",
            "font_size":"9",
            "border":True,
            "text_wrap":True,
            "bold": True
            
        }
    )




    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 30)


    worksheet.merge_range('A3:C3', 'C.1 BUKU ANGGARAN PENDAPATAN DAN BELANJA DESA',head)
    worksheet.merge_range('A4:C4', 'DESA CIKONENG KABUPATEN BANDUNG',head)


    worksheet.write("A6","NO. URUT",addon)
    worksheet.write("B6","URAIAN",addon)
    worksheet.write("C6","ANGGARAN (Rp)",addon)
    worksheet.write("A7","1",addon)
    worksheet.write("B7","2",addon)
    worksheet.write("C7","3",addon)



    pendapatan = [{
        "Pendapatan Asli Desa": data.get("pendapatan").get("pendapatan_asli_desa"),
        "Pendapatan Transfer": data.get("pendapatan").get("pendapatan_transfer"),
        "Pendapatan Lain Lain": data.get("pendapatan").get("pendapatan_lain_lain"),
    }]

    belanja = [{
        "Belanja Pegawai": data.get("belanja").get("belanja_pegawai"),
        "Belanja Barang dan Jasa": data.get("belanja").get("belanja_barang_dan_jasa"),
        "Belanja Modal": data.get("belanja").get("belanja_modal"),
    }]

    pembiayaan = [{
        "Penerimaan Pembiayaan": data.get("pembiayaan").get("penerimaan_pembiayaan"),
        "Pengeluaran Pembiayaan": data.get("pembiayaan").get("pengeluran_pembiayaan"),
    }]

    worksheet.write("A8","1",bodyleft)
    worksheet.write("B8","Pendapatan",body_head)
    worksheet.write("C8","",bodyleft)

    worksheet.write("A13","6",bodyleft)
    worksheet.write("B13","Belanja",body_head)
    worksheet.write("C13","",bodyleft)

    worksheet.write("A18","11",bodyleft)
    worksheet.write("B18","Pembiayaan",body_head)
    worksheet.write("C18","",bodyleft)


    for penda in pendapatan:
        for index, (key,val) in enumerate(penda.items()):
            worksheet.write(index+7+1, 0, str(index+2),bodyleft)
            worksheet.write(index+7+1, 1, key,bodyleft)
            worksheet.write(index+7+1, 2, val,bodyright)
            
    for bela in belanja:
        for index, (key,val) in enumerate(bela.items()):
            worksheet.write(index+12+1, 0, str(index+7),bodyleft)
            worksheet.write(index+12+1, 1, key,bodyleft)
            worksheet.write(index+12+1, 2, val,bodyright)
            
    for pembi in pembiayaan:
        for index, (key,val) in enumerate(pembi.items()):
            worksheet.write(index+17+1, 0, str(index+11),bodyleft)
            worksheet.write(index+17+1, 1, key,bodyleft)
            worksheet.write(index+17+1, 2, val,bodyright)
            
    worksheet.write("A12","5",bodyleft)
    worksheet.write("B12","Jumlah Pendapatan",body_head2)
    worksheet.write('C12', pendapatan[0].get("Pendapatan Asli Desa") + pendapatan[0].get("Pendapatan Transfer") + pendapatan[0].get("Pendapatan Lain Lain"),bodyright)

    worksheet.write("A17","11",bodyleft)
    worksheet.write("B17","Jumlah Belanja",body_head2)
    worksheet.write('C17', belanja[0].get("Belanja Pegawai") + belanja[0].get("Belanja Barang dan Jasa") + belanja[0].get( "Belanja Modal"),bodyright)

            

    workbook.close()