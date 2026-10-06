# Tugas 1

Nama : Adrian Ronald Daga
Npm : 20241320011
Prodi : Sistem Informasi

## Project Overview

Proyek ini merupakan tugas praktikum Python yang berisi 6 soal latihan dengan fokus pada logika pemrograman, validasi data, perhitungan, serta pembuatan program interaktif. Program dibuat dalam bentuk menu utama agar pengguna dapat memilih soal yang ingin dijalankan secara satu per satu.

## Ringkasan Soal

1. Soal 1 - Status Mahasiswa  
   Menentukan status mahasiswa berdasarkan IPK dan SKS.

2. Soal 2 - Diskon SPP  
   Menghitung diskon SPP berdasarkan anak karyawan, IPK, dan status pembayaran.

3. Soal 3 - Peringatan Stok  
   Menilai kondisi stok barang dan menghitung prioritas serta nilai inventaris.

4. Soal 4 - Menu Interaktif  
   Menggabungkan beberapa fungsi dalam menu pilihan yang dapat dipilih pengguna.

5. Soal 5 - Validasi Data Mahasiswa  
   Melakukan pengecekan terhadap NIM, nama, IPK, SKS, dan semester.

6. Soal 6 - Ringkasan Algoritma  
   Menyajikan ringkasan data hasil dari soal sebelumnya dalam bentuk statistik.

## Soal Teori dan Jawaban

1. Aturan bisnis adalah ketentuan yang dibuat oleh organisasi, sedangkan logika teknis adalah cara program menerjemahkan aturan tersebut ke dalam kode. Contoh aturan bisnis: mahasiswa mendapat diskon jika IPK tinggi dan status tertentu. Contoh logika teknis: if ipk >= 3.0 and status == "anak_karyawan": ...

2. NIM sebaiknya disimpan sebagai string karena formatnya bisa berisi angka dan karakter tertentu serta tidak boleh kehilangan angka depan nol. Jika disimpan sebagai integer, format data bisa berubah dan validasi menjadi lebih sulit.

3. Operator and berarti semua syarat harus benar, sedangkan or berarti salah satu syarat saja sudah cukup. Contoh and: IPK >= 3.5 dan SKS >= 24. Contoh or: status anak karyawan atau IPK >= 3.75.

4. Urutan kondisi sangat penting karena program mengecek dari atas ke bawah. Kondisi yang umum harus diletakkan setelah kondisi yang lebih spesifik agar tidak menutup akses ke kondisi berikutnya.

5. for loop digunakan untuk iterasi data yang sudah diketahui jumlahnya, seperti daftar mahasiswa. while loop digunakan jika pengulangan bergantung pada syarat tertentu, seperti memasukkan data sampai valid.

6. else pada loop dijalankan ketika perulangan selesai tanpa break. Jika break terjadi, maka blok else tidak dijalankan.

7. Validasi input harus dilakukan sebelum aturan bisnis agar data yang masuk benar dan tidak mengakibatkan error atau keputusan yang salah. Tanpa validasi, data tidak valid dapat merusak hasil program.

8. Validasi komposit berarti menggabungkan beberapa pengecekan dalam satu proses, misalnya NIM benar, nama tidak kosong, IPK 0.0-4.0, dan SKS sesuai batas. Jika ada satu syarat yang tidak terpenuhi, data ditolak.

## Bukti Hasil Soal Praktik

![Bukti hasil semua soal](bukti-semua-soal.png)
