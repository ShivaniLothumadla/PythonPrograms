string = "1abc2x300000yz67-20sdf"
lst = []
for i in range(len(string)):
    while string[i].isdigit():
        lst.append(string[i])
        i += 1

print(lst)
