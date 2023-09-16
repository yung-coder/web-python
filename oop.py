class Person:
    name = "Saksham"
    gender = "Male"
    worth = 90

    def info(self):
        print(f"{self.name} is a {self.gender}")


a = Person()
print(a.gender)
a.info()


# Constructor


class Car:
    def __init__(self, Name, Model):
        print(f"it is {Name} of Modal {Model}")


b = Car("Cruze", "2010")


# Decorartors


def greet(fx):
    def mfx():
        print("Yo")
        fx()
        print("Bye")

    return mfx


@greet
def hello():
    print("Lets go")


hello()


# Getters and Settters


class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    # Getter

    @property
    def ten_value(self):
        return 10 * self._value

    # Setter

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


obj = MyClass(10)
print(obj.ten_value)
obj.show()


# Inheritance


class Worker:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Id is {self.id} is {self.name}")


class Coder(Worker):
    def showLang(self):
        print("The Default language is Js")


c = Coder("Saksham" , 47)
c.show()
c.showLang()
