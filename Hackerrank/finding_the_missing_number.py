lt = [1, 2, 4, 3, 6, 7, 9, 8]
max_n = max(lt)
sum1 = (max_n * (max_n + 1)) // 2
sum2 = sum(lt)
print('The missing number is:', sum1 - sum2)
