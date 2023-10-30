"""
This example is for learning about dunder/special methods
Special methods are called  by the Python Interpreter, and not you. i.e you dont write my_object.__len__(), and write len(my_object)
Your code should normally not have many direct calls to special methods (the only special  method called by user code is __init__, used to
invoke the intializer of the super class in your own __init__ implementation.
Example 1-1: A deck as a sequence of cards
"""
from random import choice
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,12)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    deck = FrenchDeck()
    # FrenchDeck now behaves like a python standard sequence, because of __Len__ and __getitem__
    print(len(deck))
    print(deck[60])

    # We can also use random function on it
    print(choice(deck))

    # implementing __getitem__ allows free slicing, makes it iterable and reversable
    print(deck[:3])
    for card in deck:
        print(card)
    for card in reversed(deck):
        print(card)

    # Iteration is implicit. There is no __contains__ method so the in operator does a seequential scan. This works because
    # FrenchDeck is iterable
    print(Card('Q', 'hearts') in deck)
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    # We can also define a sort function for our FrenchDeck
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)