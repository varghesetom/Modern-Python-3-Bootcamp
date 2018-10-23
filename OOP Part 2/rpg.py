class Character:
    def __init__(self, name , hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def __repr__(self):
        return (f"{self.name} is a level {self.level} character")

class NPC(Character):
    def speak(self):
        return "The king's tax increase is affecting my wares business"

npc = NPC("Tavin", 21, 4)
print(npc)
print(npc.speak())
