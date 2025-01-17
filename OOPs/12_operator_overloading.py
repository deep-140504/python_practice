class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if(s1 > s2):
            return True
        else:
            return False
    
    def __str__(self):
        return f"marks: {self.m1} {self.m2}"

s1 = Student(1, 2)
s2 = Student(3, 4)

s3 = s1 + s2
print(s3.m1, s3.m2)

if(s1 > s2):
    print("s1 wins")
else:
    print("s2 wins")

print(s1)
print(s2)
print(s3)

# thing to remember over here is whenever we are performing any simple operations, we are calling the methods defined for the same
# e.g. print => __str__
# e.g. + => __add__
# e.g. - => __sub__
# e.g. * => __mul__
# e.g. / => __div__
# e.g. < => __lt__
# e.g. > => __gt__
# e.g. >= => __ge__
