n = int(input('Please enter a number: '))
for row in range(n + 1):
    for col in range(n + 1):
        if row + col == 2 or row - col == 2 or col - row == 2 or row + col == 6:
            print('*', end=' ')
        else:
            print(end='  ')
    print()