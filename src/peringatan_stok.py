"""Soal Praktik 3: pengecekan stok inventaris."""


def status_stok(stok: int, aman: int, peringatan: int, rendah: int, habis: int) -> str:
    """Menentukan status stok berdasarkan ambang batas yang ditentukan."""
    if stok <= habis:
        return "Habis"
    if stok <= rendah:
        return "Rendah"
    if stok <= peringatan:
        return "Peringatan"
    return "Aman"


def evaluasi_inventaris(data: list[dict]) -> list[dict]:
    """Menambah status dan nilai pada setiap item inventaris."""
    hasil = []
    for item in data:
        status = status_stok(
            item["stok"],
            item["aman"],
            item["peringatan"],
            item["rendah"],
            item["habis"],
        )
        item_baru = dict(item)
        item_baru["status"] = status
        item_baru["nilai"] = item["stok"] * item["harga_satuan"]
        item_baru["prioritas"] = 1 if status in {"Rendah", "Habis"} else 2 if status == "Peringatan" else 3
        hasil.append(item_baru)
    return hasil


def main() -> None:
    """Menampilkan laporan lengkap inventaris dan statistik ringkasan."""
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

    print("=== Laporan Peringatan Stok ===")
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


if __name__ == "__main__":
    main()
