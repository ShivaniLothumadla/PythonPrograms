num = int(input("please enter a number: "))
first, second = 0, 1
for i in range(num):
    print(first, end=' ')
    temp = first
    first = second
    second = temp + second
