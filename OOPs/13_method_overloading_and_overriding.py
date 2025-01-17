# there is no concept of method overloading in python
# so we can not create two method with the same name, and different/ same parameters inside of the same class
# lets say there is a method with same name and same parameter in the parent class, then this called as the method overriding

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self, a, b): # so this thing will work for only two parameters, to avoid creating another method accepting more number of argumnets, *args and **kwargs are used
        s = a + b
        return s

s1 = Student(1, 2)
s2 = Student(3, 4)
print(s1.sum(5, 6)) 