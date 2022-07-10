class A:
    __a = 10
    def sum(self):
        print(self.__a)
        print('Parent sum')
class B(A):
    def sum(self):
        print('Child sum')

    def sum1(self):
        super(B, self).sum()
obj = B()
print(obj.sum1())