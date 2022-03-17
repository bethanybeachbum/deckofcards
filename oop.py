# card class

from random import shuffle

class Card:
	"""Creates a card"""

	def __init__(self, value, suit):
		self.suit = suit
		self.value = value

	def __repr__(self):
		# return f'Card("{self.value}" of "{self.suite}")'
		return f'{self.value} of {self.suit}'


class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		# Python line comprehension of
		# nested loops
		# creating an instance of Card 52 times inside the Deck instance
		# uses this syntax:
		# newList = [ expression(element) for element in oldList if condition ] 
		self.cards = [Card(value, suit) for suit in suits for value in values]	

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	# accepts a number and removes at most that many cards from the deck
	# if count = 0 return value erro
	def _deal(self, num):
		count = self.count()
		actual = min([count, num])
		print(f"Going to remove {actual} cards")
		if (count == 0):
			raise ValueError("All cards have been dealt")
		# remove cards from deck from end of deck useing negative slice
		cards = self.cards[-actual:]
		# remain deck determined with slice
		self.cards = self.cards[:-actual]   
		return cards
		
	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decs can be shuffled")
		shuffle(self.cards)
		return self



d = Deck()
print(d)
print(f"\nCard count is " + str(d.count() ) )


print("\n" + str(d.count()))

print("\n")
d.shuffle()
print(d.cards)

# print("\n" + str(d._deal(52)))
# print("\n" + str(d._deal(5)))
# print("\n")
card = d.deal_card()
print(card)
print("\n")
hand = d.deal_hand(5)
# print("\n")
print(hand)
