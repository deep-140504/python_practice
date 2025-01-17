from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod # using this decorator mention that this method is an abstract method
    def process(self):
        # only declaration, but not any defination so such method is called an abstract method
        # and the class having abstract method is called an abstract class
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

# the thing is that we are able to access this object, because this is not an abstract class
# com = Computer()
# after mentioning the decorator, it is not possible to instantiate the object of the class Computer
#com.process()


#without defining the abstract method of the parent class, it will give an error
# it reuires implementing all the abstract methods present in the child class
com1 = Laptop()
com1.process()

