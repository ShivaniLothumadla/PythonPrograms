str = input()
n = len(str)
listt = []
for i in str:
    if i in listt:
        listt.remove(i)
    else:
        listt.append(i)
if n % 2 == 0 and len(listt) == 0 or n % 2 == 1 and len(listt) == 1:
    print(True)
else:
    print(False)
