# fnding runner
n = int(input())
arr = map(int, input().split())
l = set(arr)
maxi = max(l)
l.remove(maxi)
runner = max(l)
print(runner)