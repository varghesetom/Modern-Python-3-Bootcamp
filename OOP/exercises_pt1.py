
# Example of Class where it can be applied generically


class Comment():
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


c = Comment("tford112", "the alter ego")

# Example of Class that is specific to one person


class Spiderman():
    def __init__(self):
        self.name = "Peter Parker"
        self.affiliation = "Marvel"


s = Spiderman()

''' _name -> conventionality for a private '''

''' __name (double underscore) -> name mangling, which is important later for
inheritance '''

''' __name__ dunder methods -> Python has these built - in '''


# A User class with both instance attributes and instance methods
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1)

# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))
#
#
# print(user2.is_senior())
# print(user1.age)  # Print age before we update it
# print(user1.birthday())  # updates age
# print(user1.age)  # Print new value of age
