# used to update the list for example to multiply by 10
a = [1, 2, 3, 4]
print(a * 10)  # it gives the list by 10 times
# using list comprehension
b = [i * 10 for i in a]
print(b)

#it used to change the case of the word
a = ['i', 'am', 'shivani']
b = [i.upper() for i in a]
print(' '.join(b))
c = ['S', 'H', 'I', 'V', 'A', 'N', 'I']
d = [i.lower() for i in c]
print(''.join(d))
# to extract the digits/charactes from the given string
a = ['S', 'H', 'I', 'V', 'A', 'N', 'I', '12', '2']
b = [i for i in a if i.isdigit()]
print(len(b))
c = [i for i in a if i.isalpha()]
print(''.join(c))
c = [i for i in a if i.isupper()]
print(''.join(c))
# to perform operations on function
a = [i*i for i in range(1, 11)]
print(a)
# to perform to add 2 lists
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
c = [x + y for x in a for y in b]
print(c)
# to add based on corresponding index
c = [a[x] + b[x] for x in range(len(a))]
print(c)
# to find even/odd numbers
c = [i for i in range(11) if i % 2 != 0]
print(c)
'''list comprehension is substitute for
for loop
lambda
map
filter
reduce
'''
# to know the execution time using timeit
import timeit
a = ['1', '2', '3']
# print(timeit.timeit('list(map(lambda x: int(x), a'))
print(timeit.timeit('[int(i) for i in a]'))