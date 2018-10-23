'''
*args is a parameter that we can pass to a function that will pack the arguments
being passed into it as a TUPLE

**kwargs is a parameter that we can pass to a function that will pack the arguments
being passed into it as a DICTIONARY
'''

# *args example

def ensure_correct_info(*args):
    if "Tom" in args and "Varghese" in args:
        return "Welcome back Tom!"
    elif "Tom" in args:
        return "Yo Tom"

    return "Not sure who you are..."


# **kwargs example

def favorite_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")

favorite_colors(Cyrus='fuchsia', Tom='blue')

# Combined Example

def display_info(a, b, *args, instructor="Colt", **kwargs):
   print([a, b, args, instructor, kwargs])


# here a = 1, b = 2, args = 3, instructor is default Colt, kwargs is remaining
display_info(1, 2, 3, last_name="Steele", job="Instructor")

''' Using * as an Argument: Argument Unpacking '''

def sum_all_values(*args):
    # there's a built in sum function - we'll see more later!
    return sum(args)

# normally it is fine
# print("hi there", sum([1,2,3,4]))

'''here it is clear that we need to unpack with * '''
sum_all_values(*[1, 2, 3, 4]) # 10
sum_all_values(*(1, 2, 3, 4)) # 10
