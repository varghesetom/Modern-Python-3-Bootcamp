
## Creating own for loop


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        func(thing)

a = [1,2,3,4]
my_for(a,print)

sq = lambda x: print(x**2)
print()
my_for(a, sq)
