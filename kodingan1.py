import csv

file = "package_delivery_data.csv"

kolom = [
    "distance_km", "package_weight_kg", "traffic_level",
    "weather", "vehicle_type", "warehouse_delay_hours",
    "handling_time_hours", "priority", "delivery_time_hours"
]

def baca_data():
    with open(file, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def simpan_data(data):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=kolom)
        writer.writeheader()
        writer.writerows(data)


def tabel(data):
    print("-" * 117)

    print(f"{'No':<3} | {'Jarak':<10} | {'Berat':<10} | {'Traffic':<10} | {'Cuaca':<8} | {'Kendaraan':<10} | {'Delay':<9} | {'Handling':<10} | {'Prioritas':<10} | {'Waktu':<10}")

    print("-" * 117)

    no = 1

    for row in data:
        print(f"{no:<3} | {row['distance_km']:<10} | {row['package_weight_kg']:<10} | {row['traffic_level']:<10} | {row['weather']:<8} | {row['vehicle_type']:<10} | {row['warehouse_delay_hours']:<9} | {row['handling_time_hours']:<10} | {row['priority']:<10} | {row['delivery_time_hours']:<10}")

        no += 1

    print("-" * 117)

def estimasi(data):
    jarak = float(input("Masukkan jarak: "))
    berat = float(input("Masukkan berat: "))
    cuaca = input("Masukkan cuaca (Clear/Rain/Storm): ").title()

    hasil = []

    for row in data:
        if row["weather"] == cuaca and abs(float(row["distance_km"]) - jarak) <= 10:
            hasil.append(row)

    if len(hasil) == 0:
        print("Data dengan jarak dan cuaca yang sesuai tidak ditemukan.")
        return

    total_waktu = 0
    total_berat = 0

    for row in hasil:
        total_waktu += float(row["delivery_time_hours"])
        total_berat += float(row["package_weight_kg"])

    rata_waktu = total_waktu / len(hasil)
    rata_berat = total_berat / len(hasil)

    waktu = rata_waktu + (berat - rata_berat) * 0.03

    print("Jumlah data pembanding:", len(hasil))
    print("Estimasi waktu:", round(waktu, 2), "jam")

def tampilkan(data):
    i = 0

    while i < len(data):
        tabel(data[i:i + 20])
        i += 20
        
        break

def tambah(data):
    baru = {}

    for nama in kolom:
        baru[nama] = input("Masukkan " + nama + ": ")

    data.append(baru)
    simpan_data(data)

    print("Data berhasil ditambahkan.")

def ubah(data):
    no = int(input("Masukkan nomor data: "))

    if no >= 1 and no <= len(data):
        tabel([data[no - 1]])

        print("Kolom yang tersedia:")

        for nama in kolom:
            print(nama)

        nama = input("Kolom yang ingin diubah: ")

        if nama in kolom:
            nilai = input("Masukkan nilai baru: ")

            data[no - 1][nama] = nilai
            simpan_data(data)

            print("Data berhasil diubah.")
            tabel([data[no - 1]])
        else:
            print("Kolom tidak ditemukan.")
    else:
        print("Nomor data tidak ditemukan.")

def hapus(data):
    no = int(input("Masukkan nomor data: "))

    if no >= 1 and no <= len(data):
        tabel([data[no - 1]])

        pilih = input("Yakin hapus data? (y/n): ")

        if pilih == "y":
            data.pop(no - 1)
            simpan_data(data)
            print("Data berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Nomor data tidak ditemukan.")

def cari(data):
    print("1. Berdasarkan jarak")
    print("2. Berdasarkan berat")

    pilih = input("Pilih: ")

    if pilih == "1":
        nama = "distance_km"
    elif pilih == "2":
        nama = "package_weight_kg"
    else:
        print("Pilihan tidak tersedia.")
        return

    minimum = float(input("Nilai minimum: "))
    maksimum = float(input("Nilai maksimum: "))

    hasil = []

    for row in data:
        nilai = float(row[nama])

        if nilai >= minimum and nilai <= maksimum:
            hasil.append(row)

    if len(hasil) > 0:
        tabel(hasil)
        print("Jumlah data:", len(hasil))
    else:
        print("Data tidak ditemukan.")

def statistik(data):
    print("Jumlah data:", len(data))

    if len(data) == 0:
        return

    daftar = ["distance_km", "package_weight_kg",
              "delivery_time_hours"]

    for nama in daftar:
        total = 0
        minimum = float(data[0][nama])
        maksimum = float(data[0][nama])

        for row in data:
            nilai = float(row[nama])

            total += nilai

            if nilai < minimum:
                minimum = nilai

            if nilai > maksimum:
                maksimum = nilai

        print("\n", nama)
        print("Rata-rata:", round(total / len(data), 2))
        print("Minimum:", minimum)
        print("Maksimum:", maksimum)

def filter_cuaca(data):
    cuaca = input("Masukkan cuaca (Clear/Rain/Storm): ").title()

    hasil = []

    for row in data:
        if row["weather"] == cuaca:
            hasil.append(row)

    if len(hasil) > 0:
        tabel(hasil)
        print("Jumlah data:", len(hasil))
    else:
        print("Data tidak ditemukan.")

def urutkan(data):
    print("1. Jarak")
    print("2. Berat")
    print("3. Waktu pengiriman")

    pilih = input("Pilih kolom: ")

    if pilih == "1":
        nama = "distance_km"
    elif pilih == "2":
        nama = "package_weight_kg"
    elif pilih == "3":
        nama = "delivery_time_hours"
    else:
        print("Pilihan tidak tersedia.")
        return

    arah = input("1. Kecil ke besar\n2. Besar ke kecil\nPilih: ")

    if arah != "1" and arah != "2":
        print("Pilihan tidak tersedia.")
        return

    hasil = data.copy()

    for i in range(len(hasil)):
        for j in range(i + 1, len(hasil)):
            angka1 = float(hasil[i][nama])
            angka2 = float(hasil[j][nama])

            if arah == "1" and angka1 > angka2:
                hasil[i], hasil[j] = hasil[j], hasil[i]

            elif arah == "2" and angka1 < angka2:
                hasil[i], hasil[j] = hasil[j], hasil[i]

    tampilkan(hasil)

data = baca_data()

while True:
    print("\n===== MENU PENGIRIMAN =====")
    print("1. Estimasi Waktu Pengiriman")
    print("2. Tampilkan Data Pengiriman")
    print("3. Tambah Data Pengiriman")
    print("4. Ubah Data Pengiriman")
    print("5. Hapus Data Pengiriman")
    print("6. Cari Data Pengiriman")
    print("7. Statistik Pengiriman")
    print("8. Filter Berdasarkan Cuaca")
    print("9. Urutkan Data Pengiriman")
    print("10. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        estimasi(data)
    elif menu == "2":
        tampilkan(data)
    elif menu == "3":
        tambah(data)
    elif menu == "4":
        ubah(data)
    elif menu == "5":
        hapus(data)
    elif menu == "6":
        cari(data)
    elif menu == "7":
        statistik(data)
    elif menu == "8":
        filter_cuaca(data)
    elif menu == "9":
        urutkan(data)
    elif menu == "10":
        print("Terima kasih telah menggunakan program!")
        break
    else:
        print("Menu tidak tersedia.")
