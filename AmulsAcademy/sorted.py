'''
sorted is a built in method for sorting the iterable either in ascending order or in descending order
sorted() is applicable for all the iterables like list, tuple, dictionary
syntax of the sorted: sorted(iterable,key=None,reverse=False)
sorted will not modify the existing iterable instead it gives the new iterable
here iterable is list/tuple/dictionary
key is None as default and we can change the key value to change the sorting process
reverse is False as default and it represents the ascending order,if we pass reverse as True means it is in descending order.
'''

print('ascending without key')
l = [20, 4, 12, 97, 89, 2, 100]
t = (2, 4, 18, 444, 87, 99, 6)
d = {1: 'a', 10: 'aaa', 34: 'jby', 8: 'yrfs', 2: 'hg'}
s = {1,3,7,5}
print(sorted(l))
print(sorted(t))
print(sorted(s))
print(sorted(d))  # it gives keys
print(sorted(d.keys())) # it gives keys
print(sorted(d.values())) # it gives values
print(sorted(d.items())) #it gives key and values in the form of list of tuples based on the keys.

print('descending without key')
l = [20, 4, 12, 97, 89, 2, 100]
t = (2, 4, 18, 444, 87, 99, 6)
d = {1: 'a', 10: 'aaa', 34: 'jby', 8: 'yrfs', 2: 'hg'}
print(sorted(l, reverse=True))
print(sorted(t, reverse=True))
print(sorted(s, reverse=True))
print(sorted(d, reverse=True))  # it gives keys
print(sorted(d.keys(), reverse=True)) # it gives keys
print(sorted(d.values(), reverse=True)) # it gives values
print(sorted(d.items(), reverse=True)) #it gives key and values in the form of list of tuples based on the keys.

print('ascending with key')
l = [[20, 4], [12, 97], [89, 2, 100]]
t = ((2, 4), (18, 444), (87, 99, 6))

print(sorted(l, key=len))
print(sorted(l, key=lambda x: x[1]))
print(sorted(t, key=len))
print(sorted(t, key=lambda x: x[1]))

print('descending with key')
l = [[20, 4], [12, 97], [89, 2, 100]]
t = ((2, 4), (18, 444), (87, 99, 6))

print(sorted(l, reverse=True, key=len))
print(sorted(t, reverse=True, key=len))




