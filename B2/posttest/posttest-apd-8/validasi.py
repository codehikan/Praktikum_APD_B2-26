from data import ROLE, anggota


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
