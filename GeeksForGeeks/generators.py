def seequence():
    num = 0
    while num < 10:
        yield num
        num += 1

for i in seequence():
    print(i, end=",")