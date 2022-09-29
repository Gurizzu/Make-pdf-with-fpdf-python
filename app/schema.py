from pydantic import BaseModel

class SuratDomisiliForm(BaseModel):
    nomor_surat: str
    nama_pembuat_surat: str
    nik_pembuat_surat:str
    jenis_kelamin_pembuat_surat:str
    tempat_tanggal_lahir_pembuat_surat: str
    agama_pembuat_surat: str
    pekerjaan_pembuat_surat:str
    status_perkawinan_pembuat_surat:str
    alamat_pembuat_surat:str
    penanda_tangan_surat:str
    nip_penandatangan_surat:str
    class Config:
        schema_extra = {
            "example": {
                "nomor_surat": "202/0013/TR/1/2021",
                "nama_pembuat_surat": "ALEX NOERDIN",
                "nik_pembuat_surat":"3120910992820001",
                "jenis_kelamin_pembuat_surat":"Laki - Laki",
                "tempat_tanggal_lahir_pembuat_surat": "BANDUNG, 12-08-1992",
                "agama_pembuat_surat": "ISLAM",
                "pekerjaan_pembuat_surat":"PEGAWAI NEGERI SIPIL",
                "status_perkawinan_pembuat_surat":"BELUM KAWIN",
                "alamat_pembuat_surat":"DUSUN SUKAMAJU, RT 11 RW 001",
                "penanda_tangan_surat":"Mustahiq, S.Adm",
                "nip_penandatangan_surat":"1918718001902981920"
            }
        }

class SuratKematianForm(BaseModel):
    nomor_surat: str
    nama_almarhum: str
    nama_bapak_almarhum:str
    tempat_tanggal_lahir_almarhum:str
    alamat_lengkap_almarhum:str
    agama_almarhum:str
    status_perkawinan_almarhum:str
    pekerjaan_almarhum:str
    kewarganegaraan_almarhum:str
    nik_almarhum:str
    tanggal_meninggal_almarhum:str
    jam_meninggal_almarhum:str
    tempat_meninggal_almarhum:str
    penyebab_kematian_almarhum:str
    nama_pelapor_kematian:str
    jenis_kelamin_pelapor:str
    alamat_lengkap_pelapor:str
    hubungan_pelapor_dengan_almarhum:str
    penanda_tangan_surat:str
    nip_penandatangan_surat:str
    class Config:
        schema_extra = {
            "example": {
              "nomor_surat": "202/0013/TR/1/2021",
              "nama_almarhum": "Winata",
              "nama_bapak_almarhum": "Pulan",
              "tempat_tanggal_lahir_almarhum": "Laki-Laki",
              "alamat_lengkap_almarhum": "Kp. Nagrak RT.002 RW 008, Desa Sukajaya, Kecamatan Ciparay, Kabupaten Bandung Barat",
              "agama_almarhum": "Islam",
              "status_perkawinan_almarhum": "Kawin",
              "pekerjaan_almarhum": "Wiraswasta",
              "kewarganegaraan_almarhum":"WNI",
              "nik_almarhum": "312510291029109",
              "tanggal_meninggal_almarhum": "2 Januari 2022",
              "jam_meninggal_almarhum": "15 : 30",
              "tempat_meninggal_almarhum" : "Rumah",
              "penyebab_kematian_almarhum": "Sakit",
              "nama_pelapor_kematian": "Deden Hidayat",
              "jenis_kelamin_pelapor": "Laki-Laki",
              "alamat_lengkap_pelapor": "Kp. Nagrak RT.002 RW 008, Desa Sukajaya, Kecamatan Ciparay, Kabupaten Bandung Barat",
              "hubungan_pelapor_dengan_almarhum":"Anak",
              "penanda_tangan_surat":"Mustahiq, S.Adm",
              "nip_penandatangan_surat":"1918718001902981920"
            }
        }

class SuratNikahForm(BaseModel):
    nomor_surat: str
    nama_mempelai:str
    tempat_tanggal_lahir_mempelai:str
    jenis_kelamin_mempelai:str
    agama_mempelai:str
    pekerjaan_mempelai:str
    status_mempelai:str
    dusun_mempelai:str
    nama_ayah_mempelai:str
    tempat_tanggal_lahir_ayah_mempelai:str
    agama_ayah_mempelai:str
    pekerjaan_ayah_mempelai:str
    alamat_ayah_mempelai:str
    nama_ibu_mempelai:str
    tempat_tanggal_lahir_ibu_mempelai:str
    agama_ibu_mempelai:str
    pekerjaan_ibu_mempelai:str
    alamat_ibu_mempelai:str
    penanda_tangan_surat:str
    nip_penandatangan_surat:str
    class Config:
        schema_extra = {
            "example": {
                "nomor_surat": "202/0013/TR/1/2021",
                "nama_mempelai": "Ibnu Muhammad Arbain",
                "tempat_tanggal_lahir_mempelai": "Samarinda, 14 Maret 1989",
                "jenis_kelamin_mempelai": "Laki-Laki",
                "agama_mempelai": "Islam",
                "pekerjaan_mempelai": "Wiraswasta",
                "status_mempelai": "Belum Kawin",
                "dusun_mempelai": "Dusun Sukamaju",
                "nama_ayah_mempelai": "Muhammad Sahid",
                "tempat_tanggal_lahir_ayah_mempelai": "Nganjuk, 31 Desember 1954",
                "agama_ayah_mempelai": "Islam",
                "pekerjaan_ayah_mempelai": "Karyawan Swasta",
                "alamat_ayah_mempelai": "Jl. Niaga Baru no 24",
                "nama_ibu_mempelai": "Sukini",
                "tempat_tanggal_lahir_ibu_mempelai": "Kediri, 05 September 1955",
                "agama_ibu_mempelai": "Islam",
                "pekerjaan_ibu_mempelai": "Ibu Rumah Tangga",
                "alamat_ibu_mempelai": "Jl. Niaga Baru no 24",
                "penanda_tangan_surat": "Mustahiq, S.Adm",
                "nip_penandatangan_surat": "1918718001902981920"
            }
        }
