# s = input()
# l = u = d = p = 0
# if len(s) < 8:
#     print('Please enter minimum 8 characters')
# else:
#     for i in s:
#         if i.isupper():
#             u += 1
#         elif i.islower():
#             l += 1
#         elif i.isdigit():
#             d += 1
#         elif i == '@' or i == '_' or i == '$':
#             p += 1
#     if l >= 1 and u >= 1 and d >= 1 and p >= 1 and l+u+d+p == len(s):
#         print('Valid Password')
#     else:
#         print('Invalid Password')
import re
s = input()
flag = 0
while True:
    if not re.search('[a-z]', s):
        flag = 1
        print('enter atleast 1 lowercase letter')
        break
    elif not re.search('[A-Z]', s):
        flag = 1
        print('enter atleast 1 uppercase letter')
        break
    elif not re.search('[0-9]', s):
        flag = 1
        print('enter atleast 1 digit')
        break
    elif not re.search('[@_$]', s):
        flag = 1
        print('enter atleast 1 @/$/_ letter')
        break
    else:
        flag = 0
        print('Valid Password')
        break
if flag == 1:
    print('Invalid Password')



