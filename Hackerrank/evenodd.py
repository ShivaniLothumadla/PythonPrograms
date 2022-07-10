#input
a = [2, 4, 5, 8, 10, 20, 26, 1]
# output 20, 10, 26, 8, 4, 2, 5, 1
even =sorted([i for i in a if i % 2 == 0],reverse=True)
odd = [i for i in a if i % 2 != 0]
# for i in a:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
even = sorted(even, reverse=True)
# print(even)
even_5 = [i for i in even if i % 5 == 0]
even_n5 = [i for i in even if i % 5 != 0]
# for i in even:
#     if i % 5 == 0:
#         even_5.append(i)
#     else:
#         even_n5.append(i)
# print(even_5)
# print(even_n5)
# print(odd)
l = even_5 + even_n5 + odd
# print(l)
for i in l:
    k = ''.join(str(i))
    print(k, end=' ')