str = input()
n = len(str)
# start = 0
# end = len(str)-1
# if n % 2 == 0:
#     mid = (len(str)-1) // 2 + 1
# else:
#     mid = (len(str)-1) // 2
# flag = 0
# while(start <= mid):
#     if str[start] == str[end]:
#         start += 1
#         end -= 1
#     else:
#         flag = 1
#         break
# if flag == 0:
#     print(f'{str} is a palindrome')
# else:
#     print(f'{str} is not a palindrome')

mid = int(n / 2)
if n % 2 == 0:
    first_half = str[:mid]
    second_half = str[mid:]
else:
    first_half = str[:mid]
    second_half = str[mid+1:]
if first_half == second_half:
    print(f'{str} is symmetric')
else:
    print(f'{str} is not symetric')
if first_half == second_half[::-1]:
    print(f'{str} is palindrome')
else:
    print(f'{str} is not a palindrome')
