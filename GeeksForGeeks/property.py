# class student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#     @property
#     def msg(self):
#         return self.name + " got a grade " + self.grade
#
#     @msg.setter
#     def msg(self, msg):
#         sent = msg.split()
#         self.name = sent[0]
#         self.grade = sent[-1]
#
#
# a = student('shivani', 'A')
# print("Name:", a.name)
# print("Grade:", a.grade)
# print("Msg:", a.msg)
# a.name = 'Ragini'
# a.grade = 'A+'
# print("Name:", a.name)
# print("Grade:", a.grade)
# print("Msg:", a.msg)
# a.msg = 'Nani got a grade A'
# print("Name:", a.name)
# print("Grade:", a.grade)
# print("Msg:", a.msg)

class student:

    __i = 5
    def __init__(self, marks):
        self.__marks = marks

    @classmethod
    def college_name(cls):
        return 'JNTU'

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        self.__marks = value

    def percentage(self):
        print((self.__marks / 600) * 100)

    @staticmethod
    def stat_method():
        print('stats method')

a = student(600)
a.percentage()
print(a.marks)
a.marks = 400
a.percentage()
print(a.marks)
print(a.college_name())
print(student.college_name())
a.stat_method()
student.stat_method()
