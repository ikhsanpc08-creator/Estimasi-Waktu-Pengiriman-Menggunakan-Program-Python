import csv

class ProgramPengiriman:

    def __init__(self):
        self.nama_file = "package_delivery_data.csv"

        self.kolom = [
            "distance_km", "package_weight_kg", "traffic_level",
            "weather", "vehicle_type", "warehouse_delay_hours",
            "handling_time_hours", "priority", "delivery_time_hours"
        ]

        self.data = self.baca_data()

    def baca_data(self):
        with open(self.nama_file, "r", newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))

    def validasi_data(self):
        jumlah_valid = 0
        jumlah_tidak_valid = 0

        for row in self.data:
            lengkap = True

            for k in self.kolom:
                if not (row.get(k) or "").strip():
                    lengkap = False

            if lengkap:
                jumlah_valid += 1
            else:
                jumlah_tidak_valid += 1

        print("Jumlah data valid:", jumlah_valid)
        print("Jumlah data tidak valid:", jumlah_tidak_valid)

    def simpan_data(self):
        with open(self.nama_file, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=self.kolom)
            w.writeheader()
            w.writerows(self.data)

    def tabel(self, data):
        print("-" * 95)
        print(f"| {'No':<2} | {'Jarak':<6} | {'Berat':<6} | {'Traffic':<7} | {'Cuaca':<6} | {'Kendaraan':<6} | {'Delay':<6} | {'Handling':<6} | {'Prioritas':<6} | {'Waktu':<5} |")
        print("-" * 95)

        no = 1

        for row in data:
            print(f"| {no:<2} | {row['distance_km']:<6} | {row['package_weight_kg']:<6} | {row['traffic_level']:<7} | {row['weather']:<6} | {row['vehicle_type']:<9} | {row['warehouse_delay_hours']:<6} | {row['handling_time_hours']:<8} | {row['priority']:<9} | {row['delivery_time_hours']:<5} |")
            no += 1

        print("-" * 95)

    def estimasi(self):

        while True:
            distance = float(input("Masukkan jarak pengiriman (km): "))

            if distance > 0:
                break

            print("Jarak harus lebih besar dari 0. Masukkan ulang.")

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

        print("Estimasi waktu:", round(waktu, 2), "jam")

    def tampilkan(self):

        if not self.data:
            print("Data pengiriman kosong.")
        else:
            self.tabel(self.data)

        self.validasi_data()

    def tambah(self):
        baru = {}

        for k in self.kolom:

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

        self.data.append(baru)
        self.simpan_data()

        print("Data berhasil ditambahkan.")

    def ubah(self):
        while True:
            no = int(input("Masukkan nomor data: "))

            if 1 <= no <= len(self.data):
                break

            print("Nomor data tidak ditemukan.")

        self.tabel([self.data[no - 1]])

        print("Kolom yang tersedia:")

        for nama in self.kolom:
            print(nama)

        nama = input("Kolom yang ingin diubah: ").strip()

        if nama in self.kolom:

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

            self.data[no - 1][nama] = str(nilai)
            self.simpan_data()

            print("Data berhasil diubah.")
            self.tabel([self.data[no - 1]])

        else:
            print("Kolom tidak ditemukan.")

    def hapus(self):
        while True:
            no = int(input("Masukkan nomor data: "))

            if 1 <= no <= len(self.data):
                break

            print("Nomor data tidak ditemukan.")

        self.tabel([self.data[no - 1]])

        while True:
            pilih = input("Yakin hapus data? (y/n): ").strip().lower()

            if pilih == "y":
                self.data.pop(no - 1)
                self.simpan_data()
                print("Data berhasil dihapus.")
                break

            elif pilih == "n":
                print("Penghapusan dibatalkan.")
                break

            else:
                print("Pilihan tidak tersedia. Masukkan y atau n.")

    def statistik(self):
        print("Jumlah data:", len(self.data))

        if not self.data:
            return

        for k in ["distance_km", "package_weight_kg", "delivery_time_hours"]:
            nilai = [float(d[k]) for d in self.data]

            print("\n" + k)
            print("Rata-rata:", round(sum(nilai) / len(nilai), 2))
            print("Minimum:", min(nilai))
            print("Maksimum:", max(nilai))

    def filter_cuaca(self):
        while True:
            cuaca = input("Masukkan cuaca (Clear/Rain/Storm): ").strip().lower()

            if cuaca in ["clear", "rain", "storm"]:
                break

            print("Pilihan cuaca tidak tersedia. Masukkan ulang.")

        hasil = [d for d in self.data if d["weather"].lower() == cuaca]

        if hasil:
            self.tabel(hasil)
            print("Jumlah data:", len(hasil))
        else:
            print("Data tidak ditemukan.")

    def urutkan(self):
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

        hasil = self.data.copy()

        for i in range(len(hasil)):
            for j in range(i + 1, len(hasil)):
                angka1 = float(hasil[i][nama])
                angka2 = float(hasil[j][nama])

                if arah == "1" and angka1 > angka2:
                    hasil[i], hasil[j] = hasil[j], hasil[i]

                elif arah == "2" and angka1 < angka2:
                    hasil[i], hasil[j] = hasil[j], hasil[i]

        self.tampilkan_data(hasil)

    def tampilkan_data(self, data):
        self.tabel(data)

    def jalankan(self):
        while True:

            print("\n===== MENU PENGIRIMAN =====")
            print("1. Estimasi Waktu Pengiriman")
            print("2. Tampilkan Data Pengiriman")
            print("3. Tambah Data Pengiriman")
            print("4. Ubah Data Pengiriman")
            print("5. Hapus Data Pengiriman")
            print("6. Statistik Pengiriman")
            print("7. Filter berdasarkan cuaca")
            print("8. Urutkan data pengiriman")
            print("9. Keluar")

            menu = input("Pilih menu: ").strip()

            if menu == "1":
                self.estimasi()

            elif menu == "2":
                self.tampilkan()

            elif menu == "3":
                self.tambah()

            elif menu == "4":
                self.ubah()

            elif menu == "5":
                self.hapus()

            elif menu == "6":
                self.statistik()

            elif menu == "7":
                self.filter_cuaca()

            elif menu == "8":
                self.urutkan()

            elif menu == "9":
                print("Terima kasih telah menggunakan program!")
                break

            else:
                print("Menu tidak tersedia.")

program = ProgramPengiriman()
program.jalankan()
