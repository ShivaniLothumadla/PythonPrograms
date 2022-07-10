# str = input()
# n = len(str)
# # start1 = 0
# # if n%2 == 0:
# #     mid = (len(str)-1) // 2 + 1
# # else:
# #     mid = (len(str)-1) // 2
# # start2 = mid
# # flag = 0
# # while(start1 < mid and start2 < len(str)):
# #     if(str[start1] == str[start2]):
# #         start1 += 1
# #         start2 += 1
# #     else:
# #         flag = 1
# #         break
# # if flag == 0:
# #     print(f'{str} is a symmetric')
# # else:
# #     print(f'{str} is not symmetric')
# mid = int(n/2)
# if n % 2 == 0:
#     first_str = str[:mid]
#     last_str = str[mid:]
# else:
#     first_str = str[:mid]
#     last_str = str[mid+1:]
# if first_str == last_str:
#     print(f'{str} is symetric')
# else:
#     print(f'{str} is not symetric')

a = 'state'
b = 'taste'
if sorted(a) == sorted(b):
    print(f'{a} and {b} are anagram strings.')
else:
    print(f'{a} and {b} are not anagram strings.')

