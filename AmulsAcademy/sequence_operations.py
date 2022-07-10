'''
10 types of sequence operations
sequence operations can perform on list, tuple and strings
sequence oprations:
1.length
2.select
3.slice
4.min
5.max
6.sum
7.count
8.index
9.membership
10.concatination
'''
lst = [1, 2, 3, 4, 5, 6]
tp = (1, 2, 3, 4, 5, 6)
str = '123456'

#1.length
print(len(lst))
print(len(tp))
print(len(str))

#2.select
print(lst[1])
print(tp[1])
print(str[1])

#3.slice
print(lst[::-1])
print(tp[::-1])
print(str[::-1])

#4.count
print(lst.count(3))
print(tp.count(3))
print(str.count('3'))

#5.index
print(lst.index(4))
print(tp.index(4))
print(str.index('4'))

#6.min
print(min(lst))
print(min(tp))
print(min(str))

#7.max
print(max(lst))
print(max(tp))
print(max(str))

#8.membership
#in
print(1 in lst)
print(1 in tp)
print('1' in str)
#not in
print(1 not in lst)
print(1 not in tp)
print('1' not in str)

#9.concatenation
lst2 = [3, 4, 5, 6, 7]
tp2 = (3, 4, 5, 6, 7)
str2 = '34567'
print(lst + lst2)
print(tp + tp2)
print(str + str2)

#10.sum
print(sum(lst))
print(sum(tp))
# print(sum(str))   we canot perform sum operation on string