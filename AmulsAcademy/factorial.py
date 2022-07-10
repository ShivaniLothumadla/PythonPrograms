# 1st way using inbuilt method
# import math
# num = int(input("Please enter a number: "))
# result = math.factorial(num)
# print("Factorial of", num, "is", result)

# # 2nd way using recursive function
# def fact(x):
#     if x == 0:
#         return 1
#     else:
#         return x * fact(x-1)
#
# n = int(input("please enter a number: "))
# result = fact(n)
# print(result)

# 3rd way using loops
num = int(input("Please enter a number: "))
result = 1
# using for loop
# for i in range(num, 0, -1):
#     result = result * i
# print("The factorial of", num, "is", result)
# using while loop
# while num != 0:
#     result = result * num
#     num = num - 1
# print("Factorial of", num, "is", result)


