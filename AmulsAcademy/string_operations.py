'''
string is immutable
string has so many methods to perform on the string
'''
#1.capitalize is a method to change the first char of the string to uppercase if it is in lowercase otherwise it gives the same output
str = 'Hello welcome to python string operations or functions'
print(str.capitalize())
str = 'JOHNY JOHNY YES PAPA'
print(str.capitalize())

#2.count is a method to find out the number of occurances of the particular string if no matches then gives 0.
str = '''johny johny yes papa
eating sugar no papa
telling lies no papa
open your mouth hahaha'''
print(str.count('no'))
print(str.count('Papa'))

#3.endswith is gives true if the string endswith the given particular string, otherwise gives False
print(str.endswith('hahaha'))
print(str.endswith('johny'))

#4.find():is used to find the substring in the string and gives the index of the first occurance of the sub string though more than one substring present in the given string.
#if the substring is not present in the string then gives -1
print(str.find('no'))
print(str.find('papa'))
print(str.rfind('papa'))

#5.len():is used to count the number of elements in the string and the index starts with zero.
print(len(str))

#6.split():is used to split the given string into required string by passing the delemeter.
#bydefaullt delemeter is space.
print(str.split('papa'))

#7.upper():is used to return all the elements in uppercase.
print('hello shivani'.upper())

#8.lower():is used to return all the elements in lowercase.
print('HELLO SHIVANI'.lower())

#9.isupper():is used to check that all the elements are in uppercase or not.returns True if the string contains all uppercase chars,otherwise gives False
print('HELLO SHIVANI'.isupper())
print('hello shivani'.isupper())

#10.islower():is used to check that all the elements are in lowercase or not.returns True if the string contains all lowercase