str = input()
mid = int(len(str) / 2)
final_str = str[:mid] + str[mid:].upper()
print(final_str)