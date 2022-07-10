year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('a leap year')
else:
    print('not a leap year')


def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))


def is_leap(year):
    leap = False
    if year % 100 == 0 and year % 400 == 0:   # century year
        leap = True
    elif year % 4 == 0 and year % 100 != 0:    # normal year
        leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))