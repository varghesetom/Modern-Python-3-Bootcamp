import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')
res = pattern.search("234823948 blah")
res2 = pattern.search("call me at 914 354-1818")

print(res)
print(res2.group())

## Can also skip the compile part, however this is not efficient if
## you have to use the same regex pattern multiple times

## Also ".findall" searches for all matches not just the first match which is
## what .search does  
print(re.findall(r'\d{3} \d{3}-\d{4}', "914 122-4424 and 849 334-4411"))
