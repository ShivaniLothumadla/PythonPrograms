a = ['999', '1,499', '1,999']
for i in range(len(a)):
    if ',' in a[i]:
        a[i] = int(a[i].replace(',',''))
print()
print(max(a))