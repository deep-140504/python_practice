from abc import abstractmethod


class CompleteMeta(type):
    """
    A metaclass implementing as many dunder methods as possible for demonstration.
    """
    # Called before the class is created to prepare the namespace
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(f"__prepare__ called: Preparing namespace for class {name}")
        print(f"Arguments: {kwargs}")
        return {"prepared_attribute": "Added during __prepare__"}

    # Called to create the class
    def __new__(cls, name, bases, class_dict, **kwargs):
        print(f"__new__ called: Creating class {name}")
        print(f"Class dictionary before creation: {class_dict}")
        
        # Detect abstract methods
        abstract_methods = {k for k, v in class_dict.items() if getattr(v, "__isabstractmethod__", False)}
        class_dict["__isabstract__"] = bool(abstract_methods)  # Mark if class is abstract
        
        if abstract_methods:
            print(f"Abstract methods detected in {name}: {abstract_methods}")

        # Add a custom attribute
        class_dict["added_in_new"] = "Added during __new__"
        
        # Create the class
        return super().__new__(cls, name, bases, class_dict)

    # Called to initialize the class object
    def __init__(cls, name, bases, class_dict, **kwargs):
        print(f"__init__ called: Initializing class {name}")
        cls.init_attribute = "Added during __init__"
        super().__init__(name, bases, class_dict)

    # Called when the class is called (e.g., for instance creation)
    def __call__(cls, *args, **kwargs):
        print(f"__call__ called: Creating an instance of {cls.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        
        if getattr(cls, "__isabstract__", False):
            raise TypeError(f"Cannot instantiate abstract class {cls.__name__} with abstract methods.")
        
        # Create an instance
        instance = super().__call__(*args, **kwargs)
        return instance

    # Attribute management
    def __getattr__(cls, name):
        print(f"__getattr__ called: Accessing attribute {name} on {cls}")
        return f"Dynamic value for {name}"

    def __setattr__(cls, name, value):
        print(f"__setattr__ called: Setting {name} = {value} on {cls}")
        super().__setattr__(name, value)

    def __delattr__(cls, name):
        print(f"__delattr__ called: Deleting attribute {name} from {cls}")
        super().__delattr__(name)

    # Container methods for class attributes
    def __contains__(cls, item):
        print(f"__contains__ called: Checking if {item} is in {cls.__name__}")
        return item in cls.__dict__

    def __len__(cls):
        print(f"__len__ called: Returning the number of attributes in {cls.__name__}")
        return len(cls.__dict__)

    def __iter__(cls):
        print(f"__iter__ called: Iterating over attributes of {cls.__name__}")
        return iter(cls.__dict__.items())

    # String and representation
    def __str__(cls):
        return f"<Class {cls.__name__} (custom str)>"

    def __repr__(cls):
        return f"<CompleteMeta Class: {cls.__name__}>"

    # Rich comparison operators
    def __eq__(cls, other):
        print(f"__eq__ called: Comparing {cls} with {other}")
        return id(cls) == id(other)

    def __ne__(cls, other):
        print(f"__ne__ called: Comparing {cls} with {other}")
        return not (cls == other)

    def __lt__(cls, other):
        print(f"__lt__ called: Comparing {cls} < {other}")
        return cls.__name__ < other.__name__

    def __le__(cls, other):
        print(f"__le__ called: Comparing {cls} <= {other}")
        return cls.__name__ <= other.__name__

    def __gt__(cls, other):
        print(f"__gt__ called: Comparing {cls} > {other}")
        return cls.__name__ > other.__name__

    def __ge__(cls, other):
        print(f"__ge__ called: Comparing {cls} >= {other}")
        return cls.__name__ >= other.__name__

    # Arithmetic operations (custom behaviors)
    def __add__(cls, other):
        print(f"__add__ called: Adding {cls} and {other}")
        return f"{cls.__name__} + {other.__name__}"

    def __sub__(cls, other):
        print(f"__sub__ called: Subtracting {cls} and {other}")
        return f"{cls.__name__} - {other.__name__}"

    def __mul__(cls, other):
        print(f"__mul__ called: Multiplying {cls} and {other}")
        return f"{cls.__name__} * {other.__name__}"

    def __hash__(cls):
        print(f"__hash__ called: Hashing {cls.__name__}")
        return hash(cls.__name__)


# Example class using the CompleteMeta metaclass
class MyAbstractBase(metaclass=CompleteMeta):
    @abstractmethod
    def abstract_method(self):
        pass


class MyClass(MyAbstractBase):
    def abstract_method(self):
        print("Implementing abstract_method.")

    def __init__(self, value):
        print(f"MyClass instance initialized with value: {value}")
        self.value = value


# Testing the Metaclass
print("== Class Creation ==")
print(f"MyAbstractBase.__isabstract__: {MyAbstractBase.__isabstract__}")
print(f"MyClass.__isabstract__: {MyClass.__isabstract__}")

print("\n== Abstract Class Check ==")
try:
    instance = MyAbstractBase()
except TypeError as e:
    print(e)

print("\n== Instance Creation ==")
instance = MyClass("Hello")
print(f"Instance value: {instance.value}")

print("\n== Attribute Management ==")
print(f"MyClass.init_attribute: {MyClass.init_attribute}")
print(f"MyClass.added_in_new: {MyClass.added_in_new}")
MyClass.new_attribute = "Dynamic attribute"
print(f"MyClass.new_attribute: {MyClass.new_attribute}")

print("\n== Container Methods ==")
print(f"'added_in_new' in MyClass: {'added_in_new' in MyClass}")
print(f"len(MyClass): {len(MyClass)}")
print("Iterating over MyClass attributes:")
for name, value in MyClass:
    print(f"{name}: {value}")

print("\n== String and Representation ==")
print(str(MyClass))
print(repr(MyClass))

print("\n== Comparison ==")
class AnotherClass(metaclass=CompleteMeta):
    pass

print(f"MyClass == AnotherClass: {MyClass == AnotherClass}")
print(f"MyClass < AnotherClass: {MyClass < AnotherClass}")

print("\n== Arithmetic Operations ==")
print(MyClass + AnotherClass)
print(MyClass * AnotherClass)
