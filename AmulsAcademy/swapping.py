# 3 ways of swapping
# 1st is using third variable
a = int(input('Please enter a number: '))
b = int(input('Please enter a number: '))
print(a, b)
temp = a
a = b
b = temp
print(a, b)

# 2nd way is not using third variable
a = int(input('Please enter a number: '))
b = int(input('Please enter a number: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

# 3rd way is not using third variable
a = int(input('Please enter a number: '))
b = int(input('Please enter a number: '))
print(a, b)
a, b = b, a
print(a, b)
