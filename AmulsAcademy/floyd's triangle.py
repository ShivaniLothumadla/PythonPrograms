num = int(input('Please enter a number: '))
n = 1
for i in range(1, num+1):
    for j in range(i):
        print(n, end=' ')
        n = n + 1
    print()

# output:
# Please a enter a number: 4
# 1
# 2 3
# 4 5 6
# 7 8 9 10