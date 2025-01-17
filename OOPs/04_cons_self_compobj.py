class Computer:
    def __init__(self):
        self.name = "abc"
        self.age = 20

    def update(self):
        # here the self is directing towards the instance of the class, through which the method is called
        self.age = 30
    
    def __eq__(self, other):
        # this takes two arguments, (who is calling, whom to compare)
        return self.age == other.age

c1 = Computer()
c2 = Computer()
# this c1 is refering to an object created using Computer class

# in system, the objects being created are stored inside of the heal memory

# the object being created has its own ids, which can be accessed using id(object)

print(id(c1))
# so, every time you create and object it is allocated to new spaces
# size being ocuupied by an object is determined by the no of variables, and the size allocation to an object is done by the constructor
print(c1.age)
c1.update()
print(c1.name)
print(c1.age)

print(c1 == c2)
