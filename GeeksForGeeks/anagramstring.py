str1 = 'state'
str2 = 'taste'
# str3 = ''.join(sorted(str1))
# str4 = ''.join(sorted(str2))
# if str3 == str4:
#     print(f'{str1} and {str2} are anagram strings')
# else:
#     print(f'{str1} and {str2} are not anagram strings')
if len(str1) == len(str2):
    for i in str1:
        for j in range(len(str2)):
            if i in str2:
                index = str2.find(i)
                str2 = str2[:index] + '*' + str2[index+1:]
else:
    print(f'{str1} and {str2} are not arigami strings')
# print(str3)
# for i in range(len(str1)):
#     for j in range(len(str2)):
#         if str1[i] == str2[j]:
#             str3 = str3.append(str2[j])
#             break
# print(str2)

# sorted
