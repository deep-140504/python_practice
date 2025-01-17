# in oops there are two types of variable, 
# 1: instance variable
# 2: class(static) variable

class Car():
    # this variable resides inside of the class namespace, as it is a class variable
    wheels = 4
    def __init__(self):
        # these variables are part of the instance namespace
        self.mil = 10
        self.comp = "BMW"
    
c1 = Car()
c2 = Car()

# here if i change the class variables, it will affect all the variables of instances
Car.wheels = 5
# here the change in the class variables take place

# c1.wheels = 6 this can also be done considering the fact that it will only affect the variable of the object, c1


print(c1.mil, c1.comp, c1.wheels)
print(c2.mil, c2.comp, c2.wheels)

# in instance variable what happens is, on changing attribute of one object, another attribute of an object is not affected, but the thing is, same does not go for the static variables

# in this case, such static variable is, wheels, which is static and common for every car


# so what happens is, in the memory, there exists various namespace, namespace is an area where you create ans store object/variable
# so there are total two namespaces, 
# 1. class namespace
# 2. object/ instance namespace

