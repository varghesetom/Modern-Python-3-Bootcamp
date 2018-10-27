import re

''' Define a function that censors out words that start with "frack". Replace with entire word,
"CENSORED" -- Regex should be case insensitive.
'''

def censor(input):
    censor_regex = re.compile(r'frack[a-z]*', re.I)
    replace = censor_regex.sub("CENSORED", input)
    print(replace)

censor("Frack you")
censor("I hope you fracking frack off")
censor("you Fracking frack")
