from data import anggota
import tampilan
import validasi



def tambah_anggota():
    print("\n--- TAMBAH ANGGOTA ---")
    nama_baru = validasi.minta_nama_baru()
    role_baru = validasi.pilih_role()
    try:
        jadwal_baru = input("Kapan bisa main? (contoh: Senin): ").strip()
        if jadwal_baru == "":
            raise ValueError("Jadwal tidak boleh kosong!")
    except ValueError as pesan_error:
        print(pesan_error, "Data tidak disimpan.")
    else:
        anggota[nama_baru] = {"role": role_baru, "jadwal": jadwal_baru}
        print("Anggota berhasil ditambahkan!")


# ---------- READ ----------
def lihat_anggota():
    print("\n--- DAFTAR SEMUA ANGGOTA ---")
    tampilan.tampilkan_anggota(anggota)


def cari_anggota():
    print("\n--- CARI ANGGOTA BERDASARKAN ROLE ---")
    role_dicari = validasi.pilih_role()
    hasil = {}
    for nama, info in anggota.items():
        if info["role"] == role_dicari:
            hasil[nama] = info
    print("\nAnggota dengan role", role_dicari + ":")
    tampilan.tampilkan_anggota(hasil)


# ---------- UPDATE ----------
def ubah_anggota():
    print("\n--- UBAH DATA ANGGOTA ---")
    try:
        if len(anggota) == 0:
            raise ValueError("Belum ada anggota.")
        tampilan.tampilkan_anggota(anggota)
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
            data["role"] = validasi.pilih_role()
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


# ---------- DELETE ----------
def hapus_anggota():
    print("\n--- HAPUS ANGGOTA ---")
    try:
        if len(anggota) == 0:
            raise ValueError("Belum ada anggota.")
        tampilan.tampilkan_anggota(anggota)
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
