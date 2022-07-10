# def solve (N, ch):
#     # Write your code here
#     l = ''.join(ch)
#     return l
#
# N = int(input())
# ch = input().split()
#
# out_ = solve(N, ch)
# print (out_)

# // Online Java Compiler
# // Use this editor to write, compile and run your Java code online
#
# var xyFile:File = File.createTempFile();
# if (xyFile.isDirectory() == true)
# xyFile.deleteDirectory(true)
# else
# xyFile.deleteFile()

a = [1, 3, 16, 14, 20, 10, 26]
even, odd = sorted([i for i in a if i % 2 == 0], reverse=True), [i for i in a if i % 2 != 0]
even_5, even_not5 = [i for i in even if i % 5 == 0], [i for i in even if i % 5 != 0]
f = even_5 + even_not5 + odd
print(f)
for i in f:
    k = ''.join(str(i))
    print(k, end=' ')
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         even.append(a[i])
#     else:
#         odd.append(a[i])
# even = sorted(even, reverse=True)
# print(even)
# print(odd)

# for i in range(len(even)):
#     if even[i] % 5 == 0:
#         even_final.append(even[i])
#     else:
#         even_final2.append(even[i])
# print(even_final)
# print(even_final2)
# print(even)
# f = []
#
# fl = even_final + even_final2 + odd
# for i in range(len(fl)):
#     f.append(fl[i])
# print(f)