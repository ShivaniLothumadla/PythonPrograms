x = int(input())
y = int(input())
z = int(input())
n = int(input())
i = [i for i in range(x+1)]
j = [j for j in range(y+1)]
k = [k for k in range(z+1)]
list = []
for a in i:
    for b in j:
        for c in k:
            if a + b + c != n:
                l = [a, b, c]
                list.append(l)
print(list)


