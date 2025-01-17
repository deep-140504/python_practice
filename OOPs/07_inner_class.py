class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(f'{self.name} {self.rollno}')
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = "hp"
            self.cpu = "i3"
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)
s1 = Student("a", 1)
s2 = Student("b", 2)
s1.show()

lap1 = s1.lap
lap2 = s2.lap


# you can create object of inner class inside the outer class or 
# you can create object of inner class outised the outer class provided you use outer class name to call it
lap3 = Student.laptop()
lap3.show()