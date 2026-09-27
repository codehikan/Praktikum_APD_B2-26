nama = "Abi"
nim = "66"

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == nama and password == nim:
    print("Login berhasil")
    total_point = int(input("Masukkan total point: "))

    if total_point < 0:
        print("Error: total_point tidak boleh kurang dari 0")
    else:
        if total_point < 100:
            rank = "Rookie"
            needed = 100 - total_point
        elif total_point < 300:
            rank = "Warrior"
            needed = 300 - total_point
        elif total_point < 1000:
            rank = "Master"
            needed = 1000 - total_point
        elif total_point < 5000:
            rank = "Grand Master"
            needed = 5000 - total_point
        else:
            rank = "Legend"

        print("Username:", username)
        print("Rank saat ini:", rank)
        if rank == "Legend":
            print("Selamat! Kamu telah mencapai rank tertinggi!")
        else:
            print("Point yang dibutuhkan untuk naik rank:", needed)
else:
    print("Login gagal. Username atau password salah.")
