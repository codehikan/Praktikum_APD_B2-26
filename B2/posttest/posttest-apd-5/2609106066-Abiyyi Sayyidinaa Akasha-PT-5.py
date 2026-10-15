ROLE = ("Tank", "Fighter", "Assassin", "Mage", "Marksman", "Support")


nama = ["Nando", "Habibur", "Abbie"]
role = ["Assassin", "Tank", "Marksman"]
jadwal = ["Senin", "Rabu", "Jumat"]

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
        nama_baru = input("Nama anggota: ")
        print("Pilihan role:")
        for i in range(len(ROLE)):
            print(str(i + 1) + ".", ROLE[i])
        no_role = input("Pilih nomor role: ")
        jadwal_baru = input("Kapan bisa main? (contoh: Senin : ")

        if no_role.isdigit() and 1 <= int(no_role) <= len(ROLE):
            nama.append(nama_baru)
            role.append(ROLE[int(no_role) - 1])
            jadwal.append(jadwal_baru)
            print("Anggota berhasil ditambahkan!")
        else:
            print("Nomor role tidak valid, data tidak disimpan.")

    elif pilih == "2":
        print("\n--- DAFTAR ANGGOTA ---")
        if len(nama) == 0:
            print("Belum ada anggota.")
        else:
            print("No".ljust(4) + "Nama".ljust(14) + "Role".ljust(12) + "Kapan bisa main")
            for i in range(len(nama)):
                print(str(i + 1).ljust(4) + nama[i].ljust(14) + role[i].ljust(12) + jadwal[i])

    elif pilih == "3":
        print("\n--- UBAH ANGGOTA ---")
        if len(nama) == 0:
            print("Belum ada anggota.")
        else:
            for i in range(len(nama)):
                print(str(i + 1) + ".", nama[i], "|", role[i], "|", jadwal[i])
            no = input("Pilih nomor anggota yang diubah: ")

            if no.isdigit() and 1 <= int(no) <= len(nama):
                i = int(no) - 1
                print("Kosongkan (Enter) jika tidak ingin mengubah bagian itu.")
                nama_baru = input("Nama baru: ")
                print("Pilihan role:")
                for j in range(len(ROLE)):
                    print(str(j + 1) + ".", ROLE[j])
                no_role = input("Nomor role baru: ")
                jadwal_baru = input("Jadwal baru: ")

                if nama_baru != "":
                    nama[i] = nama_baru
                if no_role.isdigit() and 1 <= int(no_role) <= len(ROLE):
                    role[i] = ROLE[int(no_role) - 1]
                if jadwal_baru != "":
                    jadwal[i] = jadwal_baru
                print("Data anggota berhasil diubah!")
            else:
                print("Nomor anggota tidak valid.")

    elif pilih == "4":
        print("\n--- HAPUS ANGGOTA ---")
        if len(nama) == 0:
            print("Belum ada anggota.")
        else:
            for i in range(len(nama)):
                print(str(i + 1) + ".", nama[i], "|", role[i], "|", jadwal[i])
            no = input("Pilih nomor anggota yang dihapus: ")

            if no.isdigit() and 1 <= int(no) <= len(nama):
                i = int(no) - 1
                print("Anggota", nama[i], "berhasil dihapus.")
                nama.pop(i)
                role.pop(i)
                jadwal.pop(i)
            else:
                print("Nomor anggota tidak valid.")

    elif pilih == "5":
        print("Terima kasih, sampai jumpa!")
        break

    else:
        print("Pilihan menu tidak valid!")