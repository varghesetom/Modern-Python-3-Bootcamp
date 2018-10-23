import json

j = json.dumps(["foo", {"bar": ("baz", None, 1.0, 2)}])


## converts into a json string (no tuples exist in JavaScript)
print(j)

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

c = Cat("Tommy", "Tabby")

jc = json.dumps(c.__dict__)
print(jc)
