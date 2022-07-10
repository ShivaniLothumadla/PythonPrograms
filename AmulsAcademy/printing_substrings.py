str = 'abcd'
for i in range(0, len(str)):
    for j in range(i+1, len(str)+1):
        print(str[i:j], end=' ')
    print()

# output :
# a ab abc abcd
# b bc bcd
# c cd
# d