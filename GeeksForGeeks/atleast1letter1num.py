# s = input()
# lflag = False
# nflag = False
# for i in range(len(s)):
#     if s[i].isalpha():
#         lflag = True
#     elif s[i].isdigit():
#         nflag = True
# if lflag and nflag:
#     print(f'{s} is having atleast one letter and one number.')
# else:
#     print(f'{s} is not having atleast one letter and one number.')
s = input()
dflag = lflag = uflag = 0
for i in range(len(s)):
    if s[i].isdigit():
        dflag += 1
    elif s[i].islower():
        lflag += 1
    elif s[i].isupper():
        uflag += 1
if dflag >= 0 and lflag >= 0 and uflag >= 0:
    print('{} is having {} digits, {} lowercase letters and {} uppercase letters.'.format(s, dflag, lflag, uflag))
else:
    print('In {0} we have {1} number of digits, {2} number of lowercase letters and {3} number of uppercase letters'.format(s, dflag, lflag, uflag))


