str = input("Please enter a string: ")
for i in range(len(str)):
    for j in range(i+1):
        print(str[j], end=' ')
    print()
