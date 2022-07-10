# s = input().split()
# d1 = {}
# s1 = 0
# for i in s:
#     currentsum = sum(map(ord, i))
#     d1[i] = currentsum
# # totalsum = 0
# asciivalues = [d1[i] for i in s]
# av = ' '.join(str(asciivalues))

s = 'shivani ayan'
asky = ''
alist = [str(ord(i)) for i in s if i != ' ']
# print(alist)
# print(type(alist))
blist = str(' '.join(alist))
print(blist)
print(type(blist))
# print(atuple)
# m = map(ord, s)
# print(list(m))

# print(ord('A'), ord('Z'), ord('a'), ord('z'), ord(' '))