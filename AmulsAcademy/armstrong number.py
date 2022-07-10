# Armstrong number : The number of n digits is equal to the sum of the nth power of it digits.
for i in range(10):
    num = i
    result = 0
    length = len(str(i))
    while i != 0:
        digit = i % 10
        result = result + digit ** length
        i = i // 10
    if num == result:
        print(num, end=' ')
