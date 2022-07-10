def palindrome(num):
    temp = num
    sum = 0
    while(num > 0):
        rem = num % 10
        sum = sum * 10 + rem
        num = int(num / 10)
    return (temp == sum)

def palinlimit(min, max):
    for num in range(min, max):
        pnum = palindrome(num)
        if pnum:
            print(num, end=' ')

palinlimit(110, 200)

# num = int(input())
# rnum = ''.join(reversed(str(num)))
# if num == int(rnum):
#     print(f'{num} is palindrome number')
# else:
#     print(f'{num} is not a palindrome number')