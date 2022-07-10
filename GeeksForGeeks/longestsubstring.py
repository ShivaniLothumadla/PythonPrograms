# incomplete
s1 = 'shivani geeksforgeeks'
s2 = 'shivani geek'
sa = input()
sb, sb1 = map(str, s2.split())
print(sa)
print(sb)
alow = 0
blow = map(str, s2.split())
print(''.join(blow))
count = 0
for i in range(len(s1)-len(s2)+1):
    if s1[i:i+len(s2)] == s2:
        count = 1
if count == 1:
    print(f'{s1} is having {s2}')
else:
    print(f'{s1} is not having {s2}')