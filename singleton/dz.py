"""!"""


class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

class MyClass(metaclass=Singleton):
    pass


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
obj_4 = MyClass()

print(obj_1 is obj_4)
