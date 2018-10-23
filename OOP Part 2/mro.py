class A:
    def do_something(self):
        print("Method in A")

class B(A):
    def do_something(self):
        print("Method in B")

class C(A):
    def do_something(self):
        print("Method in C")

class D(B,C):
    pass
    # def do_something(self):
    #     print("Method in D")

d = D()
# help(D())
#D -> B -> C - >  A
d.do_something()

###### GENETICS EXAMPLE ##########################

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
