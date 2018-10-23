class Mother:

    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:

    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "curly"

class Child(Mother, Father):
    pass

c = Child()
print(c.eye_color)
