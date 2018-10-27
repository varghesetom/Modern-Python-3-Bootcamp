from random import choice
food = choice(["apple", "grape", "steak", "worm", "dirt", "bacon"])

if (food == "apple") or (food == "grape"):
    print(food + " fruit")
elif (food == "bacon") or (food == "steak"):
    print(food + " meat")
else:
    print(food + " yuck")
