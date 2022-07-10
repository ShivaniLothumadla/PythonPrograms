s = input().split()
s1 = []
for i in range(len(s)-1):
    s1 += s[i][0].upper()+'.'
s1 += s[-1].title()
s1 = ''.join(s1)
print(s1)