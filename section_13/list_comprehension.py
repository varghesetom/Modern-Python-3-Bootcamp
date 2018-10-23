# Conditional Logic

l = [1,2,3,4,5]

answer = [val for val in l if val % 2 ==0 ]

# Intersection of Two Lists

list1 = [1,2,3,4]
list2 = [3,4,5,6]

answer_one = [val for val in list1 if val in list2 ]

#Reverse and LowerCase

names = ["Elie", "Tim", "Matt"]

low_reverse = [name.lower() for name in names[::-1]]

# 1-100, numbers divisible by 12

num_100 = [num for num in range(1,101)]

num_div_12 = [num for num in num_100 if num % 12 == 0]

# No Vowels

answer = [letter for letter in "amazing" if letter not in "aeiou"]

# Nested List Comp

real = [[i for i in range(0,3)] for num in range(0,3)]

# 10x10 Nested List comp

answer = [[i for i in range(0,10)] for i in range(0,10)]
