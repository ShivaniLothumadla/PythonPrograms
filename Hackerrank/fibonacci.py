"""Python's reduce() is a function that implements a mathematical technique called folding or reduction.
#  reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value."""
# from functools import reduce
# lines = [25, 26.5, 28]
# x = 0
# # list comprehesion
#
# # lambda expression
# s = reduce(lambda a, b: a+b, lines)
# print((s))
# # s = [x for x in lines]
# # for i in lines:
# #     x = x + i
# # print(x)
# # newlist = [i for i in lines]
# # print(newlist)

# Python program to find the sum of
# all elements of the list

# from functools import reduce
#
# # List of some fibonacci numbers
# fiboList = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# print("List of fibonacci numbers :", fiboList)
#
# # using Lambda function to
# # add elements of fibonacci list
# listSum = reduce(lambda a, b: a+b, fiboList)
# print("The sum of all elements is ", listSum)

a = 0
b = 1
count = 0
# for i in range(10):
#     print(a, end=' ')
#     temp = a + b
#     a = b
#     b = temp

while(count<10):
    print(a, end=' ')
    temp = a + b
    a = b
    b = temp
    count += 1
