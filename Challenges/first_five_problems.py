def reverse_string(string):
    reverse = string[::-1]
    return reverse

def list_check(l):
    return all(isinstance(arg, (list)) for arg in l)

def remove_every_other(l):
    l2 = []
    for x in range(len(l)):
        if x % 2 == 0:
            l2.append(l[x])
    return l2

def sum_pairs(l, goal):
    for n1 in l:
        for n2 in l[1:]:
            if n1 + n2 == goal:
                return [n1, n2]
            else:
                return []


def vowel_count(string):
    vowels = "aeiou"
    string_lower = string.lower()
    answer = {}
    for vow in vowels:
        if vow in string_lower:
            answer[vow] = string_lower.count(vow)
    return answer
