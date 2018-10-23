def valid_parentheses(s):
    # result = s.split("()")
    # if any(r != "" for r in result):
    #     print(False)
    count = 0
    for part in s:
        if part == "(":
            count += 1
        if part == ")":
            count -= 1
        if count < 0:  ## checking whether it is ")(" which is still incorrect
            return (False)
    return (count == 0)
'''
valid_parentheses("()") # True
valid_parentheses(")(()))") # False
valid_parentheses("(") # False
valid_parentheses("(())((()())())") # True
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def reverse_vowels(input):
    vowels = "aeiou"
    extract = ""
    ans = ""
    rev_counter = 0
    ## extract the vowels from the phrase/word
    for s in input:
        if (s in vowels) or (s in vowels.upper()) :
            extract += s
    ## make sure to reverse this extract
    rev_extract = extract[::-1]

    ## now go back through the input and create the new phrase
    for s in input:
        if (s in vowels) or (s in vowels.upper()):
            ## whenever encounter the vowel, replace in order the rev_counter
            ans += rev_extract[rev_counter]
            rev_counter +=1
        else:
            ans += s
    return (ans)
'''
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("Hello!") # "Holle!"
reverse_vowels("Tomatoes") # "Temotaos"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

## RETURN TO THE PROBLEM
def three_odd_numbers(l1):
    sum = 0
    counter = 0
    while counter <= (len(l1) -2):
        num = counter
        while num <= (counter+2):
            sum += l1[num]
            counter += 1
        if sum % 2 != 0:
            return (True)
        counter += 1
    return (False)

'''
three_odd_numbers([1,2,3,4,5]) # True

print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False
'''


def mode(arr):
    num_dict = {}
    for num in arr:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    ans = max(num_dict, key = num_dict.get)
    return ans

# mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])

def running_average():


'''
rAvg = running_average();
rAvg(10) // 10.0;
rAvg(11) // 10.5;
rAvg(12) // 11;

rAvg2 = running_average()
rAvg2(1) // 1
rAvg2(3) // 2
'''
