n = 5
# while(n != 0):
#     print((n-1)*(n-1))
#     n -= 1
k = [str(i*i) for i in range(n)]
# print(type(k))
print('\n'.join(k))
# print(type(k))
for i in range(n):
    print(i*i)