Mini Project Pemrograman Komputer : prediksi waktu pengiriman berdasarkan jarak, beban, dan kondisi cuaca menggunakan python.

Disusun oleh kelompok mini project 6A :

Muhamad Ikhsan     (2610932024)

Daffa Alfarizi     (2610933018)

Rila Febri Irianti (2610933022)

Siti Fadilla       (2610933030)

Perkembangan teknologi mendorong proses pengiriman paket untuk dilakukan secara lebih efektif dan terorganisir. Dalam kegiatan pengiriman, terdapat berbagai informasi yang perlu dikelola, seperti jarak pengiriman, berat paket, kondisi cuaca, jenis kendaraan, dan estimasi waktu pengiriman. Pengelolaan data tersebut secara manual dapat menyulitkan proses pencatatan dan pemantauan.
Oleh karena itu, Program python ini dibuat untuk membantu menghitung perkiraan estimasi waktu pengiriman berdasarkan jarak, beban, kondisi cuaca. serta mengelola informasi yang tersedia pada data.

Batasan pada mini project :
1. Data yang digunakan adalah data pengiriman paket pada file
package_delivery_data.csv yang berjumlah 500 data. Namun pada
implementasi kode program di VS Code data yang diolah dibatasi hanya
sebanyak 20 data yang telah diringkas dari 500 data asli tersebut.
2. Estimasi waktu pengiriman dihitung dari tiga masukan, yaitu jarak
pengiriman (km), berat paket (kg), dan kondisi cuaca. Waktu pengiriman
menjadi hasil estimasi dalam satuan jam. Kolom lalu lintas, jenis kendaraan,
waktu tunggu gudang, waktu penanganan, dan prioritas disimpan serta
ditampilkan, tetapi tidak dimasukkan ke dalam rumus estimasi.
3. Rumus estimasi menggunakan koefisien tetap yang tertulis di dalam program,
sehingga program tidak melatih ulang koefisien dari data.
4. Kondisi cuaca dikelompokkan ke dalam tiga kategori, yaitu Clear (cerah),
Rain (hujan), dan Storm (badai).
5. Program dibuat dengan bahasa pemrograman Python, berjalan pada terminal
dengan menu berbasis angka, dan menyimpan perubahan data ke file CSV.
6. Hasil estimasi merupakan perkiraan dan bukan jaminan waktu tiba yang pasti.
7. Program tidak terhubung dengan data cuaca atau sistem pelacakan paket
secara langsung (real-time).

program python ini memiliki beebrapa fitur yang dapat dimanfaatkan oleh pengguna diantaranya :
1. Estimasi Waktu Pengiriman
Menghitung perkiraan waktu pengiriman berdasarkan jarak, berat paket, dan kondisi cuaca.
2. Tampilkan Data Pengiriman
Menampilkan seluruh data pengiriman yang tersimpan dalam file CSV beserta jumlah data valid dan tidak valid.
3. Tambah Data Pengiriman
Menambahkan informasi pengiriman baru ke dalam file CSV.
4. Ubah Data Pengiriman
Memperbarui informasi dari data pengiriman yang sudah tersimpan.
5. Hapus Data Pengiriman
Menghapus data pengiriman berdasarkan nomor data yang dipilih.
6. Statistik Pengiriman
Menampilkan ringkasan statistik, seperti jumlah data, rata-rata, nilai minimum, dan maksimum.
7. Filter Berdasarkan Cuaca
Menampilkan data pengiriman sesuai kondisi cuaca yang dipilih.
8. Urutkan Data Pengiriman
Mengurutkan data berdasarkan jarak, berat paket, atau estimasi waktu pengiriman.
9. Keluar
Mengakhiri program dan kembali ke terminal.

panduan penggunaan :
1. pastikan file program python dan file csv dalam satu folder syang sama
2. jalankan program 
3. Pilih nomor menu sesuai fitur yang ingin digunakan

struktur repository:

kodingan1.py

package_delivery_data.csv

README.md

penggunaan AI :
Penyusunan Program Python juga memanfaatkan bantuan AI guna meminimalisasi kesalahan pada program
