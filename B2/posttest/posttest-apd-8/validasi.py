# validasi.py - semua input dari pengguna beserta pengecekannya (error handling)

from data import ROLE, anggota


# ---------- FUNGSI DENGAN PARAMETER ----------
def minta_angka(pesan, batas):
    # Meminta angka 1 sampai batas, diulang sampai input benar
    while True:
        try:
            angka = int(input(pesan))                  # [Lokal] angka
            if angka < 1 or angka > batas:
                raise ValueError
        except ValueError:
            print("Input tidak valid! Masukkan angka 1 sampai", batas)
        else:
            return angka


# ---------- FUNGSI TANPA PARAMETER ----------
def pilih_role():
    # Menampilkan pilihan role (tuple ROLE) lalu mengembalikan role yang dipilih
    print("\nPilihan role:")
    for i in range(len(ROLE)):                         # [Lokal] i
        print(str(i + 1) + ".", ROLE[i])
    nomor = minta_angka("Pilih nomor role: ", len(ROLE))   # [Lokal] nomor
    return ROLE[nomor - 1]


def minta_nama_baru():
    # Meminta nama anggota baru: tidak boleh kosong dan tidak boleh kembar
    while True:
        try:
            nama = input("Nama anggota: ").strip()     # [Lokal] nama
            if nama == "":
                raise ValueError("Nama tidak boleh kosong!")
            if nama in anggota:
                raise ValueError("Nama sudah terdaftar!")
        except ValueError as pesan_error:
            print(pesan_error)
        else:
            return nama
