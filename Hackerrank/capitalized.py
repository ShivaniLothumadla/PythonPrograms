# def solve(s):
#     for i in s.split():
#         s = s.replace(i, i.capitalize())
#     print(s)


# or

def solve(s):
    a = map(str.title, s.split())
    print(' '.join(a))
    # or
# def solve(s):
#     s = s.title()
#     print(s)
solve('hello world')

