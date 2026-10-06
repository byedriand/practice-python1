"""Soal Praktik 5: validasi data mahasiswa."""


def validasi_data_mahasiswa(nim: str, nama: str, ipk: float, sks: int, semester: int) -> list[str]:
    """Mengembalikan list error jika ada data yang tidak valid."""
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


def main() -> None:
    """Menerima input data mahasiswa dan menampilkan hasil validasi."""
    print("=== Validasi Data Mahasiswa ===")
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


if __name__ == "__main__":
    main()
