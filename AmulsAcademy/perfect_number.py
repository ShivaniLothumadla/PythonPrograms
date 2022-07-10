# the sum of the positive divisors of the given number excluding the number is equals to the given number itself is called Perfect number.
# the half of the sum of positive divisors including given number is equals to the given number is called perfect number.
num = int(input('Please enter a number: '))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if num == sum:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")

