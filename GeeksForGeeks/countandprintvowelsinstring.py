# to print total vowel count from given string
# s = input()
# s = [i for i in s if i in 'AaEeIiOoUu']
# print(s)
# print(len(s))

# 2nd way
# s = input()
# vowels = 'aeiou'
# s = s.casefold()
# count = {}.fromkeys(vowels, 0)
# for c in s:
#     if c in count:
#         count[c] += 1
# print(count)

# third way
# s = input()
# vowels = 'aeiou'
# aflag = eflag = iflag = oflag = uflag = 0
# for i in s.casefold():
#     if i in vowels:
#         if i == 'a':
#             aflag += 1
#         elif i == 'e':
#             eflag += 1
#         elif i == 'i':
#             iflag += 1
#         elif i == 'o':
#             oflag += 1
#         elif i == 'u':
#             uflag += 1
# print('{} is having {} a\'s, {} e\'s, {} i\'s, {} o\'s and {} u\'s.'.format(s, aflag, eflag, iflag, oflag, uflag))

s = input().casefold()
vowels = 'aeiou'
count = {}.fromkeys(vowels, 0)
for i in s:
    if i in count:
        count[i] += 1
print(count)