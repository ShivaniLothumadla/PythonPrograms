# file = open('C:\Shivani\demofile.txt', 'w')
# file.write("This is my first line of code \n")
# file.write("This is my second line of code \n")
# file.close()


# file = open('C:\Shivani\demofile.txt', 'r')
# # print(file.read(10))
# # print(file.read())
# # print(file.readlines()) #array format
# print(file.readline())
# file.close()

# file = open('C:\Shivani\demofile.txt', 'a')
# file.write("This is my third line \n")
# file.close()

# file = open('C:\Shivani\demofile.txt', 'r')
# for i in file:
#     print(i)
# file.close()

a, b = 10, 20
class A:
    a, b = 3,4

    def add(self, a, b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a'] + globals()['b'])
obj = A()
obj.add(100, 200)


