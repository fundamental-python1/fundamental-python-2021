print ('tipe data skalar => tipe data sederhana')
anak1 = 'Eka'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print ('\nTipe data list/daftar/array')
anak = ['Eka', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Catur')
print(anak)

print ('\nsapa anak ke-2')
print(f'Hai {anak[1]}!')

print ('\nsapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print ('\nSapa semua anak : cara ribet')
for a in range(0,len(anak)):
    print(f'{a+1}. Hai {anak[a]}')
