from geometry.bangun_ruang import BangunRuang


class SegiTiga(BangunRuang):
    def __init__(self, alas, tinggi):
        # fungsi yang dipanggil pertama kali saat objek dibuat
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Ini adalah objek segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi}'

    def hitung_luas(self):
        return self.alas * self.tinggi / 2