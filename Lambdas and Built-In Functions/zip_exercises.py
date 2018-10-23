'''
1. Make an iterator that aggregates elements from each of the iterables.

2. Returns an iterator of tuples, where the i-th tuple contains the i-th element from
   each of the argument sequences or iterables.

3. The iterator stops when the shortest input iterable is exhausted.'''

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = {"Aew", "Brad", "Cee"}

# print(list(zip(students, midterms, finals)))

final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}

final_scores = dict(
    zip(students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
        )
)


# String Interleaving

def interleave(s1, s2):
    zipped_tuples = list(zip(s1, s2))
    str_overall = ""
    for tup in zipped_tuples:
        str1 = ""
        for str_el in tup:
            str1 += str_el
        str_overall += str1
    return str_overall


def interleave_better(s1, s2):
    return ''.join(''.join(x) for x in (zip(str1, str2)))


print(interleave("lzr", "iad"))
