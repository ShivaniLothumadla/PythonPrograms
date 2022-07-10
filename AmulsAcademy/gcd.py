def computegcd(a, b):
    if b == 0:
        return a
    else:
        return computegcd(b, a % b)


n1 = int(input())
n2 = int(input())
print(computegcd(n1, n2))
