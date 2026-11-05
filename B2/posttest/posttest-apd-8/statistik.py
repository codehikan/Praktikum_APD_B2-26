# statistik.py - perhitungan jumlah anggota per role (memakai fungsi rekursif)

from data import ROLE, anggota
import tampilan


# ---------- FUNGSI REKURSIF DENGAN PARAMETER ----------
def hitung_role(daftar, role_dicari):
    # Menghitung jumlah anggota dengan role tertentu
    if len(daftar) == 0:                               # basis rekursi
        return 0
    if daftar[0]["role"] == role_dicari:
        return 1 + hitung_role(daftar[1:], role_dicari)
    return hitung_role(daftar[1:], role_dicari)


# ---------- PROSEDUR ----------
def lihat_statistik():
    print("\n--- JUMLAH ANGGOTA PER ROLE ---")
    daftar_data = list(anggota.values())               # [Lokal] daftar_data
    hasil = {}                                         # [Lokal] hasil
    for role in ROLE:
        hasil[role] = hitung_role(daftar_data, role)
    tampilan.tampilkan_statistik(hasil)
