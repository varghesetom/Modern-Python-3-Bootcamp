import re

''' Write a function that accepts a single string. Return a list of binary bytes contained in string.
A byte is a combination of eight 1s or 0s. '''

def parse_bytes(input):
    byte_regex = re.compile(r'\b[0,1]{8}\b')
    match = byte_regex.findall(input)
    return match

print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is 01010111 123 01101100"))
print(parse_bytes("1232"))
