import re
s = 'Hello i am shivani https://www.google.com welcome to the url testing'
a = re.search(r'http[s]?://.+\..+$', s)
print(a)

