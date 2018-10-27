import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b') # \b checks for boundary of space or newline
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

def extract_all_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(input) ## returns list of matches
    return match

def is_valid(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return False

print(is_valid("914 414-4124"))

print(extract_phone("my number is 914 364-1719"))
print(extract_phone("my number is 914 314-515441"))

print(extract_all_phone("my number is 914 364-1719 or call me at 714 841-4188"))
