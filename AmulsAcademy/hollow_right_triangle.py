# n = int(input("enter a number"))
# for i in range(1, n):
#     for j in range(1, i+1):
#         if j == 1 or i == (n-1) or i == j:
#             print('*', end=' ')
#         else:
#             print(end='  ')
#     print()

# output :
# enter a number5
# *
# * *
# *   *
# * * * *

num = int(input("enter a number: "))
for i in range(num):
    for j in range(num):
        if i == 0 or j == (num-1) or i == j:
            print('*', end=' ')
        else:
            print(end='  ')
    print()

# output:
# enter a number: 5
# * * * * *
#   *     *
#     *   *
#       * *
#         *