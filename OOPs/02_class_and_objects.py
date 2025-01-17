# till now we have interacted with inbuilt datatypes class and objects can be used to create the custom dataypes, having different behaviour and functionalities

class Computer:
    #here we can put two things inside of the class
    # 1. variables also known as attributes
    # 2. methods(functions defined inside of the class) also known as behaviour
    def config(self):
        print("hi this is an i3 machine with 16 gb ram")

com1 = Computer()
# this is a general syntax of defining a object of a class

print(type(com1))

com1.config()
Computer.config(com1)
# this both gives the same output the thing here to notice is that the object is passes as an argument, as the method being called here is not a static, it depends on the object, on whom, it is being called on

# Computer.config() this gives an error because the method defined over here is not staticmethod, classmethod or a dunder method

