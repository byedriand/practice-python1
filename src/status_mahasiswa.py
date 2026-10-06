"""Soal Praktik 1: laporan status mahasiswa."""


def cek_status_mahasiswa(ipk: float, sks: int) -> str:
    """Mengembalikan status mahasiswa berdasarkan IPK dan SKS."""
    if ipk >= 2.0 and sks >= 18:
        return "Aktif"
    if 1.5 <= ipk < 2.0:
        return "Peringatan"
    return "Tidak Aktif"


def main() -> None:
    """Menerima data 5 mahasiswa lalu menampilkan laporan status."""
    print("=== Program Status Mahasiswa ===")
    data = []

    for i in range(1, 6):
        nim = input(f"Mahasiswa {i} - NIM: ").strip()
        nama = input(f"Mahasiswa {i} - Nama: ").strip()
        ipk = float(input(f"Mahasiswa {i} - IPK: "))
        sks = int(input(f"Mahasiswa {i} - SKS: "))
        status = cek_status_mahasiswa(ipk, sks)
        data.append((nim, nama, ipk, sks, status))

    print("\nLaporan Status Mahasiswa")
    print("-" * 75)
    print(f"{'NIM':<12} {'Nama':<20} {'IPK':>6} {'SKS':>5} {'Status':<12}")
    print("-" * 75)
    for nim, nama, ipk, sks, status in data:
        print(f"{nim:<12} {nama:<20} {ipk:>5.1f} {sks:>5} {status:<12}")


if __name__ == "__main__":
    main()
