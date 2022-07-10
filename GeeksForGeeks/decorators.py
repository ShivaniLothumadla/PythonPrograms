# from collections import deque
#
# def lowercase_decorator(func):
#     def wrapper():
#         func()
#         make_lowercase = func().lower()
#         return make_lowercase
#     return wrapper
# def split_string(func):
#     def wrapper():
#         func()
#         split_string = func().split()
#         return split_string
#     return wrapper
# @split_string
# @lowercase_decorator
# def test_func():
#     return 'MOTHER OF DRAGONS'
# print(test_func())
def extra_add(f):
    def newfunc(x,y):
        if x % 2 == 0 and y % 2 == 0:
            f(x,y)
        elif x > y:
            f(x, y)
        elif x < y:
            print('first number should be greater.')
        else:
            print("Please enter even values.")
    return newfunc


@extra_add
def add(a, b):
    print(a + b)
add(6,6)

@extra_add
def sub(a,b):
    print(a - b)
sub(6,8)
