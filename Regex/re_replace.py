import re

text = "Last night, Mrs. Daisy and Mr. White greeted Ms. Chow"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) [a-z]+', re.I)
result = pattern.sub("REDACTED", text)
print(result)

pattern_2 = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
result = pattern_2.sub("\g<1> \g<2>", text)
print(result)
