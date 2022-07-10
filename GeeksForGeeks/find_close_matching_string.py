from difflib import get_close_matches
l = input().split()
word = input()
close_matches = get_close_matches(word, l)
print(close_matches)
