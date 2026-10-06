"""Program utama gabungan untuk semua soal praktik 1-6."""

from __future__ import annotations


def parse_uang(value: str) -> float:
    """Mengubah format uang seperti 1.500.000 atau 1.500.000,50 menjadi float."""
    teks = value.strip()
    if not teks:
        raise ValueError("Nilai uang tidak boleh kosong")
    teks = teks.replace(".", "").replace(",", ".")
    return float(teks)


def cek_status_mahasiswa(ipk: float, sks: int) -> str:
    """Status mahasiswa berdasarkan IPK dan SKS."""
    if ipk >= 2.0 and sks >= 18:
        return "Aktif"
    if 1.5 <= ipk < 2.0:
        return "Peringatan"
    return "Tidak Aktif"


def program_status_mahasiswa() -> None:
    """Soal 1: menampilkan status lima mahasiswa."""
    print("\n=== Soal 1 - Status Mahasiswa ===")
    data = []

    for i in range(1, 6):
        nim = input(f"Mahasiswa {i} - NIM: ").strip()
        nama = input(f"Mahasiswa {i} - Nama: ").strip()
        ipk = float(input(f"Mahasiswa {i} - IPK: "))
        sks = int(input(f"Mahasiswa {i} - SKS: "))
        status = cek_status_mahasiswa(ipk, sks)
        data.append((nim, nama, ipk, sks, status))

    print("\nLaporan Status Mahasiswa")
    print("-" * 76)
    print(f"{'NIM':<12} {'Nama':<20} {'IPK':>6} {'SKS':>5} {'Status':<12}")
    print("-" * 76)
    for nim, nama, ipk, sks, status in data:
        print(f"{nim:<12} {nama:<20} {ipk:>5.1f} {sks:>5} {status:<12}")


def hitung_diskon(biaya_spp: float, anak_karyawan: bool, ipk: float, status_pembayaran: bool) -> tuple[float, float, float]:
    """Soal 2: menghitung diskon berdasarkan aturan program."""
    diskon_persen = 0.0

    if anak_karyawan:
        diskon_persen += 25
    if ipk >= 3.8:
        diskon_persen += 20
    elif ipk >= 3.5:
        diskon_persen += 15
    elif ipk >= 3.0:
        diskon_persen += 10
    if status_pembayaran:
        diskon_persen += 5

    potongan = biaya_spp * (diskon_persen / 100)
    total_biaya = biaya_spp - potongan
    return diskon_persen, potongan, total_biaya


def program_diskon_spp() -> None:
    """Soal 2: kalkulator diskon SPP."""
    print("\n=== Soal 2 - Kalkulator Diskon SPP ===")
    biaya_spp = parse_uang(input("Biaya SPP: "))
    anak_karyawan = input("Apakah anak karyawan? (y/n): ").strip().lower() == "y"
    ipk = float(input("IPK: "))
    status_pembayaran = input("Apakah sudah membayar? (y/n): ").strip().lower() == "y"

    diskon_persen, potongan, total_biaya = hitung_diskon(
        biaya_spp, anak_karyawan, ipk, status_pembayaran
    )

    print("\nRincian Diskon")
    print("-" * 40)
    print(f"Biaya SPP     : Rp {biaya_spp:,.2f}")
    print(f"Total diskon  : {diskon_persen:.0f}%")
    print(f"Potongan      : Rp {potongan:,.2f}")
    print(f"Biaya akhir   : Rp {total_biaya:,.2f}")


def status_stok(stok: int, aman: int, peringatan: int, rendah: int, habis: int) -> str:
    """Soal 3: menentukan status stok."""
    if stok <= habis:
        return "Habis"
    if stok <= rendah:
        return "Rendah"
    if stok <= peringatan:
        return "Peringatan"
    return "Aman"


def evaluasi_inventaris(data: list[dict]) -> list[dict]:
    """Menambahkan status, nilai, dan prioritas untuk setiap item."""
    hasil = []
    for item in data:
        item_baru = dict(item)
        item_baru["status"] = status_stok(
            item["stok"], item["aman"], item["peringatan"], item["rendah"], item["habis"]
        )
        item_baru["nilai"] = item["stok"] * item["harga_satuan"]
        if item_baru["status"] in {"Rendah", "Habis"}:
            item_baru["prioritas"] = 1
        elif item_baru["status"] == "Peringatan":
            item_baru["prioritas"] = 2
        else:
            item_baru["prioritas"] = 3
        hasil.append(item_baru)
    return hasil


def program_inventaris() -> None:
    """Soal 3: program laporan stok inventaris."""
    print("\n=== Soal 3 - Peringatan Stok ===")
    inventaris = [
        {"nama": "Mouse", "stok": 40, "aman": 30, "peringatan": 20, "rendah": 10, "habis": 0, "harga_satuan": 120000},
        {"nama": "Keyboard", "stok": 18, "aman": 25, "peringatan": 15, "rendah": 8, "habis": 0, "harga_satuan": 220000},
        {"nama": "Monitor", "stok": 7, "aman": 12, "peringatan": 8, "rendah": 3, "habis": 0, "harga_satuan": 1500000},
        {"nama": "CPU", "stok": 25, "aman": 20, "peringatan": 12, "rendah": 6, "habis": 0, "harga_satuan": 3500000},
        {"nama": "Printer", "stok": 4, "aman": 10, "peringatan": 6, "rendah": 2, "habis": 0, "harga_satuan": 1800000},
        {"nama": "UPS", "stok": 0, "aman": 8, "peringatan": 5, "rendah": 2, "habis": 0, "harga_satuan": 700000},
        {"nama": "Router", "stok": 11, "aman": 15, "peringatan": 10, "rendah": 4, "habis": 0, "harga_satuan": 900000},
        {"nama": "Scanner", "stok": 2, "aman": 9, "peringatan": 5, "rendah": 1, "habis": 0, "harga_satuan": 950000},
    ]

    hasil = evaluasi_inventaris(inventaris)
    total_nilai = sum(item["nilai"] for item in hasil)
    total_habis = sum(1 for item in hasil if item["status"] == "Habis")
    total_rendah = sum(1 for item in hasil if item["status"] == "Rendah")
    total_peringatan = sum(1 for item in hasil if item["status"] == "Peringatan")
    total_aman = sum(1 for item in hasil if item["status"] == "Aman")

    print(f"{'Nama':<15} {'Stok':>5} {'Status':<12} {'Prioritas':>9} {'Nilai':>15}")
    print("-" * 70)
    for item in hasil:
        print(f"{item['nama']:<15} {item['stok']:>5} {item['status']:<12} {item['prioritas']:>9} {item['nilai']:>15,.0f}")

    print("\nRingkasan Statistik")
    print("-" * 45)
    print(f"Total nilai inventaris : Rp {total_nilai:,.0f}")
    print(f"Aman                  : {total_aman}")
    print(f"Peringatan            : {total_peringatan}")
    print(f"Rendah                : {total_rendah}")
    print(f"Habis                 : {total_habis}")


def menu_interaktif() -> None:
    """Soal 4: menu interaktif untuk tiga studi kasus."""
    print("\n=== Soal 4 - Menu Interaktif ===")
    while True:
        print("\n1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("4. Kembali ke menu utama")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            nim = input("NIM: ").strip()
            nama = input("Nama: ").strip()
            ipk = float(input("IPK: "))
            sks = int(input("SKS: "))
            print(f"{nama} ({nim}) berstatus: {cek_status_mahasiswa(ipk, sks)}")
        elif pilihan == "2":
            biaya_spp = parse_uang(input("Biaya SPP: "))
            anak_karyawan = input("Anak karyawan? (y/n): ").strip().lower() == "y"
            ipk = float(input("IPK: "))
            lunas = input("Sudah membayar? (y/n): ").strip().lower() == "y"
            diskon_persen, potongan, total = hitung_diskon(biaya_spp, anak_karyawan, ipk, lunas)
            print(f"Diskon: {diskon_persen:.0f}%")
            print(f"Potongan: Rp {potongan:,.2f}")
            print(f"Biaya akhir: Rp {total:,.2f}")
        elif pilihan == "3":
            data = [
                {"nama": "Mouse", "stok": int(input("Stok Mouse: ")), "aman": 30, "peringatan": 20, "rendah": 10, "habis": 0, "harga_satuan": 120000},
                {"nama": "Keyboard", "stok": int(input("Stok Keyboard: ")), "aman": 25, "peringatan": 15, "rendah": 8, "habis": 0, "harga_satuan": 220000},
            ]
            hasil = evaluasi_inventaris(data)
            for item in hasil:
                print(f"{item['nama']}: {item['status']} (prioritas {item['prioritas']})")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")


def validasi_data_mahasiswa(nim: str, nama: str, ipk: float, sks: int, semester: int) -> list[str]:
    """Soal 5: validasi data mahasiswa."""
    errors: list[str] = []

    if len(nim) != 10 or not nim.isdigit():
        errors.append("NIM harus 10 digit angka")
    else:
        tahun = int(nim[:4])
        if not 2000 <= tahun <= 2037:
            errors.append("Tahun pada NIM harus 2000-2037")

    if not nama.strip():
        errors.append("Nama tidak boleh kosong")

    if not 0.0 <= ipk <= 4.0:
        errors.append("IPK harus antara 0.0 sampai 4.0")

    if not 0 <= sks <= 24:
        errors.append("SKS harus antara 0 sampai 24")

    if not 1 <= semester <= 14:
        errors.append("Semester harus antara 1 sampai 14")

    return errors


def program_validasi_data() -> None:
    """Soal 5: validasi input mahasiswa."""
    print("\n=== Soal 5 - Validasi Data Mahasiswa ===")
    nim = input("NIM: ").strip()
    nama = input("Nama: ").strip()
    ipk = float(input("IPK: "))
    sks = int(input("SKS: "))
    semester = int(input("Semester: "))

    errors = validasi_data_mahasiswa(nim, nama, ipk, sks, semester)
    if not errors:
        print("Data mahasiswa valid.")
    else:
        print("Terdapat kesalahan:")
        for error in errors:
            print(f"- {error}")


def hitung_status_ringkasan(ipk: float, sks: int) -> str:
    """Status untuk ringkasan soal 6."""
    return cek_status_mahasiswa(ipk, sks)


def ringkasan_algoritma() -> None:
    """Soal 6: menghitung ringkasan data dari soal sebelumnya."""
    print("\n=== Soal 6 - Ringkasan Algoritma ===")
    mahasiswa = [
        (3.8, 20),
        (2.4, 18),
        (1.6, 16),
        (1.3, 9),
        (3.1, 19),
    ]
    diskon_data = [
        (2500000, True, 3.9, True),
        (2000000, False, 3.4, True),
        (1800000, False, 3.2, False),
        (2300000, True, 3.7, True),
    ]
    stok_data = [
        (12, 20, 15, 7, 0),
        (5, 20, 15, 7, 0),
        (0, 20, 15, 7, 0),
        (30, 20, 15, 7, 0),
        (8, 20, 15, 7, 0),
    ]

    aktif = sum(1 for ipk, sks in mahasiswa if hitung_status_ringkasan(ipk, sks) == "Aktif")
    tidak_aktif = sum(1 for ipk, sks in mahasiswa if hitung_status_ringkasan(ipk, sks) == "Tidak Aktif")
    total_mahasiswa = len(mahasiswa)
    persentase_aktif = (aktif / total_mahasiswa) * 100 if total_mahasiswa else 0
    persentase_tidak_aktif = (tidak_aktif / total_mahasiswa) * 100 if total_mahasiswa else 0

    rata_diskon = sum(
        hitung_diskon(biaya, anak, ipk, bayar)[0] for biaya, anak, ipk, bayar in diskon_data
    ) / len(diskon_data)

    butuh_restock = sum(
        1
        for stok, aman, peringatan, rendah, habis in stok_data
        if status_stok(stok, aman, peringatan, rendah, habis) in {"Rendah", "Habis", "Peringatan"}
    )
    persentase_restock = (butuh_restock / len(stok_data)) * 100 if stok_data else 0

    print(f"{'Kategori':<28} {'Nilai':>10}")
    print("-" * 40)
    print(f"{'Mahasiswa aktif':<28} {persentase_aktif:>9.2f}%")
    print(f"{'Mahasiswa tidak aktif':<28} {persentase_tidak_aktif:>9.2f}%")
    print(f"{'Rata-rata diskon':<28} {rata_diskon:>9.2f}%")
    print(f"{'Persentase perlu restock':<28} {persentase_restock:>9.2f}%")


def main() -> None:
    """Menu utama gabungan untuk semua latihan soal."""
    while True:
        print("\n=== Program Latihan Praktik Python ===")
        print("1. Soal 1 - Status Mahasiswa")
        print("2. Soal 2 - Diskon SPP")
        print("3. Soal 3 - Peringatan Stok")
        print("4. Soal 4 - Menu Interaktif")
        print("5. Soal 5 - Validasi Data")
        print("6. Soal 6 - Ringkasan Algoritma")
        print("0. Keluar")

        pilihan = input("Pilih nomor soal: ").strip()

        if pilihan == "1":
            program_status_mahasiswa()
        elif pilihan == "2":
            program_diskon_spp()
        elif pilihan == "3":
            program_inventaris()
        elif pilihan == "4":
            menu_interaktif()
        elif pilihan == "5":
            program_validasi_data()
        elif pilihan == "6":
            ringkasan_algoritma()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 0-6.")


if __name__ == "__main__":
    main()
