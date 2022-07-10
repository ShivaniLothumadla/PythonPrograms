# armstrong number
# n = 153
# temp = n
# sum = 0
# while(n > 0):
#     rem = n % 10
#     sum = sum + rem * rem * rem
#     n = int(n / 10)
# if temp == sum:
#     print(f'{sum} is a armstrong number')
# else:
#     print(f'{temp} and {sum} are not same.')

# How to count the occurrences of a particular element in the list?
# from collections import Counter
# weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
# count = Counter(weekdays)
# print(count.most_common(len(weekdays)))

# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]
#
# names2[0] = 'Alice'
# names3[1] = 'Bob'
#
# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
#     if ls[1] == 'Bob':
#         sum += 10
#
# print(sum)

# list1 = [1, 3, 2]
# print(list1 * 2)

# print(list('hello'))

# average of numbers in a list in Python
# lisst = [20, 45, 53, 84, 90]
# print(sum(lisst) // len(lisst))
# s = 0
# for i in lisst:
#     s = s + i
# print(s // len(lisst))

# reverse number
# num = int(input())
# temp = num
# rev = 0
# while(num > 0):
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# if temp == rev:
#     print(f'the actual num {temp} and the reverse num {rev} is same')
# else:
#     print(f'the actual num {temp} and the reverse num {rev} are not same')

# # sum of the digits of a number
# num = int(input())
# temp = num
# sum = 0
# while(num > 0):
#     rem = num % 10
#     sum = sum + rem
#     num = num // 10
# print(f'sum of the given number {temp} is {sum}')

# # Check if a Number is a Palindrome or not
# num = int(input())
# temp = num
# sum = 0
# while(num > 0):
#     rem = num % 10
#     sum = sum * 10 + rem
#     num = num // 10
# if temp == sum:
#     print(f'{temp} is palindrome')
# else:
#     print(f'{temp} is not palindrome')

# # Count the Number of Digits in a Number
# num = int(input())
# count = 0
# while (num > 0):
#     count = count + 1
#     num = num // 10
# print(count)

# #  Print Table of a Given Number
# num = int(input())
# for i in range(1, 11):
#     print(num, 'X', i, '=', num * i)

# #  year is a Leap Year or not
# num = int(input())
# if num % 4 == 0 and num % 100 != 0:
#     print(f'{num} is Leap Year')
# elif num % 100 == 0 and num % 400 == 0:
#     print(f'{num} is a Leap Year')
# else:
#     print(f'{num} is not Leap year')

# # Prime number or not:A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself.
# num = int(input())
# count = 0
# for i in range(2, (num // 2)+1):
#     if (num % i) == 0:
#         count = count + 1
# if count <= 0:
#     print(f'{num} is prime number')
# else:
#     print(f'{num} is not prime')

# # Number is an Armstrong Number
# num = int(input())
# a = list(map(int, str(num)))
# b = list(map(lambda x: x*x*x, a))
# if sum(b) == num:
#     print(f'{num} is armstrong')
# else:
#     print(f'{num} is not armstrong')

# # perfect number
# def perfect_num(i):
#     num = i
#     sum = 0
#     for k in range(1, num):
#         if num % k == 0:
#             sum = sum + k
#     if num == sum:
#         return sum
#     # else:
#     #     print(f'{num} is not perfect number')
#
#
# def no_of_perfect_num(num1, num2):
#     num = []
#     for i in range(num1, num2 + 1):
#         num.append(perfect_num(i)) if perfect_num(i) != None else num
#     return num
#
#
# print(no_of_perfect_num(1, 100))

# # strong number:A number can be said as a strong number when the sum of the factorial of the individual digits is equal to the number
#
# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fact(num-1)
# num = int(input())
# temp = num
# add = 0
# while num > 0:
#     add = add + fact(num % 10)
#     num = num // 10
# if add == temp:
#     print(f'{temp} is a strong number.')
# else:
#     print(f'{temp} is not a strong number.')

# # Second Largest Number in a List?
# a = [1, 20, 23, 34, 34, 55, 12]
# ss = set(sorted(a))
# ss.remove(max(a))
# print(max(ss))

#  Swap the First and Last Value of a List
# a = [1, 2, 3, 4, 5, 6, 4]
# a[0], a[-1] = a[-1], a[0]
# # temp = a[0]
# # a[0] = a[-1]
# # a[-1] = temp
# print(a)


# # string Palindrome
# s = input()
# mid = len(s) // 2
# first_list = s[:mid]
# if len(s) % 2 == 0:
#     second_list = s[mid:]
# else:
#     second_list = s[mid+1:]
# if first_list == second_list[::-1]:
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} is not palindrome')
#
# # or
# if s == s[::-1]:
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} is not a palindrome')

# #Count the Number of Vowels in a String
# s= input()
# count = 0
# vowels='aeiou'
# s= s.casefold()
# dit = {}.fromkeys(vowels, 0)
# for i in s:
#     if i in vowels:
#        dit[i] += 1
# print(dit)from random import random
# def fun(x=random()):
#  print(x)
#
# fun()
# fun()


#Common Letters in Two Input Strings?
s1 = input()
s2 = input()
s3 = list(set(s1) & set(s2))
for i in s3:
    print(i)
