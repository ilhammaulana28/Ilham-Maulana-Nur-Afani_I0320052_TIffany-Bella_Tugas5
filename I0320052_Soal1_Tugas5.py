print('Soal No.1')
# program sederhana untuk menyapa pengunjung sesuai gender
# input nama dan jenis kelamin
# output berupa kalimat "Selamat datang, nyonya/tuan *nama*!"
nama = input('Perkenalkan nama anda : ')
gender = input('Tuan / Nyonya         : ')
if gender == 'Tuan':
    print('Selamat datang, Tuan %s !' % nama)
else:
    print('Selamat datang, Nyonya %s !' % nama)
print()
