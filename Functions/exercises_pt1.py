def make_noise():
    return "THE CROWD GOES WILD"

print(make_noise())

# Generating Even Numbers
def generate_evens():
    evens = [x for x in range(1,50) if x % 2 == 0]
    return evens

# Animal Speak

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal =="duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

print(speak())
