skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000

ongkos_kirim = 12000
total_pengeluaran = skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6 + ongkos_kirim
print(total_pengeluaran)

daftar_skincare = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]
rata_rata = total_pengeluaran / len(daftar_skincare)
print(rata_rata)
nim = 66
print(nim)
bolean = nim < rata_rata
print(bolean)

print("skincare_1        :", skincare_1)
print("skincare_2        :", skincare_2)
print("skincare_3        :", skincare_3)
print("skincare_4        :", skincare_4)
print("skincare_5        :", skincare_5)
print("skincare_6        :", skincare_6)
print("total_pengeluaran :", total_pengeluaran)
print("rata_rata         :", rata_rata)
print("nim               :", nim)
print("bolean            :", bolean)