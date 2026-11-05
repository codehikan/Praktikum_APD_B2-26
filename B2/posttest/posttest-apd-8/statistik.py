from data import ROLE, anggota
import tampilan



def hitung_role(daftar, role_dicari):
    if len(daftar) == 0:                               
        return 0
    if daftar[0]["role"] == role_dicari:
        return 1 + hitung_role(daftar[1:], role_dicari)
    return hitung_role(daftar[1:], role_dicari)


def lihat_statistik():
    print("\n--- JUMLAH ANGGOTA PER ROLE ---")
    daftar_data = list(anggota.values())              
    hasil = {}                                         
    for role in ROLE:
        hasil[role] = hitung_role(daftar_data, role)
    tampilan.tampilkan_statistik(hasil)
