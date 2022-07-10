n = int(input('Please enter a number: '))
row = 0
while row < n:
    star = row + 1
    while star > 0:
        print('*', end=' ')
        star = star - 1
    row = row + 1
    print()

