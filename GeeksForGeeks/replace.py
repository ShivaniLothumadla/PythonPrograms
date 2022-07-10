a = '14, 30, 45.5, 98'
maketrans = a.maketrans
final = a.translate(maketrans('.,',',.',' '))
final = final.replace(',',', ')
print(final)

a = a.replace('.', 'a')
a = a.replace(',', '.')
a = a.replace('a', ',')
print(a)
