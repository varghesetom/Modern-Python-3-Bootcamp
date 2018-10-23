def two_list_dictionary(keys, vals):
    dic = {}
    for ind, val in enumerate(keys):
        if ind < len(vals):
            dic[keys[ind]] = vals[ind]
        else:
            dic[keys[ind]] = None
    print(dic)

def range_in_list(l, n1=0, n2 = None):
    ## defaulting n2 to be None in case there is no arg passed in for n2
    ## will become the last item by default with snippet below
    n2 = n2 or l[-1]
    new_l = l[n1:n2+1]
    print(sum(new_l))

def same_frequency(n1, n2):
    if len(str(n1)) == len(str(n2)):
        return True
    else:
        return False

def nth(l, n):
    return l[n]

## Finding duplicate within list
from collections import Counter
def yo(arr):
    counts = Counter(arr)
    for c in counts:
        tally = counts[c]
        if tally != 1:
            return c
    else:
        return None

## sum diagonals

def sum_up_diagonals(lol):
    first_diag = 0
    second_diag = 0
    incr = -1
    for i in range(len(lol)):
        first_diag += lol[i][i]
        second_diag += lol[i][incr]
        incr -= 1
    return first_diag + second_diag

### Find min/max of dictionary keys

def min_max_key_in_dictionary(d):
    min_key = min(d.keys())
    max_key = max(d.keys())
    return [min_key, max_key]

## Find number of times a number is followed by a larger number across list


def find_greater_numbers(l):
    count = 0
    limit = len(l)
    for elem in l[::-1]:
        pos = 0
        while (pos != limit):
            if elem > l[pos]:
                count += 1
            pos += 1
        limit -= 1
    print(count)

def two_oldest_ages(l):
    # oldest = max(l)
    # l.remove(oldest)
    # second_oldest = max(l)
    # print([second_oldest, oldest])
    print(sorted(l[-2:]))


def is_odd_string(word):
    alpha = {
            "a": 1, "b": 2, "c" :3, "d" : 4, "e" : 5, "f" : 6,
            "g" : 7, "h" : 8, "i" : 9, "j": 10, "k" : 11, "l" : 12,
            "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" :17, "r" : 18,
            "s" : 19, "t" : 20, "u" : 21, "v" :22 , "w" :23, "x" : 24,
            "y" : 25, "z" : 26
    }
    count = 0
    for s in word:
        val = alpha[s]
        count += val
    if count % 2 != 0:  ## checking whether it is odd
        print(count, "True")
    else:
        print(count, "False")
