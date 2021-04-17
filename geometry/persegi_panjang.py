from geometry.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, panjang, lebar):
        # fungsi yang dipanggil pertama kali saat objek dibuat
        self.panjang = panjang
        self.lebar = lebar

    def info(self):
        return f'Ini adalah objek persegi panjang dengan panjang = {self.panjang} dan lebar = {self.lebar}'

    def hitung_luas(self):
        return self.panjang * self.lebar
