# num = int(input())
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
# print(fact)

# or
def addsum(f):
    def innerfunc(n):
        if n < 0:
            print('please enter the positive number.')
        else:
            return f(n)
    return innerfunc

@addsum
def fact(num):

    if num == 0 or num == 1:
        return 1
    else:
        return (num * fact(num-1))

print(fact(5))