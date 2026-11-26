import csv

nama_file = "package_delivery_data.csv"

kolom = [
    "distance_km", "package_weight_kg", "traffic_level",
    "weather", "vehicle_type", "warehouse_delay_hours",
    "handling_time_hours", "priority", "delivery_time_hours"
]

def baca_data():
    with open(nama_file, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def validasi_data(data):
    for no, row in enumerate(data, start=1):
        for k in kolom:
            if not row[k].strip():
                print("Baris", no, "kolom", k, "kosong.")
                return False

    print("Data Valid.")
    return True

def simpan_data(data):
    with open(nama_file, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=kolom)
        w.writeheader()
        w.writerows(data)

def tabel(data):
    print("-" * 117)
    print(f"| {'No':<2} | {'Jarak':<6} | {'Berat':<6} | {'Traffic':<7} | {'Cuaca':<6} | {'Kendaraan':<6} | {'Delay':<6} | {'Handling':<6} | {'Prioritas':<6} | {'Waktu':<5} |" )
    print("-" * 117)

    no = 1
    for row in data:
        print(f"| {no:<2} | {row['distance_km']:<6} | {row['package_weight_kg']:<6} | {row['traffic_level']:<7} | {row['weather']:<6} | {row['vehicle_type']:<9} | {row['warehouse_delay_hours']:<6} | {row['handling_time_hours']:<8} | {row['priority']:<8} | {row['delivery_time_hours']:<5} |")
        no += 1
    print("-" * 121)

def estimasi():
    while True:
        distance = float(input("Masukkan jarak pengiriman (km): "))
        if distance > 0:
            break
        print("Jarak harus lebih besar dari 0 ")
        print("harap input kembali")


    while True:
        weight = float(input("Masukkan berat paket (kg): "))
        if weight > 0:
            break
        print("Berat harus lebih besar dari 0. Masukkan ulang.")

    while True:
        weather = input("Masukkan cuaca (Clear/Storm/Rain): ").strip().lower()
        if weather in ["clear", "storm", "rain"]:
            break
        print("Pilihan cuaca tidak tersedia. Masukkan ulang.")

    waktu = 8.126 + (0.111 * distance) + (0.069 * weight)

    if weather == "rain":
        waktu += 3.972
    elif weather == "storm":
        waktu += 5.693

    print("Estimasi waktu :", round(waktu, 2), "jam")

def tampilkan(data):
    i = 0

    while i < len(data):
        tabel(data[i:i + 20])
        i += 20

def tambah(data):
    baru = {}

    for k in kolom:

        if k in ["distance_km", "package_weight_kg",
                 "warehouse_delay_hours", "handling_time_hours",
                 "delivery_time_hours"]:

            while True:
                nilai = float(input("Masukkan " + k + " : "))
                if nilai > 0:
                    baru[k] = str(nilai)
                    break
                print("Angka harus lebih besar dari 0. Masukkan ulang.")

        elif k == "traffic_level":
            while True:
                nilai = input("Masukkan traffic level (low/medium/high): ").strip().lower()
                if nilai in ["low", "medium", "high"]:
                    baru[k] = nilai
                    break
                print("Traffic level tidak tersedia. Masukkan ulang.")

        elif k == "weather":
            while True:
                nilai = input("Masukkan weather (clear/storm/rain): ").strip().lower()
                if nilai in ["clear", "storm", "rain"]:
                    baru[k] = nilai
                    break
                print("Weather tidak tersedia. Masukkan ulang.")

        elif k == "vehicle_type":
            while True:
                nilai = input("Masukkan vehicle type (bike/van/truck): ").strip().lower()
                if nilai in ["bike", "van", "truck"]:
                    baru[k] = nilai
                    break
                print("Vehicle type tidak tersedia. Masukkan ulang.")

        elif k == "priority":
            while True:
                nilai = input("Masukkan priority (express/standard): ").strip().lower()
                if nilai in ["express", "standard"]:
                    baru[k] = nilai
                    break
                print("Priority tidak tersedia. Masukkan ulang.")

    data.append(baru)
    simpan_data(data)
    print("Data berhasil ditambahkan.")

def ubah(data):
    while True:
        no = int(input("Masukkan nomor data: "))
        if 1 <= no <= len(data):
            break
        print("Nomor data tidak ditemukan.")

    tabel([data[no - 1]])

    print("Kolom yang tersedia:")

    for nama in kolom:
        print(nama)

    nama = input("Kolom yang ingin diubah: ").strip()

    if nama in kolom:

        if nama in ["distance_km", "package_weight_kg",
                    "warehouse_delay_hours", "handling_time_hours",
                    "delivery_time_hours"]:

            while True:
                nilai = float(input("Masukkan nilai baru: "))
                if nilai > 0:
                    break
                print("Angka harus lebih besar dari 0. Masukkan ulang.")

        elif nama == "traffic_level":
            while True:
                nilai = input("Masukkan traffic level: ").strip().lower()
                if nilai in ["low", "medium", "high"]:
                    break
                print("Pilihan tidak tersedia. Masukkan ulang.")

        elif nama == "weather":
            while True:
                nilai = input("Masukkan weather: ").strip().lower()
                if nilai in ["clear", "storm", "rain"]:
                    break
                print("Pilihan tidak tersedia. Masukkan ulang.")

        elif nama == "vehicle_type":
            while True:
                nilai = input("Masukkan vehicle type: ").strip().lower()
                if nilai in ["bike", "van", "truck"]:
                    break
                print("Pilihan tidak tersedia. Masukkan ulang.")

        elif nama == "priority":
            while True:
                nilai = input("Masukkan priority: ").strip().lower()
                if nilai in ["express", "standard"]:
                    break
                print("Pilihan tidak tersedia. Masukkan ulang.")

        data[no - 1][nama] = str(nilai)
        simpan_data(data)

        print("Data berhasil diubah.")
        tabel([data[no - 1]])

    else:
        print("Kolom tidak ditemukan.")

def hapus(data):
    while True:
        no = int(input("Masukkan nomor data: "))
        if 1 <= no <= len(data):
            break
        print("Nomor data tidak ditemukan.")

    tabel([data[no - 1]])

    pilih = input("Yakin hapus data? (y/n): ").strip().lower()

    if pilih == "y":
        data.pop(no - 1)
        simpan_data(data)
        print("Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def cari(data):
    print("1. Berdasarkan jarak")
    print("2. Berdasarkan berat")

    pilih = input("Pilih 1/2: ").strip()

    if pilih == "1":
        k = "distance_km"
    elif pilih == "2":
        k = "package_weight_kg"
    else:
        print("Pilihan tidak tersedia.")
        return

    while True:
        batas_min = float(input("Nilai minimum: "))
        if batas_min > 0:
            break
        print("Angka harus lebih besar dari 0. Masukkan ulang.")

    while True:
        batas_max = float(input("Nilai maksimum: "))
        if batas_max >= batas_min:
            break
        print("Nilai maksimum tidak boleh lebih kecil dari minimum.")

    hasil = [d for d in data if batas_min <= float(d[k]) <= batas_max]

    if hasil:
        tabel(hasil)
        print("Jumlah data:", len(hasil))
    else:
        print("Data tidak ditemukan.")

def statistik(data):
    print("Jumlah data:", len(data))

    if not data:
        return

    for k in ["distance_km", "package_weight_kg", "delivery_time_hours"]:
        nilai = [float(d[k]) for d in data]

        print("\n" + k)
        print("Rata-rata:", round(sum(nilai) / len(nilai), 2))
        print("Minimum:", min(nilai))
        print("Maksimum:", max(nilai))

def filter_cuaca(data):
    while True:
        cuaca = input("Masukkan cuaca (Clear/Rain/Storm): ").strip().lower()

        if cuaca in ["clear", "rain", "storm"]:
            break
        print("Pilihan cuaca tidak tersedia. Masukkan ulang.")

    hasil = [d for d in data if d["weather"].lower() == cuaca]

    if hasil:
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
validasi_data(data)
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

    menu = input("Pilih menu: ").strip()

    if menu == "1":
        estimasi()
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
