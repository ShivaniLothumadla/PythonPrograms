#match: searches beginning of the string,if found gives the starting and ending index.to get the pattern use var.group(0)
#search: searches entire string, if found gives the starting and ending index.Gives only one occurance.to get the pattern use var.group(0)
#findall:searches entire string,if found gives direct list and it gives all occurances of the pattern.
import re
line = 'pet: cat i love cats pet:cow i love cows'
#match
var = re.match(r'pet:\w\w\w', line)
print(var)
# print(var.group(0))
#search
var = re.search(r'pet:\w\w\w', line)
print(var.group(0))
#findall
var = re.findall(r'pet:\w\w\w', line)
print(var)
# split
var = re.split(r'pet:\w\w\w', line)
print(var)
#replace
var = re.sub(r'pet:\w\w\w', 'replaced', line)
print(var)