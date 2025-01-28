class A:
    a = 1
    b = "hello"

    def f(self):
        return 42
    
def main():
    print(f'{type(42)=}')
    print(f'{type(str)=}')
    print(f'{type(list)=}')
    print(f'{type(A)=}')
    print()
    a = A()
    print(f'{type(a) = }')
    print(f'{type(A) = }')
    print()
    b = B()
    print(f'{type(b)=}')
    print(f'{type(B)=}')

class MyMetaclass(type):
    pass
class B(metaclass = MyMetaclass):
    pass
if __name__ == "__main__":
    main()

# in python 3 there is no difference between type and a class
# in concept type and classes are identical
# class is a syntaxtical sugar, which is the specific way of calling the type constructor
