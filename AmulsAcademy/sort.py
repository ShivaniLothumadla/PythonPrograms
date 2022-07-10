'''
sort is a built in method for sorting and it is only applicable for lists.
syntax of sort: L.sort(key=None, reverse=False)
here L is the list on which we are performing the sort
sort is the method to sort the list
key is None as default and by passing any value we can change the sorting process
reverse is False as default and it means the sorting is in ascending order,where as reverse is true means the sorting is in descending order.
'''
lst = [2,4,3,1,6,9,5]
#ascending order
lst.sort()
print(lst)

#descending order
lst.sort(reverse=True)
print(lst)

#string sorting
#ascending order
lst2 = ['a', 'bb', 'dddd', 'eeeee', 'ccc']
lst2.sort()
print(lst2)

#desending order
lst2.sort(reverse=True)
print(lst2)

#sorting using key
#ascending order
lst3 = ['z', 'aa', 'yyy', 'bbb', 'xxxx', 'c']
lst3.sort(key=len)    # the key will convert into the length on the individual item like [1, 2, 3, 3, 4, 1] and now it actually sort like [1, 1, 2, 3, 3, 4] and the actual element can be shown as ['z', 'c', 'aa', 'yyy', 'bbb', 'xxxx']
print(lst3)
#descending order
lst3 = ['z', 'aa', 'yyy', 'bbb', 'xxxx', 'c']
lst3.sort(key=len, reverse=True)   #[1, 2, 3, 3, 4, 1] and then revesresort like [4, 3, 3, 2, 1, 1] and the output is ['xxxx', 'yyy', 'bbb', 'aa', 'z', 'c']
print(lst3)

#sorting on numbers using key
lst4 = [[2, 4], [6, 1], [3, 7], [9, 0]]
lst4.sort(key=len)
print(lst4)
lst4 = [[2, 4], [6, 1], [3, 7], [9, 0]]
def sortByDec(ele):
    return ele[1]
lst4.sort(key=sortByDec, reverse=True)
# lst4.sort(key=lambda x:x[1], reverse=True)
print(lst4)