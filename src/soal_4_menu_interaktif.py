"""Soal 4: menu interaktif untuk tiga studi kasus."""

from src.soal_1_status_mahasiswa import cek_status_mahasiswa
from src.soal_2_diskon_spp import hitung_diskon
from src.soal_3_peringatan_stok import evaluasi_inventaris


def main() -> None:
    """Program menu interaktif."""
    print("=== Soal 4 - Menu Interaktif ===")
    while True:
        print("\n1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("4. Kembali")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            nim = input("NIM: ").strip()
            nama = input("Nama: ").strip()
            ipk = float(input("IPK: "))
            sks = int(input("SKS: "))
            print(f"{nama} ({nim}) berstatus: {cek_status_mahasiswa(ipk, sks)}")
        elif pilihan == "2":
            biaya_spp = float(input("Biaya SPP: "))
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
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
