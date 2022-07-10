a = 'state'
b = 'tastet'
if sorted(a) == sorted(b):
    print(f'{a} and {b} are anagram strings.')
else:
    print(f'{a} and {b} are Not anagram strings.')
# count = 0
# # for i in a:
# #     if i in b:
# #         count += 1
# # if count == len(a):
# #     print('YES')
# # else:
# #     print('NO')
# for i in a:
#     for j in b:
#         if i == j:
#             count += 1
#             x = b.find(i)
#             b = b.replace(b[x], '*')
# if count == len(a):
#     print('YES')
# else:
#     print('NO')
