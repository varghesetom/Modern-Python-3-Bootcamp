import re

def parse_date(input):
    date_regex = re.compile(r'^(?P<day>\d{2})[/,.](?P<month>\d{2})[/,.](?P<year>\d{4})$')
    match = date_regex.search(input)
    if match:
        return ({"d": match.group("day"), "m": match.group("month"), "y" : match.group("year")})
    return None

print(parse_date("12,01,1995"))
