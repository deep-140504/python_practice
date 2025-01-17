class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature1 working")
    def feature2(self):
        print("feature2 working")


class B:
    def __init__(self):
        # super().__init__() # this
        # super.__init__() not this
        print("in B init")
    def feature3(self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")

class C(B, A):
    def __init__(self):
        super().__init__() # the input will be biased towards, the class defined in inheriting from left to right
        print("in c init")
    def feat(self):
        super().feature1()

# sub calss can acesse all the features of super class but,
# super class can not access any feature of sub class

a1 = C()
a1.feat()
# so here, even if you have object of B, it will call the constructor of A (till now constructor of B is not created)

# so the flow, was going inside the constructor of A because there was no constructor inside of the B

#by default, the flow will only go inside the constructor of B, but, if you want to exeute both of the constructors, then it can be done by using the super keyword