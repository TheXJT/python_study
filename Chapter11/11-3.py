class Foo:
	def __getitem__(self,pos):
		return range(0,30,10)[pos]

# f=Foo()
# for i in f: print(i)
# print(202 in f)

from random import shuffle
from frenchdeck import FrenchDeck

def set_card(deck,position,card):
	deck._cards[position]=card

FrenchDeck.__setitem__=set_card
deck=FrenchDeck()
shuffle(deck)
print(deck[:5])