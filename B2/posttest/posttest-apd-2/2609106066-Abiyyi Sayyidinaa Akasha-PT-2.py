skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000

ongkos_kirim = 12000
total_pengeluaran = skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6 + ongkos_kirim


daftar_skincare = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]
rata_rata = total_pengeluaran / len(daftar_skincare)

nim = 66

bolean = nim < rata_rata
print(skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6)
print(total_pengeluaran)
print(rata_rata)
print(nim)
print(bolean)