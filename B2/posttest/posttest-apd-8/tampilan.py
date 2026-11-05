# tampilan.py - semua output program ditampilkan lewat library prettytable

try:
    from prettytable import PrettyTable
except ImportError:
    print("Library prettytable belum terpasang.")
    print("Jalankan perintah ini di terminal: pip install prettytable")
    raise SystemExit


# ---------- PROSEDUR ----------
def tampilkan_judul(teks):
    print()
    print("=" * 50)
    print(teks.center(50))
    print("=" * 50)


def tampilkan_menu(daftar_menu):
    tabel = PrettyTable()                              # [Lokal] tabel
    tabel.field_names = ["No", "Menu"]
    tabel.align["Menu"] = "l"
    for i in range(len(daftar_menu)):
        tabel.add_row([i + 1, daftar_menu[i]])
    print(tabel)


def tampilkan_anggota(data):
    # Mencetak tabel anggota, tidak mengembalikan nilai
    if len(data) == 0:
        print("Tidak ada data anggota.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama", "Role", "Kapan bisa main"]
        tabel.align["Nama"] = "l"
        tabel.align["Role"] = "l"
        tabel.align["Kapan bisa main"] = "l"
        nomor = 1                                      # [Lokal] nomor
        for nama, info in data.items():
            tabel.add_row([nomor, nama, info["role"], info["jadwal"]])
            nomor += 1
        print(tabel)


def tampilkan_statistik(hasil):
    tabel = PrettyTable()
    tabel.field_names = ["Role", "Jumlah Anggota"]
    tabel.align["Role"] = "l"
    for role, jumlah in hasil.items():
        tabel.add_row([role, jumlah])
    print(tabel)
