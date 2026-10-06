"""Soal 6: ringkasan algoritma dari soal sebelumnya."""

from src.soal_1_status_mahasiswa import cek_status_mahasiswa
from src.soal_2_diskon_spp import hitung_diskon
from src.soal_3_peringatan_stok import status_stok


def main() -> None:
    """Menampilkan ringkasan data dari soal 1 sampai 3."""
    print("=== Soal 6 - Ringkasan Algoritma ===")
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

    aktif = sum(1 for ipk, sks in mahasiswa if cek_status_mahasiswa(ipk, sks) == "Aktif")
    tidak_aktif = sum(1 for ipk, sks in mahasiswa if cek_status_mahasiswa(ipk, sks) == "Tidak Aktif")
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


if __name__ == "__main__":
    main()
