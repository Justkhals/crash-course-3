from geometry.bangun_ruang import BangunRuang
from geometry.persegi_panjang import PersegiPanjang
from geometry.segitiga import SegiTiga

print('OOP Program')

persegi_panjang = PersegiPanjang(10, 3)
print(persegi_panjang.info())
print(persegi_panjang.hitung_luas())

segitiga = SegiTiga(4, 2)
print(segitiga.info())
print(segitiga.hitung_luas())

print('Mencoba membuat objek dengan class BangunRuag')
bangun_ruang = BangunRuang()
print(bangun_ruang.info())

# Polymorphism: kemampuan objek untuk meresponse berbeda terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(persegi_panjang)
daftar_bangun_ruang.append(segitiga)

print('\nPolymorphism')
for bangun_ruang_member in daftar_bangun_ruang:
    print(bangun_ruang_member.info())
