nama_benar = "abi"
nim_benar = "066"

garis_tebal = "𓂃" * 50
garis_tipis = "⌁" * 50

print(garis_tebal)
print("            LOS POLLOS HERMANOS")
print("      Program Makanan Bergizi Gratis")
print("            Kota Albuquerque")
print(garis_tebal)
print("Silakan login dulu untuk melanjutkan")
print(garis_tipis)


percobaan = 0
batas_login = 3
sukses_login = False

while percobaan < batas_login:
    print(f"Kesempatan login ke-{percobaan + 1} dari {batas_login}")

    input_nama = input("Username : ").strip().lower()
    input_nim = input("Password : ").strip()
    percobaan += 1

    if input_nama == "" or input_nim == "":
        print("Username dan password wajib diisi")
    else:
        nama_cocok = input_nama == nama_benar
        nim_cocok = input_nim == nim_benar

        if nama_cocok and nim_cocok:
            sukses_login = True
            print("Login berhasil, selamat datang", nama_benar.upper())
            break
        elif not nama_cocok and nim_cocok:
            print("Login gagal, username salah")
        elif nama_cocok and not nim_cocok:
            print("Login gagal, password salah")
        else:
            print("Login gagal, username dan password salah")

    if percobaan < batas_login:
        print(f"Kesempatan tersisa: {batas_login - percobaan}")

if not sukses_login:
    print(garis_tebal)
    print("Gagal login 3 kali, akses ditolak")
    print(garis_tebal)
else:
    menu_aktif = True

    while menu_aktif:
        
        print(garis_tebal)
        print("Menu Distribusi Paket")
        print(garis_tebal)
        print("1. Paket Reguler   (1 porsi)")
        print("2. Paket Anak      (1 porsi)")
        print("3. Paket Keluarga  (4 porsi)")
        print("4. Keluar")
        print(garis_tipis)

        input_valid = False
        while not input_valid:
            pilihan = input("Pilih opsi (1-4): ").strip()
            if pilihan in ("1", "2", "3", "4"):
                input_valid = True
            else:
                print("Opsi tidak valid")

        pilihan = int(pilihan)

        if pilihan == 4:
            print(garis_tebal)
            print("Terima kasih sudah berbagi")
            print("Program distribusi paket selesai")
            print(garis_tebal)
            menu_aktif = False
            continue

        if pilihan == 1:
            jenis_paket = "Paket Reguler"
            porsi_per_paket = 1
        elif pilihan == 2:
            jenis_paket = "Paket Anak"
            porsi_per_paket = 1
        else:
            jenis_paket = "Paket Keluarga"
            porsi_per_paket = 4

        jumlah_valid = False
        while not jumlah_valid:
            input_jumlah = input(f"Jumlah {jenis_paket} yang dibagikan: ").strip()
            if input_jumlah == "":
                print("Jumlah paket tidak boleh kosong")
            elif not input_jumlah.isdigit():
                print("Jumlah paket harus berupa angka")
            elif int(input_jumlah) <= 0:
                print("Jumlah paket harus lebih dari 0")
            else:
                jumlah_valid = True

        jumlah_paket = int(input_jumlah)

        
        total_porsi = 0
        for i in range(jumlah_paket):
            total_porsi += porsi_per_paket

        penerima_manfaat = total_porsi

        if total_porsi >= 20:
            bonus = "5 paket buah"
        elif total_porsi >= 10:
            bonus = "3 botol susu"
        elif total_porsi >= 5:
            bonus = "1 paket vitamin"
        else:
            bonus = "Tidak ada bonus"

        print(garis_tebal)
        print("          Rekap Distribusi Paket")
        print(garis_tebal)
        print(f"Jenis paket        : {jenis_paket}")
        print(f"Jumlah paket       : {jumlah_paket}")
        print(f"Total porsi        : {total_porsi} porsi")
        print(f"Penerima manfaat   : {penerima_manfaat} orang")
        print(f"Bonus              : {bonus}")
        print(garis_tipis)
        print("Makanan dibagikan secara gratis untuk masyarakat")
        print(garis_tebal)
