s='shivani'
c1 = 'i'
c2 = 'a'
a = map(lambda x: x if (x!=c1 and x!=c2) else c1 if(x==c2) else c2,s)
print((''.join(a)))