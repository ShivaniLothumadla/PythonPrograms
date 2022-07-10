empty_set = set()
# print(empty_set)
st1 = {1, 2, 3, 4, 5, 6, 6}
st2 = set(st1)
st3 = set(st1).copy()
# print(st1)
# print(st2)
# print(st3)
st1.add(7)
# print(st1)
# print(st2)
# print(st3)
# st4 = frozenset([1, 3, 4, 5, 6])
# print(st4)
st3.add(88)
# if 88 in st3:
#     print('True')
# else:
#     print('False')
# print(st3)
st2.remove(4)
print(st1)
print(st2)
# union
print(st1 | st2)
# #clear
# st3.clear()
# print(st3)
# intersection
print(st1 & st2)
#difference
print(st1 - st2)
#symetric difference
#it gives uncommon elements from both sets
print(st1 ^ st2)
#size
print(len(st1))
# copy
st5 = st1.copy()
print(st5)