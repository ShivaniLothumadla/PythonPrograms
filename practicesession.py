from random import random, shuffle

# def fun(x=random()):
#     print(x)
#
# fun()
# fun()
#
# fruit=['apple', 'banana', 'papaya', 'cherry']
# a = shuffle(fruit)
# random
# def fx(x):
#   x[0] = ['def']
#   x[1] = ['abc']
#   return id(x)
# a = ['abc', 'def']
# print(id(a) == fx(a))
# print(list(range(5)))

# l=list(range(1, 0, 0))
# for i in l:
#     print(i)
# def my_func(nums):
#   count = 0
#   for i, j in enumerate(nums):
#     if i > count:
#       return False
#     count = max(count, i + j)
#   return True
#
#
# if __name__ == "__main__":
#   print(my_func([3, 2, 1, 0, 4]))

# def my_func(st):
#   l1 = [ch for ch in st if ch.isalpha()]
#   return ''.join(l1.pop() if ch.isalpha() else ch for ch in st)
#
#
# st = 'ab-cd-ef'
# print(my_func(st))
# circle_areas = [3.54773, 5.57778, 4.00014, 59.24241, 34.01344, 32.01013]
#
# result = list(map(round, circle_areas, range(1,3)))
# print(result)

# class Person:
#   def __init__(self, id):
#     self.id = id
#
# sam = Person(100)
#
# sam.__dict__['age'] = 49
#
# print (sam.age + len(sam.__dict__))

x = "abcdef"
i = "a"
while i in x:
  x = x[1:]
  print(i, end = " ")