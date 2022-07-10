# 7 X 21
for i in range(7):
    for j in range(21):
        if j == 21 // 2:
            print('|', end='')
        elif i == 7 // 2 and j == 21 // 2:
            print('welcome')
    print()
