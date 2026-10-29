ROLE = ("Tank", "Fighter", "Assassin", "Mage", "Marksman", "Support")                
MENU_ADMIN = ("Tambah anggota", "Lihat semua anggota", "Ubah data anggota",
              "Hapus anggota", "Jumlah anggota per role", "Logout")                    
MENU_USER = ("Lihat semua anggota", "Cari anggota berdasarkan role",
             "Jumlah anggota per role", "Logout")                                      


anggota = {                                                                            
    "Cortez/kris": {"role": "Assassin", "jadwal": "Kapan aja"},
    "BiburNextDoor": {"role": "Marksman", "jadwal": "Free kalau ga malam"},
    "Ghozali": {"role": "Fighter", "jadwal": "Sabtu, Minggu"},
}


akun = {                                                                              
    "admin": {"password": "admin123", "level": "admin"},
    "user": {"password": "user123", "level": "user"},
}

pengguna_aktif = ""    
level_aktif = ""       



def minta_angka(pesan, batas):
    while True:
        try:
            angka = int(input(pesan))                  
            if angka < 1 or angka > batas:
                raise ValueError
        except ValueError:
            print("Input tidak valid! Masukkan angka 1 sampai", batas)
        else:
            return angka


def hitung_role(daftar, role_dicari):
    if len(daftar) == 0:                               
        return 0
    if daftar[0]["role"] == role_dicari:
        return 1 + hitung_role(daftar[1:], role_dicari)
    return hitung_role(daftar[1:], role_dicari)


def pilih_role():
    print("\nPilihan role:")
    for i in range(len(ROLE)):                         
        print(str(i + 1) + ".", ROLE[i])
    nomor = minta_angka("Pilih nomor role: ", len(ROLE))  
    return ROLE[nomor - 1]


def minta_nama_baru():
    while True:
        try:
            nama = input("Nama anggota: ").strip()     
            if nama == "":
                raise ValueError("Nama tidak boleh kosong!")
            if nama in anggota:
                raise ValueError("Nama sudah terdaftar!")
        except ValueError as pesan_error:
            print(pesan_error)
        else:
            return nama

def tampilkan_anggota(data):
    if len(data) == 0:
        print("Tidak ada data anggota.")
    else:
        nomor = 1                                      
        print("-" * 50)
        print("No".ljust(4) + "Nama".ljust(14) + "Role".ljust(12) + "Kapan bisa main")
        print("-" * 50)
        for nama, info in data.items():
            print(str(nomor).ljust(4) + nama.ljust(14) + info["role"].ljust(12) + info["jadwal"])
            nomor += 1
        print("-" * 50)


def login():
    global pengguna_aktif, level_aktif
    percobaan = 0                                     
    while percobaan < 3:
        username = input("Username: ").strip()        
        password = input("Password: ").strip()         
        try:
            if akun[username]["password"] != password:   
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

while True:
    if level_aktif == "":
       
        print()
        print("=" * 50)
        print("SISTEM PENGELOLAAN ANGGOTA DAN JADWAL MABAR TIM")
        print("=" * 50)
        print("1. Login")
        print("2. Keluar")
        pilih = minta_angka("Pilih menu: ", 2)

        if pilih == 1:
            login()
        else:
            print("Terima kasih, sampai jumpa!")
            break

    else:
        
        if level_aktif == "admin":
            daftar_menu = MENU_ADMIN
        else:
            daftar_menu = MENU_USER

        print()
        print("=" * 50)
        print("MENU", level_aktif.upper(), "| Login sebagai:", pengguna_aktif)
        print("=" * 50)
        for i in range(len(daftar_menu)):
            print(str(i + 1) + ".", daftar_menu[i])
        pilih = minta_angka("Pilih menu: ", len(daftar_menu))
        aksi = daftar_menu[pilih - 1]

        if aksi == "Tambah anggota":
            print("\n--- TAMBAH ANGGOTA ---")
            nama_baru = minta_nama_baru()
            role_baru = pilih_role()
            try:
                jadwal_baru = input("Kapan bisa main? (contoh: Senin): ").strip()
                if jadwal_baru == "":
                    raise ValueError("Jadwal tidak boleh kosong!")
            except ValueError as pesan_error:
                print(pesan_error, "Data tidak disimpan.")
            else:
                anggota[nama_baru] = {"role": role_baru, "jadwal": jadwal_baru}
                print("Anggota berhasil ditambahkan!")

        elif aksi == "Lihat semua anggota":
            print("\n--- DAFTAR SEMUA ANGGOTA ---")
            tampilkan_anggota(anggota)

        elif aksi == "Cari anggota berdasarkan role":
            print("\n--- CARI ANGGOTA BERDASARKAN ROLE ---")
            role_dicari = pilih_role()
            hasil = {}
            for nama, info in anggota.items():
                if info["role"] == role_dicari:
                    hasil[nama] = info
            print("\nAnggota dengan role", role_dicari + ":")
            tampilkan_anggota(hasil)

        elif aksi == "Ubah data anggota":
            print("\n--- UBAH DATA ANGGOTA ---")
            try:
                if len(anggota) == 0:
                    raise ValueError("Belum ada anggota.")
                tampilkan_anggota(anggota)
                nama = input("Ketik nama anggota yang diubah: ").strip()
                data = anggota[nama]                  
            except ValueError as pesan_error:
                print(pesan_error)
            except KeyError:
                print("Anggota tidak ditemukan.")
            else:
                print("Kosongkan (Enter) jika tidak ingin mengubah bagian itu.")
                nama_baru = input("Nama baru: ").strip()
                ubah_role = input("Ubah role? (y/t): ").strip().lower()
                if ubah_role == "y":
                    data["role"] = pilih_role()
                jadwal_baru = input("Jadwal baru: ").strip()

                if jadwal_baru != "":
                    data["jadwal"] = jadwal_baru
                if nama_baru != "" and nama_baru != nama:
                    if nama_baru in anggota:
                        print("Nama baru sudah dipakai, nama tidak diubah.")
                    else:
                        anggota[nama_baru] = anggota.pop(nama)
                print("Data anggota berhasil diubah!")
            finally:
                print("-" * 50)

        elif aksi == "Hapus anggota":
            print("\n--- HAPUS ANGGOTA ---")
            try:
                if len(anggota) == 0:
                    raise ValueError("Belum ada anggota.")
                tampilkan_anggota(anggota)
                nama = input("Ketik nama anggota yang dihapus: ").strip()
                anggota.pop(nama)                      
            except ValueError as pesan_error:
                print(pesan_error)
            except KeyError:
                print("Anggota tidak ditemukan.")
            else:
                print("Anggota", nama, "berhasil dihapus.")
            finally:
                print("-" * 50)

        elif aksi == "Jumlah anggota per role":
            print("\n--- JUMLAH ANGGOTA PER ROLE ---")
            daftar_data = list(anggota.values())
            for role in ROLE:
                print(role.ljust(12) + ":", hitung_role(daftar_data, role))

        else:
            pengguna_aktif = ""
            level_aktif = ""
            print("Anda telah logout.")