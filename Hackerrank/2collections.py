l1 = ['abc', 'bcd', 'efg']
l2 = ['xyz', 'rfg', 'jju', 'uym', 'abs', 'mno','uuh']
k = 0
for i in range(len(l2)):
    if i >= len(l1):
        k = len(l1)
    print(f'{l1[i-k]} - {l2[i-k]}')