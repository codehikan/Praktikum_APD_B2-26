import auth
import crud
import statistik
import tampilan
import validasi
from data import MENU_ADMIN, MENU_USER

while True:
    if auth.level_aktif == "":
        tampilan.tampilkan_judul("SISTEM PENGELOLAAN ANGGOTA DAN JADWAL MABAR TIM")
        tampilan.tampilkan_menu(("Login", "Keluar"))
        pilih = validasi.minta_angka("Pilih menu: ", 2)

        if pilih == 1:
            auth.login()
        else:
            print("Terima kasih, sampai jumpa!")
            break

    else:
        if auth.level_aktif == "admin":
            daftar_menu = MENU_ADMIN
        else:
            daftar_menu = MENU_USER

        tampilan.tampilkan_judul("MENU " + auth.level_aktif.upper() + " | Login sebagai: " + auth.pengguna_aktif)
        tampilan.tampilkan_menu(daftar_menu)
        pilih = validasi.minta_angka("Pilih menu: ", len(daftar_menu))
        aksi = daftar_menu[pilih - 1]

        if aksi == "Tambah anggota":
            crud.tambah_anggota()
        elif aksi == "Lihat semua anggota":
            crud.lihat_anggota()
        elif aksi == "Cari anggota berdasarkan role":
            crud.cari_anggota()
        elif aksi == "Ubah data anggota":
            crud.ubah_anggota()
        elif aksi == "Hapus anggota":
            crud.hapus_anggota()
        elif aksi == "Jumlah anggota per role":
            statistik.lihat_statistik()
        else:
            auth.logout()
