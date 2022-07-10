# string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
#
# max_width = 4
# s = list(string)
# x = s[::4]
# print(x)
# for i in range(1, len(x)):
#     if x[i] in s:
#         k = s.index(x[i])
#         s.insert(k, '\n')
#     print(s)
# string = ''.join(s)
# print(string)
import textwrap

def wrap(string, max_width):
    # Text Wrap in Python - HackerRank Solution START
    return textwrap.fill(string, max_width)
    # Text Wrap in Python - HackerRank Solution END

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

