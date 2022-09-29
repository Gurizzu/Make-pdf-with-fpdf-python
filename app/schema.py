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
