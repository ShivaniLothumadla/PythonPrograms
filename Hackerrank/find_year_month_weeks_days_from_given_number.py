n = int(input('enter days: '))
year = n // 365
n = n % 365
months = n // 30
n = n % 30
weeks = n // 7
n = n % 7
print('Years:', year, 'Months:', months, 'Weeks:', weeks, 'Days:', n)