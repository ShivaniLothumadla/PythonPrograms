from collections import Counter
s1 = 'shivani lothumadla ayansh goud lothumadla srinivas lothumadla lavanya sindoora tharun lothumadla shivani ayan ayan ayan'
s = s1.split()

print(Counter(s).most_common(1))
print(Counter(s).most_common(2))