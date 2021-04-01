print('Soal No.2')
# grading nilai
# input nama pengguna dan nilai yang berupa angka
# output "Halo,...! Nilai anda setelah dikonversi adalah.."
# < 60 = E
# 60-64 = C
# 65-69 = C+
# 70-74 = B
# 75-79 = B+
# 80-84 = A-
# 85-100 = A
print('KONVERSI NILAI ANDA')
nama = input('Masukkan nama anda : ')
nilai = float(input('Masukkan nilai anda : '))
if nilai < 60:
    print('Halo, %s ! Nilai anda setelah dikonversi adalah E'% nama)
elif nilai < 65:
    print('Halo, %s ! Nilai anda setelah dikonversi adalah C' % nama)
elif nilai < 70:
    print('Halo, %s ! Nilai anda setelah dikonversi adalah C+' % nama)
elif nilai < 75:
    print('Halo, %s ! Nilai anda setelah dikonversi adalah B' % nama)
elif nilai < 80:
    print('Halo, %s ! Nilai anda setelah dikonversi adalah B+' % nama)
elif nilai < 85:
    print('Halo, %s ! Nilai anda setelah dikonversi adalah A-' % nama)
else:
    print('Halo, %s ! Nilai anda setelah dikonversi adalah A' % nama)
print()