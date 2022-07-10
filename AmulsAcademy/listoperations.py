'''
List characteristics:
1.List is mutable
2.List is linear data type
3.List accepts mixed data type
4.List has a variable length
5.List has zero based indexed
-------------------------------
List operations:
1.replace
2.insert
3.append
4.sort
5.delete
6.reverse
'''
list1 = [10, 20, 30, 40]
print(list1)

#replace
list1[1] = 50
print(list1)

#insert----adding an item at perticular position
list1.insert(1, 60)
print(list1)

#append---adding an item at the end.
list1.append(70)
print(list1)

#sort --- sorting the list and updating the same list
list1.sort()
print(list1)

#delete --- deleting an element based on the index
del list1[2]
print(list1)

#reverse ---- reversing the list of elements and giving the elements in the same list
list1.reverse()
print(list1)

