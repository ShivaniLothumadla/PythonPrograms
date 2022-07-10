# rows = int(input('Please enter a number: '))
# for row in range(1, rows+1):
#     for col in range(1, 2 * rows):
#         if row == rows or row + col == rows+1 or col - row == rows-1:
#             print("*", end=' ')
#         else:
#             print(end='  ')
#     print()

# output:
# Please enter a number: 4
#       *
#     *   *
#   *       *
# * * * * * * *

rows = int(input('Please enter a number: '))
for i in range(1, rows+1):
    for j in range(1, 2 * rows):
        if i + j == rows + 1 or j - i == rows - 1:
            print("*", end=' ')
        elif i == rows and j % 2 != 0:
            print('*', end=' ')
        else:
            print(end='  ')
    print()

# output :
# Please enter a number: 4
#       *
#     *   *
#   *       *
# *   *   *   *
