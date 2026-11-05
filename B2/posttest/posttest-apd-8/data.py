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
