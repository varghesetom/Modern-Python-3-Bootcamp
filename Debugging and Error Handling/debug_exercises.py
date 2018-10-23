def colorize(text, color):
    colors = ("cyan", "blue", "magenta")
    if type(text) is not str:
        raise TypeError("text must be an instance of str")
    if type(color) is not str:
        raise TypeError("color must be an instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printing {text} in {color}")


def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Can't divide by 0")
    except TypeError:
        print("Only numbers can be divided!")
    except NameError:
        print("Variable is not defined")
    else:
        return result

print(divide(1,2,3))

'''PDB Trace (Python Debugger)'''

# FIRST EXAMPLE:
# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)


# Be careful with variable names!
def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace()

    return a + b + c + d
add_numbers(1,2,3,4)

# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
