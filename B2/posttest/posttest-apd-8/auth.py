# auth.py - login, logout, dan status pengguna yang sedang aktif (multiuser)

from data import akun

pengguna_aktif = ""    # [Global 6] username yang sedang login ("" = belum login)
level_aktif = ""       # [Global 7] level yang sedang login ("" = belum login)


# ---------- PROSEDUR ----------
def login():
    # Memproses login dan mengubah variabel global
    global pengguna_aktif, level_aktif
    percobaan = 0                                      # [Lokal] percobaan
    while percobaan < 3:
        username = input("Username: ").strip()         # [Lokal] username
        password = input("Password: ").strip()         # [Lokal] password
        try:
            if akun[username]["password"] != password:   # KeyError jika username tidak ada
                raise ValueError
        except (KeyError, ValueError):
            percobaan += 1
            print("Username atau password salah!")
        else:
            pengguna_aktif = username
            level_aktif = akun[username]["level"]
            print("Login berhasil!")
            return
    print("Login gagal 3 kali. Kembali ke menu awal.")


def logout():
    global pengguna_aktif, level_aktif
    pengguna_aktif = ""
    level_aktif = ""
    print("Anda telah logout.")
