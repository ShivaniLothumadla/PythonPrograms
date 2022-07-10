# Capitalizing first and last element of the string

str = input()
# str = str.split(' ')
# str1 = []
# for s in str:
#     if len(s) == 1:
#         st = s[0].upper()
#     else:
#         st = s[0].upper() + s[1:len(s)-1] + s[-1].upper()
#     str1.append(st)
# str = ' '.join(str1)
# print(str)
if len(str) == 1:
    str = str[0].upper()
else:
    str = list(map(str[0].upper() + str[1:-1] + str[-1].upper(), str))
print(''.join(str))

# capitalizing the first element of the string
# s = input()
# print(s.title())