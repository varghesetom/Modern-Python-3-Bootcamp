# Return Day of Week

def return_day(num):
    days = dict([(1, "Sunday"), (2, "Monday"),
    (3, "Tuesday"), (4, "Wednesday"), (5, "Thursday"), (6, "Friday"), (7, "Saturday")])
    return days.get(num)

# Return Last Element of List

def last_element(l = []):
    if l == []:
        return None
    else:
        return l[-1]

# Single Letter Count

def single_letter_count(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower() #Make sure it is case insensitive
    if (s1.count(s2) != 0):
        return s1.count(s2)
    else:
        return 0

# Multiple Letter Count

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

s1 = multiple_letter_count("hithere")
print(s1)

# List Manipulation

def list_manipulation(l, command, location, value = None ):
    if (command == "remove") and (location == "end"):
        return l[-1]
    elif (command == "remove") and (location == "beginning"):
        return l[0]
    elif (command == "add") and (location == "beginning"):
        return l.insert(0, value)
    elif (command == "add") and (location == "end"):
        return l.insert(-1, value)

# Palindrome

def is_palindrome(s):
    s = s.replace(" ", "").lower() ## remove whitespace and capitalization
    if (s[::] == s[::-1]):
        return True
    else:
        return False

# Multiply Evens

def multiply_even_numbers(l):
    evens = [x for x in l if x % 2 ==0]
    product = 1
    for n in evens:  ## # NOTE: list comprehension is for creating a list
                        #       not for looping to get a product
        product *= n
    return product

l1 = multiply_even_numbers([2,4,5,6])

# Capitalize

def capitalize(s):
    return s[0].upper() + s[1:] ## the .upper() for the first letter only returns
                                #   first letter
