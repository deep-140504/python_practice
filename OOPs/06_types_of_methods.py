# there are total three types of methods:
# 1. Instance methods
# 2. Class methods
# 3. Static methods

# the thing here to notice is that in variables, class variables and static variables both are the same thing, but in methods, both are different

class Student:
    school = "xyz"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # below 3 methods are instance methods
    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3
        
    def get_m1(self):
        return self.m1
    def set_m1(self, value):
        self.m1 = value

    # the thing here to notice over here is, while accessing the class variables, or static variables, cls is passed as an argument 
    @classmethod
    def info(cls):
        return cls.school
    # as long as there is @classmethod, defined above the info() method, u can pass self or cls, does not matter, but to avoid confusion, convention must be followed
    # only way of manipulating instance variables, through class method is that, passing object, no other way, no need to do so, just for information

    # when it is required to do something without affecting the class variables or instance variables, then it is good to go with the staticmethod

    @staticmethod
    def stInfo():
        print("this is a student class, inside the abc module")

s1 = Student(1, 2, 3)
s2 = Student(3, 4, 5)

print(s1.average())
print(s2.average())

# in insatnce methods, there are two different types, one is accessors method and the another one is mutators

# print(s1.info())
# above thing works but is not a good practice, it is good to use, name of the class, in this case, so it will go like:

# print(Student.info())
# before applying the @classmethod decorator, it will give an error, since we are calling the function with the name of the class, so it is required to specify so

print(Student.info())
print(s1.get_m1())




Student.stInfo()



# ----------------------------------------------------------------------------------------
# thing to take into consideration here is that, a method is made class method, 
# (1) it is being accessed using the name of the class
# (2) it is accessing the class/static variables