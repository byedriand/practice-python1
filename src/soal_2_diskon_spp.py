"""Soal 2: kalkulator diskon SPP."""


def parse_uang(value: str) -> float:
    """Mengubah format uang seperti 1.500.000 atau 1.500.000,50 menjadi float."""
    teks = value.strip()
    if not teks:
        raise ValueError("Nilai uang tidak boleh kosong")
    teks = teks.replace(".", "").replace(",", ".")
    return float(teks)


def hitung_diskon(biaya_spp: float, anak_karyawan: bool, ipk: float, status_pembayaran: bool) -> tuple[float, float, float]:
    """Menghitung total diskon, potongan, dan biaya akhir."""
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


def main() -> None:
    """Menerima input biaya SPP dan menampilkan hasil diskon."""
    print("=== Soal 2 - Kalkulator Diskon SPP ===")
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


if __name__ == "__main__":
    main()
