from random import shuffle, randint


class Card:
    allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    allowed_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "J", "Q", "K"]

    def __init__(self, value, suit):
        if suit not in Card.allowed_suits:
            raise ValueError("That is not an appropriate suit")
        if value not in Card.allowed_values:
            raise ValueError("That is not an appropriate value")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        allowed_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                          "J", "Q", "K"]

        # Critical Part in how to instantiate each deck with 52 cards

        self.cards = [Card(value, suit) for value in allowed_values
                      for suit in allowed_suits]

        ####
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num=0):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        if num > self.count():
            raise ValueError(
                "You are trying to draw more cards than available")

        dealt_cards = []

        while num != 0:
            random_card = randint(0, self.count() - 1)
            dealt_cards.append(self.cards[random_card])
            num -= 1

        for card in dealt_cards:
            self.cards.remove(card)

        return dealt_cards

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffled = shuffle(self.cards)
        return shuffled

    def deal_card(self):
        card = self._deal(1)
        return card

    def deal_hand(self, num):
        cards = self._deal(num)
        return cards


d = Deck()
d.shuffle()
print(d)

x = d.deal_hand(3)
print(d)
print(x)


## Only after creating the __iter__ dunder method 
for card in d:
    print(card)


''' TESTS '''
# print(len(d.cards))
# x = d._deal(5)
# print(x)
# print(len(d.cards))
#
# if x[1] in d.cards:
#     print("didn't work")
# else:
#     print("yay, the deck doesn't have it anymore")
