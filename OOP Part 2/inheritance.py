## Simple example of Class Inheritance

class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animals says {sound}")

class Dog(Animal):
    pass

# blue = Dog()
# blue.make_sound("woof")

######       Getter and Setter Properties  #################

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    # def get_age(self):
    #     return self._age ## signifying that this variable should be respected
    #
    # def set_age(self, value):
    #     if value >= 0:
    #         self._age = value
    #     else:
    #         raise ValueError("Age can't be negative")
    #     return self._age

    @property  ### GETTER METHOD PROPERTY
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative")

John = Human("John", "Rockefeller", 99)
# print(John.get_age())
# print(John.set_age(100))

print(John.age)
John.age = 100
print(John.age)
