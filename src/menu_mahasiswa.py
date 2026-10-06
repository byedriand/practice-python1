"""Soal Praktik 4: menu interaktif untuk tiga studi kasus."""

try:
    from src.status_mahasiswa import cek_status_mahasiswa
    from src.diskon_biaya import hitung_diskon
    from src.peringatan_stok import evaluasi_inventaris, status_stok
except ImportError:
    from status_mahasiswa import cek_status_mahasiswa
    from diskon_biaya import hitung_diskon
    from peringatan_stok import evaluasi_inventaris, status_stok


def menu_status_mahasiswa() -> None:
    """Submenu untuk mengecek status mahasiswa."""
    print("\n=== Cek Status Mahasiswa ===")
    nim = input("NIM: ").strip()
    nama = input("Nama: ").strip()
    ipk = float(input("IPK: "))
    sks = int(input("SKS: "))
    status = cek_status_mahasiswa(ipk, sks)
    print(f"{nama} ({nim}) berstatus: {status}")


def menu_diskon_biaya() -> None:
    """Submenu untuk menghitung diskon biaya SPP."""
    print("\n=== Hitung Diskon Biaya ===")
    biaya_spp = float(input("Biaya SPP: "))
    anak_karyawan = input("Anak karyawan? (y/n): ").strip().lower() == "y"
    ipk = float(input("IPK: "))
    lunas = input("Sudah membayar? (y/n): ").strip().lower() == "y"
    diskon_persen, potongan, total = hitung_diskon(biaya_spp, anak_karyawan, ipk, lunas)
    print(f"Diskon: {diskon_persen:.0f}%")
    print(f"Potongan: Rp {potongan:,.2f}")
    print(f"Biaya akhir: Rp {total:,.2f}")


def menu_peringatan_stok() -> None:
    """Submenu untuk mengecek stok inventaris."""
    print("\n=== Cek Peringatan Stok ===")
    data = [
        {"nama": "Mouse", "stok": int(input("Stok Mouse: ")), "aman": 30, "peringatan": 20, "rendah": 10, "habis": 0, "harga_satuan": 120000},
        {"nama": "Keyboard", "stok": int(input("Stok Keyboard: ")), "aman": 25, "peringatan": 15, "rendah": 8, "habis": 0, "harga_satuan": 220000},
    ]
    hasil = evaluasi_inventaris(data)
    for item in hasil:
        print(f"{item['nama']}: {item['status']} (prioritas {item['prioritas']})")


def main() -> None:
    """Menampilkan menu utama dan menjalankan submenu sesuai pilihan."""
    while True:
        print("\n=== Menu Studi Kasus ===")
        print("1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("4. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            menu_status_mahasiswa()
        elif pilihan == "2":
            menu_diskon_biaya()
        elif pilihan == "3":
            menu_peringatan_stok()
        elif pilihan == "4":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
