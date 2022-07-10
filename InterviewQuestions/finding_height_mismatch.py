# a = [1, 1, 3, 3, 4, 1]
# count = 0
# l = len(a)
# for i in range(0, l):
#     j = i
#     for j in range(0, l-1):
#         if a[j] > a[j+1]:
#             globals()['count'] += 1
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)
# print(count)


# mylist = [1,2,3]
# copymylist = mylist
# print(mylist)
# print(copymylist)
# print(mylist)

#second maximum number
# a = [1,4,6,4]
# print(a)
# print(sorted(a))
# b = set(sorted(a))
# b.remove(max(b))
# print(max(b))

# reverse words in a string
# a = 'welcome to python programming'
# words = a.split(" ")
# print(words)
# r = words[::-1]
# print(r)
# rw = ' '.join(r)
# print(rw)

# separating vowels and constants from a string
# a = 'shivani lothumadla'
# o ,c = [], []
# for i in range(len(a)):
#     if a[i] in ['a','e','i','o','u']:
#         globals()['o'] += a[i]
#     else:
#         globals()['c'] += a[i]
# print(a)
# print(o)
# print(c)


# l = [2,3,4,5,6,7,8,9]
# l1 = l[:]
# print(l)
# print(l1)

# a = '110a'
# print(int(a))

# dimensional program
for i in range(5):
    for j in range(0, 5-i):
        print('*', end=' ')
    print(" ")
