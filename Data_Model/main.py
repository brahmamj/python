from FrenchDeck import FrenchDeck
from FrenchDeck import Card
from random import choice
deck = FrenchDeck()
print(f"Length of the deck : ",len(deck))
print(deck)
#print(deck[0])
#print(deck[-1])
#print(choice(deck))
#print(deck[11::13])

## Since FrenchDeck class implements __getitem__ method, it is iterable
## So, we can use for loop to iterate over the deck
for card in deck:
    print(card)

print(Card('K','hearts') in deck)

suite_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suite_values) + suite_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)