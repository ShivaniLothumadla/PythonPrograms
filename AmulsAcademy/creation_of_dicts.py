# 4 ways to create dict
# 1st way is taking empty dict and add one by one
my_dict = {}
print(my_dict)
my_dict[0]='llll'
my_dict[1]='2222'
my_dict[2]='3333'
print(my_dict)

# 2nd way is to create a dict with key values
my_dict = {1: 'shiva', 2.0: 'ayan', 'sahasra': 'cherry', (8,9): 'mango'}
my_dict[9]= 'john'
print(my_dict)

# 3rd way is to create using dict constructor and list of tuples
my_dict = dict([(1,'amm'), (2,'ewr'), (3,'war')])
print(my_dict)

# 4th way is to create using 2 lists having same legnth
l1 = [1,2,3,4]
l2 = ['shivani', 'lavanya', 'ayan', 'srinivas']
my_dict = {}
for i in range(len(l1)):
    my_dict[l1[i]] = l2[i]
print(my_dict)
print(my_dict.keys())
print(list(my_dict.values()))
print(my_dict.get(1))

# creating a dictionary using fromkeys() method
# fromkeys takes iterable as keys
# my_dict = dict.fromkeys((1,2,3,4,5),[0,2])
my_dict = dict.fromkeys(range(1,7), 9)
print(my_dict)
tuplee = (1,)
intt = (1)
print(type(tuplee))
print(type(intt))

#setdefault method in dictionary
# it takes keys as a parameter and search for the key in dictionary.If key is present in dictionary it gives the coresponding value of the key.
#if key is not present,then the key will be added to the dictionary as a key and None will be the value of that key as we didnot pass the value.
#Here in setdefault(key,value),key will be mandatory where as value is optional.If you pass the value along with key then the corresponding value will be added in ditionary instead of None.

print(my_dict)
# print(my_dict.setdefault(3, 11))
print(my_dict.setdefault(7, 11))

# update method
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)
d1 = {1: 11, 2: 22}
d2 = {3: 33, 4: 44}
d1.update(d2)
print(d1)
# d3 = d1 + d2    ---unsupported operand type(s) for +: 'dict' and 'dict'

# delete in 3 ways
# 1 is using del keyword
# del d1[1]    # del dictionaryname[key]
#The main difference between pop() and popitem() is that the pop() element can remove an element with a specific key
# while in the case of popitem() we will delete the last entered element from the dictionary.
# d1.pop(1)
# print(d1)
# d1.popitem()
# print(d1)
 # 3rd way is clear() where as it gives empty dict
 #if you use del then entire dictionary will be deleted
print(d1)
d1.clear()
print(d1)
print(d2)
del d2
print(d2)    #name 'd2' is not defined


