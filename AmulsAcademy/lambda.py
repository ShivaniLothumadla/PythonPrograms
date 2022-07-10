# lambda is an anonymous function
# we can use 3 functions along with lambda
#1.map(),2.reduce(),3.filter()
#list/tuple(map(function, iterable))is the syntax of map function
#map is used to perform the same operation on the iterable like square
#normal function to perform square
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
def sqr(n):
    return n * n
for i in a:
    print(sqr(i), end=' ')
print()
# using map function
print(list(map(sqr, a)))
# using lambda function and map
print(tuple(map(lambda x: x*x, a)))
#map function accepts one or more iterables
print(list(map(lambda x,y: x+y, a, b)))
#filter function is used to filter out the iterable based on the condition and it gives only true values
print(list(filter(lambda x: x % 2 == 0, a)))
#reduce function is used to get a single element upon the iterable by performing computation operations like sum,prod
import functools
c = [1, 2, 3, 4, 5, 6]
print(functools.reduce(lambda x, y: x * y, c))
