


ROLE = ("Tank", "Fighter", "Assassin", "Mage", "Marksman", "Support")


anggota = {
    "Cortez/kris": {"role": "Assassin", "jadwal": "Kapan aja"},
    "BiburNextDoor": {"role": "Marksman", "jadwal": "Free kalau ga malam"},
    "Ghozali": {"role": "Fighter", "jadwal": "Sabtu, Minggu"},
}

while True:
    print()
    print("=" * 50)
    print("SISTEM PENGELOLAAN ANGGOTA DAN JADWAL MABAR TIM")
    print("=" * 50)
    print("1. Tambah anggota")
    print("2. Lihat anggota")
    print("3. Ubah anggota")
    print("4. Hapus anggota")
    print("5. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        
        print("\n--- TAMBAH ANGGOTA ---")
        nama_baru = input("Nama anggota: ").strip()

        if nama_baru == "":
            print("Nama tidak boleh kosong, data tidak disimpan.")
        elif nama_baru in anggota:
            print("Nama sudah terdaftar, data tidak disimpan.")
        else:
            print("Pilihan role:")
            for i in range(len(ROLE)):
                print(str(i + 1) + ".", ROLE[i])
            no_role = input("Pilih nomor role: ")
            jadwal_baru = input("Kapan bisa main? (contoh: Senin): ")

            if no_role.isdigit() and 1 <= int(no_role) <= len(ROLE):
                anggota[nama_baru] = {
                    "role": ROLE[int(no_role) - 1],
                    "jadwal": jadwal_baru
                }
                print("Anggota berhasil ditambahkan!")
            else:
                print("Nomor role tidak valid, data tidak disimpan.")

    elif pilih == "2":
       
        print("\n--- DAFTAR ANGGOTA ---")
        if len(anggota) == 0:
            print("Belum ada anggota.")
        else:
            print("No".ljust(4) + "Nama".ljust(14) + "Role".ljust(12) + "Kapan bisa main")
            nomor = 1
            for nama, data in anggota.items():
                print(str(nomor).ljust(4) + nama.ljust(14) + data["role"].ljust(12) + data["jadwal"])
                nomor += 1

    elif pilih == "3":
        
        print("\n--- UBAH ANGGOTA ---")
        if len(anggota) == 0:
            print("Belum ada anggota.")
        else:
            for nama, data in anggota.items():
                print("-", nama, "|", data["role"], "|", data["jadwal"])
            nama = input("Ketik nama anggota yang diubah: ").strip()

            if nama in anggota:
                print("Kosongkan (Enter) jika tidak ingin mengubah bagian itu.")
                nama_baru = input("Nama baru: ").strip()
                print("Pilihan role:")
                for j in range(len(ROLE)):
                    print(str(j + 1) + ".", ROLE[j])
                no_role = input("Nomor role baru: ")
                jadwal_baru = input("Jadwal baru: ")

                if no_role.isdigit() and 1 <= int(no_role) <= len(ROLE):
                    anggota[nama]["role"] = ROLE[int(no_role) - 1]
                if jadwal_baru != "":
                    anggota[nama]["jadwal"] = jadwal_baru
                if nama_baru != "" and nama_baru != nama:
                    if nama_baru in anggota:
                        print("Nama baru sudah dipakai, nama tidak diubah.")
                    else:
                        anggota[nama_baru] = anggota.pop(nama)
                print("Data anggota berhasil diubah!")
            else:
                print("Anggota tidak ditemukan.")

    elif pilih == "4":
        print("\n--- HAPUS ANGGOTA ---")
        if len(anggota) == 0:
            print("Belum ada anggota.")
        else:
            for nama, data in anggota.items():
                print("-", nama, "|", data["role"], "|", data["jadwal"])
            nama = input("Ketik nama anggota yang dihapus: ").strip()

            if nama in anggota:
                anggota.pop(nama)
                print("Anggota", nama, "berhasil dihapus.")
            else:
                print("Anggota tidak ditemukan.")

    elif pilih == "5":
        print("Terima kasih, sampai jumpa!")
        break

    else:
        print("Pilihan menu tidak valid!")