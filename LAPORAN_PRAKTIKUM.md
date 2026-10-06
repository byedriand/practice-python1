# Laporan Praktikum Python

## 1. Pengantar

Proyek ini merupakan tugas praktik Python yang berisi 6 soal dengan fokus pada penerapan logika dasar, validasi data, perhitungan, dan pengelolaan kondisi program. Program dibuat dalam bentuk menu interaktif agar pengguna dapat memilih soal yang ingin dijalankan secara satu per satu.

## 2. Tujuan

Tujuan utama dari proyek ini adalah:

- Menerapkan logika pemrograman dasar menggunakan Python.
- Memahami konsep perhitungan diskon, validasi data, dan pemetaan status.
- Membuat program interaktif yang mudah digunakan.
- Menyusun hasil praktikum dalam bentuk yang rapi dan siap dikumpulkan.

## 3. Deskripsi Setiap Soal

### Soal 1 - Status Mahasiswa

Pada soal ini, program menerima data mahasiswa berupa NIM, nama, IPK, dan SKS, kemudian menentukan status mahasiswa berdasarkan aturan tertentu. Program menampilkan hasil dalam bentuk tabel laporan.

### Soal 2 - Diskon SPP

Soal ini menghitung besar diskon SPP berdasarkan beberapa faktor, seperti status anak karyawan, IPK, dan status pembayaran. Hasilnya mencakup total diskon, potongan, dan biaya akhir yang harus dibayarkan.

### Soal 3 - Peringatan Stok

Program ini mengevaluasi stok barang menggunakan ambang batas aman, peringatan, rendah, dan habis. Selanjutnya, program menghitung prioritas item dan total nilai inventaris secara otomatis.

### Soal 4 - Menu Interaktif

Soal ini menggabungkan beberapa logika sebelumnya ke dalam menu interaktif. Pengguna dapat memilih submenu untuk mengecek status mahasiswa, menghitung diskon, atau melihat kondisi stok.

### Soal 5 - Validasi Data Mahasiswa

Program ini melakukan validasi terhadap NIM, nama, IPK, SKS, dan semester. Jika ada data yang tidak sesuai, sistem akan menampilkan pesan kesalahan yang jelas.

### Soal 6 - Ringkasan Algoritma

Soal terakhir menyajikan ringkasan data dari tugas sebelumnya, seperti persentase mahasiswa aktif, rata-rata diskon, dan persentase kebutuhan restock.

## 4. Struktur Project

- src/ : berisi script utama dan file soal per tugas
- tests/ : berisi pengecekan dasar program
- README.md : dokumentasi singkat project
- bukti-semua-soal.png : bukti hasil gabungan semua soal

## 5. Hasil Program

Bukti hasil lengkap semua soal dapat dilihat pada gambar berikut:

![Bukti hasil semua soal](bukti-semua-soal.png)

## 6. Soal Teori dan Jawaban

### 1) Perbedaan antara aturan bisnis dan logika teknis

Aturan bisnis adalah ketentuan yang berasal dari kebutuhan organisasi atau operasional, misalnya mahasiswa dinyatakan aktif jika IPK minimal 2.75 dan jumlah SKS sesuai syarat. Logika teknis adalah cara program menerjemahkan aturan tersebut ke dalam kode komputer, misalnya dengan struktur if dan else. Contoh aturan bisnis: diskon SPP diberikan kepada mahasiswa yang memenuhi syarat tertentu. Contoh logika teknis: if ipk >= 3.0 and status == "anak_karyawan": ...

### 2) Mengapa NIM sebaiknya disimpan sebagai string

NIM sering kali memiliki format khusus dan dapat diawali dengan angka nol atau gabungan angka dan huruf, sehingga jika disimpan sebagai integer, format asli dapat berubah dan data menjadi kurang akurat. Contohnya, NIM dengan format 202401001 akan tetap utuh jika disimpan sebagai string, sedangkan jika dipaksa ke integer maka representasi dapat berubah dan proses validasi juga menjadi lebih rumit. Jadi, NIM lebih aman disimpan sebagai string untuk menjaga format data dan memudahkan validasi.

### 3) Perbedaan operator and dan or

Operator and berarti semua kondisi harus bernilai benar agar hasilnya benar, sedangkan or berarti salah satu kondisi saja sudah cukup. Contoh aturan bisnis untuk and: siswa berhak mendapatkan beasiswa jika IPK >= 3.5 dan SKS >= 24. Contoh aturan bisnis untuk or: mahasiswa mendapat diskon jika status anak karyawan atau IPK >= 3.75.

### 4) Mengapa urutan kondisi if, elif, else penting

Urutan kondisi sangat penting karena program akan mengecek kondisi dari atas ke bawah secara berurutan. Jika kondisi yang lebih umum diletakkan di depan kondisi yang lebih spesifik, maka kondisi yang lebih spesifik tidak pernah akan tercapai. Misalnya, jika kondisi if nilai >= 60 ditempatkan sebelum if nilai >= 80, maka semua nilai di atas 80 akan langsung masuk ke kondisi pertama dan kondisi kedua tidak dijalankan.

### 5) Kapan sebaiknya menggunakan for loop dan while loop

for loop digunakan ketika jumlah iterasi sudah diketahui atau data yang diproses bersifat terstruktur seperti daftar mahasiswa atau daftar barang. Contoh bisnis: menghitung data seluruh mahasiswa satu per satu. while loop digunakan ketika kondisi pengulangan tergantung pada kondisi tertentu, seperti terus meminta input sampai data valid. Contoh bisnis: meminta pengguna memasukkan NIM sampai formatnya benar.

### 6) Fungsi else pada for loop dan while loop

Else pada loop digunakan untuk mengeksekusi blok kode ketika perulangan selesai tanpa gangguan break. Pada for loop, else biasanya digunakan untuk menandai bahwa seluruh data berhasil diproses. Pada while loop, else dijalankan jika kondisi loop menjadi false setelah proses pengulangan selesai. Jika loop dihentikan dengan break, maka blok else tidak akan dieksekusi.

### 7) Mengapa validasi input harus dilakukan sebelum mengevaluasi aturan bisnis

Validasi input harus dilakukan agar data yang masuk sesuai dengan aturan sistem dan tidak menyebabkan kesalahan perhitungan. Jika validasi diabaikan, data tidak valid seperti NIM kosong, nama kosong, atau IPK di luar rentang 0.0 sampai 4.0 dapat menghasilkan hasil yang salah bahkan menyebabkan program error. Dengan validasi, data yang masuk lebih akurat dan keputusan bisnis menjadi lebih terpercaya.

### 8) Konsep validasi komposit

Validasi komposit adalah proses pengecekan beberapa syarat secara bersamaan sebelum data diterima. Contohnya, data mahasiswa valid jika NIM berisi karakter yang benar, nama tidak kosong, IPK berada dalam rentang 0.0 sampai 4.0, dan SKS di antara 0 sampai 24. Jika salah satu syarat tidak terpenuhi, sistem akan menolak data dan menampilkan pesan kesalahan. Dengan cara ini, data dapat dipastikan konsisten sebelum masuk ke proses bisnis.

Bukti pengerjaan soal teori ini tercatat dalam laporan ini sebagai bagian dari tugas praktik Python. Dokumentasi ini menunjukkan bahwa teori dasar pemrograman, validasi data, dan logika keputusan sudah dipahami dengan benar.

## 6. Kesimpulan

Proyek ini berhasil dibuat sebagai latihan pemrograman Python yang mencakup berbagai konsep penting, mulai dari input-output dasar, kondisi, perhitungan, validasi, hingga pengelolaan menu interaktif. Program ini juga sudah dibuat dalam bentuk yang rapi untuk kebutuhan dokumentasi dan pengumpulan tugas. Selain itu, soal teori juga telah dikerjakan dan didokumentasikan sebagai bukti pemahaman terhadap konsep dasar sistem informasi dan logika pemrograman.
