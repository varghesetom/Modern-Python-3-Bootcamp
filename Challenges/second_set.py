def titleize(string):
    strings = string.split(" ")
    result = ""
    for string in strings:
        string = string[0].upper() + string[1:] + " "
        result += string
    return result[:-1]

def find_factor(num):
    result = []
    for x in range(1, num+1):
        div = num / x
        if div.is_integer():
            result.append(x)
    return result

def includes(collection, val, start=False):
    if type(collection) == list or type(collection) == str:
        if val in collection[start:]:
            return True
        else:
            return False
    if type(collection) == dict:
        if val in collection.values():
            return True
        else:
            return False

def repeat(string, num):
    if num == 0:
        result = ""
    else:
        result = string * num
    return result


def truncate(string, num):
    if num < 3:
        print("Truncation must be at least 3 characters.")
    else:
        end_index = num - 3 # 3 spaces for the ...
        new_str = string[:end_index]
        if end_index < len(string):
            new_str += "..."
        print(new_str)

truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
