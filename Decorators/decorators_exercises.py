# Higher Order Functions -- passing funcs as args to other funcs

def sum(n, func):
    total = 0
    for num in range(1, n):
        total += func(num)
    return total

def square(x):
    return x * x

# print(sum(3,square))


### 2.  Nesting Functions
from random import choice

def make_laugh_func():
    def get_laugh():
        l = choice(("Haha", "lol", "teehee"))
        return l

    return get_laugh

# laugh = make_laugh_func()
# print(laugh())

''' Decorators wrap other functions and enhance them
    Decorators are considered to be higher order functions '''

### 1.

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a great day")
    return wrapper

@be_polite  ## this way, I don't have to call in a new variable
            ## i.e. no need for g = be_polite(greet())
def greet():
    print("My name is Tom")

# greet()


### 2. Multiple Arguments for Wrapper

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi I'm {name}."

@shout
def food(main, side):
    return f"I would like a {main} and a side of {side} please"

print(greet("Tom"))
print(food(main = "pizza", side = "cole slaw"))


##### 3 ENSURE AUTHORIZED ADMIN

from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper
