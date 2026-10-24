
# Melakukan perulangan dari 1 hingga 100
for angka in range(1, 101):
    # Jika angka dibagi 3 sisanya nol dan angka dibagi 5 sisanya nol
    # angka yang bisa dibagi dengan 3 dan bisa dibagi dengan 5 
    # contoh 15, 30, 45, 60, 75, 90
    # Maka cetak "Dangdut"
    if angka % 3 == 0 and angka % 5 == 0:
        print("Dangdut")
    # Jika kondisi sebelumnya tidak terpenuhi, periksa apakah nomor bisa dibagi 3 tanpa sisa.
    # angka yang bisa dibagi dengan 3 dan tidak bisa dibagi dengan 5
    # contoh 3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99
    # Maka cetak "Dang"
    elif angka % 3 == 0:
        print("Dang")
    # Jika kondisi sebelumnya tidak terpenuhi, periksa apakah nomor bisa dibagi 5 tanpa sisa.
    # angka yang bisa dibagi dengan 5 dan tidak bisa dibagi dengan 3
    # contoh 5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100
    # Maka cetak "Dut"
    elif angka % 5 == 0:
        print("Dut")
    # Jika kondisi sebelumnya tidak terpenuhi, maka cetak angka itu sendiri.
    # contoh 1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46 47, 48 dst
    else:
        print(angka)