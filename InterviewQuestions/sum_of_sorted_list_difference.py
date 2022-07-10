a = [5, 1, 3, 7, 3]
b = sorted(a)
diff = []
for i in range(len(b)):
    if i == len(b)-1:
        break
    else:
        diff.append(abs(b[i] - b[i + 1]))
print(diff)
diff = sum(diff)
print(diff)