"""Model data dan operasi koleksi mahasiswa."""

from dataclasses import dataclass, field


@dataclass
class Mahasiswa:
    """Data seorang mahasiswa beserta validasi dasarnya."""

    nim: str
    nama: str
    program_studi: str
    angkatan: int
    ipk: float = 0.0

    def __post_init__(self) -> None:
        self.nim = self.nim.strip()
        self.nama = self.nama.strip()
        self.program_studi = self.program_studi.strip()

        if len(self.nim) < 6:
            raise ValueError(f"NIM tidak valid: {self.nim}")
        if not self.nama:
            raise ValueError("Nama tidak boleh kosong")
        if not self.program_studi:
            raise ValueError("Program studi tidak boleh kosong")
        if not 0.0 <= self.ipk <= 4.0:
            raise ValueError(f"IPK harus 0.0-4.0, bukan {self.ipk}")

    def __str__(self) -> str:
        return (
            f"{self.nim} | {self.nama:<30} | "
            f"{self.program_studi:<20} | {self.angkatan} | IPK: {self.ipk:.2f}"
        )


@dataclass
class DaftarMahasiswa:
    """Koleksi mahasiswa dengan operasi tambah, cari, hapus, dan edit IPK."""

    data: list[Mahasiswa] = field(default_factory=list)

    def tambah(self, mahasiswa: Mahasiswa) -> None:
        """Tambahkan mahasiswa jika NIM belum digunakan."""
        if self.cari(mahasiswa.nim) is not None:
            raise ValueError(f"NIM {mahasiswa.nim} sudah terdaftar")
        self.data.append(mahasiswa)

    def cari(self, nim: str) -> Mahasiswa | None:
        """Cari mahasiswa berdasarkan NIM."""
        for mahasiswa in self.data:
            if mahasiswa.nim == nim.strip():
                return mahasiswa
        return None

    def hapus(self, nim: str) -> bool:
        """Hapus mahasiswa berdasarkan NIM; kembalikan False jika tidak ada."""
        mahasiswa = self.cari(nim)
        if mahasiswa is None:
            return False
        self.data.remove(mahasiswa)
        return True

    def perbarui_ipk(self, nim: str, ipk: float) -> bool:
        """Perbarui IPK; nilai harus berada pada rentang 0.0 sampai 4.0."""
        if not 0.0 <= ipk <= 4.0:
            raise ValueError(f"IPK harus 0.0-4.0, bukan {ipk}")

        mahasiswa = self.cari(nim)
        if mahasiswa is None:
            return False
        mahasiswa.ipk = ipk
        return True

    @property
    def jumlah(self) -> int:
        """Jumlah mahasiswa yang tersimpan."""
        return len(self.data)
