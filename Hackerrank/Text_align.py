# width = 10
# word = 'shivani'
# print(word.ljust(width, '-'))
# print(word.center(width, '*'))
# print(word.rjust(width, '$'))
f = None
n = 10
if n %2 == 0 and 0 < n < 50:
    f = n
for i in range(1, n):
    if i % 2 != 0:
        h = 'H'.center(n-i, ' ')
        print(h, end='')
    else:
        continue
print()
# for i in range(0, n):
#     for j in range(0, n):
#         if j == n/2:
#              h = 'H'.rjust(10, ' ')
#         else:
#             h = 'H'
#         print(h, end='')
#     print()
