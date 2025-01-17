# till now we have interacted with inbuilt datatypes class and objects can be used to create the custom dataypes, having different behaviour and functionalities

class Computer:
    def __init__(self, cpu, ram):
        # __init__ method runs for every time an object has been instantiated
        self.cpu = cpu
        self.ram = ram
        print("in init")

    def config(self):
        print(self.cpu, self.ram)


com1 = Computer("i5", 16)

com1.config()