"""Soal Praktik 6: ringkasan algoritma dari tiga studi kasus."""


def hitung_status_mahasiswa(ipk: float, sks: int) -> str:
    """Status mahasiswa sesuai aturan tugas."""
    if ipk >= 2.0 and sks >= 18:
        return "Aktif"
    if 1.5 <= ipk < 2.0:
        return "Peringatan"
    return "Tidak Aktif"


def hitung_diskon(biaya_spp: float, anak_karyawan: bool, ipk: float, status_pembayaran: bool) -> float:
    """Mengembalikan total persen diskon."""
    diskon = 0.0
    if anak_karyawan:
        diskon += 25
    if ipk >= 3.8:
        diskon += 20
    elif ipk >= 3.5:
        diskon += 15
    elif ipk >= 3.0:
        diskon += 10
    if status_pembayaran:
        diskon += 5
    return diskon


def status_stok(stok: int, aman: int, peringatan: int, rendah: int, habis: int) -> str:
    """Status stok berdasarkan ambang batas."""
    if stok <= habis:
        return "Habis"
    if stok <= rendah:
        return "Rendah"
    if stok <= peringatan:
        return "Peringatan"
    return "Aman"


def tampilkan_tabel(data: list[tuple[str, str]]) -> None:
    """Tampilkan data ringkasan dalam format tabel sederhana."""
    print(f"{'Kategori':<28} {'Nilai':>10}")
    print("-" * 40)
    for kategori, nilai in data:
        print(f"{kategori:<28} {nilai:>10}")


def main() -> None:
    """Menghitung ringkasan dari studi kasus mahasiswa, diskon, dan stok."""
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

    aktif = sum(1 for ipk, sks in mahasiswa if hitung_status_mahasiswa(ipk, sks) == "Aktif")
    tidak_aktif = sum(1 for ipk, sks in mahasiswa if hitung_status_mahasiswa(ipk, sks) == "Tidak Aktif")
    total_mahasiswa = len(mahasiswa)
    persentase_aktif = (aktif / total_mahasiswa) * 100 if total_mahasiswa else 0
    persentase_tidak_aktif = (tidak_aktif / total_mahasiswa) * 100 if total_mahasiswa else 0

    rata_diskon = sum(hitung_diskon(biaya, anak, ipk, bayar) for biaya, anak, ipk, bayar in diskon_data) / len(diskon_data)

    butuh_restock = sum(
        1 for stok, aman, peringatan, rendah, habis in stok_data if status_stok(stok, aman, peringatan, rendah, habis) in {"Rendah", "Habis", "Peringatan"}
    )
    total_stok = len(stok_data)
    persentase_restock = (butuh_restock / total_stok) * 100 if total_stok else 0

    print("=== Ringkasan Algoritma ===")
    tampilkan_tabel([
        ("Mahasiswa aktif", f"{persentase_aktif:.2f}%"),
        ("Mahasiswa tidak aktif", f"{persentase_tidak_aktif:.2f}%"),
        ("Rata-rata diskon", f"{rata_diskon:.2f}%"),
        ("Persentase perlu restock", f"{persentase_restock:.2f}%"),
    ])


if __name__ == "__main__":
    main()
