# Creating Dictionary from Two Lists

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i] : list2[i] for i in range(0,3)}

answer_2 = dict(zip(list1,list2))

# Creating a Dictionary from List of Pairs

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

per_answer = dict(person)

# Mapping ASCII Code to Capital Letters

answer = { i : chr(i) for i in range(65,91)}
