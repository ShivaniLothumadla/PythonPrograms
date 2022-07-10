lst  = [1, 2, 3, 4, 5]
#assignment
lst[0] = 0
print(lst)

#copying
# by using list()
lst2 = list(lst)
print(lst2)
# by using copy()
lst3 = lst.copy()
print(lst3)

# if u assign the list with assignment opeartor, the changes will be reflected on the new list also.
lst4 = lst
print(lst4)

lst[0] = 'apple'
print(lst)
print(lst2)
print(lst3)
print(lst4)
lst4[1] = 'banana'
print(lst)
print(lst4)
