import pytest
from src.models import DaftarMahasiswa, Mahasiswa


def mahasiswa_contoh(nim: str = "2024SI001", ipk: float = 3.5) -> Mahasiswa:
    return Mahasiswa(nim, "Andi Pratama", "Sistem Informasi", 2024, ipk)


def test_buat_mahasiswa_valid() -> None:
    mahasiswa = mahasiswa_contoh()

    assert mahasiswa.nim == "2024SI001"
    assert mahasiswa.ipk == 3.5


def test_nim_kurang_dari_enam_karakter_ditolak() -> None:
    with pytest.raises(ValueError, match="NIM tidak valid"):
        Mahasiswa("abc", "Andi", "Sistem Informasi", 2024)


def test_nim_kosong_ditolak() -> None:
    with pytest.raises(ValueError, match="NIM tidak valid"):
        Mahasiswa("", "Andi", "Sistem Informasi", 2024)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError, match="Nama tidak boleh kosong"):
        Mahasiswa("2024SI001", "  ", "Sistem Informasi", 2024)


@pytest.mark.parametrize("ipk", [-0.1, 4.1])
def test_ipk_di_luar_rentang_ditolak(ipk: float) -> None:
    with pytest.raises(ValueError, match="IPK harus 0.0-4.0"):
        mahasiswa_contoh(ipk=ipk)


@pytest.mark.parametrize("ipk", [0.0, 4.0])
def test_ipk_batas_rentang_diterima(ipk: float) -> None:
    assert mahasiswa_contoh(ipk=ipk).ipk == ipk


def test_nama_panjang_dapat_disimpan() -> None:
    nama = "Nama Mahasiswa " * 20

    mahasiswa = Mahasiswa("2024SI001", nama, "Sistem Informasi", 2024)

    assert mahasiswa.nama == nama.strip()


def test_tambah_dan_cari_mahasiswa() -> None:
    daftar = DaftarMahasiswa()
    mahasiswa = mahasiswa_contoh()

    daftar.tambah(mahasiswa)

    assert daftar.cari("2024SI001") == mahasiswa
    assert daftar.jumlah == 1


def test_nim_duplikat_ditolak() -> None:
    daftar = DaftarMahasiswa()
    daftar.tambah(mahasiswa_contoh())

    with pytest.raises(ValueError, match="sudah terdaftar"):
        daftar.tambah(mahasiswa_contoh())


def test_cari_nim_yang_tidak_ada() -> None:
    assert DaftarMahasiswa().cari("2024SI999") is None


def test_hapus_mahasiswa() -> None:
    daftar = DaftarMahasiswa()
    daftar.tambah(mahasiswa_contoh())

    assert daftar.hapus("2024SI001") is True
    assert daftar.jumlah == 0


def test_hapus_nim_yang_tidak_ada() -> None:
    assert DaftarMahasiswa().hapus("2024SI999") is False


def test_perbarui_ipk() -> None:
    daftar = DaftarMahasiswa()
    daftar.tambah(mahasiswa_contoh())

    assert daftar.perbarui_ipk("2024SI001", 4.0) is True
    assert daftar.cari("2024SI001").ipk == 4.0


def test_perbarui_ipk_di_luar_rentang_ditolak() -> None:
    daftar = DaftarMahasiswa()
    daftar.tambah(mahasiswa_contoh())

    with pytest.raises(ValueError, match="IPK harus 0.0-4.0"):
        daftar.perbarui_ipk("2024SI001", 4.1)
