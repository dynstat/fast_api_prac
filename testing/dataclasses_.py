from dataclasses import dataclass


class Person_old:
    def __init__(self, name="Joe", age=30, height=1.85, email="joe@dataquest.io"):
        self.name = name
        self.age = age
        self.height = height
        self.email = email


@dataclass
class Person:
    name: str = "Joe"
    age: int = 30
    height: float = 1.85
    email: str = "joe@dataquest.io"


p = Person()
p_old = Person_old()
print("debug")
