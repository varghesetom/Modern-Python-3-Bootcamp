import keyword


def contains_keyword(*args):
    for a in args:
        if keyword.iskeyword(a):
            return True
    return False


# Example of using External Module
import termcolor

text = termcolor.colored("Hi There", "cyan", attrs=['underline'])
print(text)
