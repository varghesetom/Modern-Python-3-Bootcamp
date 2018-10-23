''' Class Attributes

We can also define attributes directly on a class that
are shared by all instances of a class and the class itself.'''


class Pet:
    allowed = ("cat", "dog", "lizard", "hamster")

    def __init__(self, kind, name):
        if kind not in Pet.allowed:
            raise ValueError(f"You can't have a {kind} as a pet here!")

        self.kind = kind
        self.name = name


Chip = Pet("cat", "Chip")

print(Chip.kind)

# Bro = Pet("bear", "Bro")


# Exercise - Chicken Coop

class Chicken:
    total_eggs = 0

    @classmethod
    def display_total_eggs(cls):
        return f"There are a total of : {cls.total_eggs} eggs"

    def __init__(self, name, species, eggs=0):
        self.name = name
        self.species = species
        self.eggs = eggs

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


c1 = Chicken("Alice", "Tyson's")
c2 = Chicken("Brad", "Meyer's")

print("The number of chicken eggs: ", Chicken.total_eggs)
print(c1.lay_egg())
print(c2.lay_egg())
print("The number of chicken eggs: ", Chicken.total_eggs)

print("This is an example of a class method - > ", Chicken.display_total_eggs())
