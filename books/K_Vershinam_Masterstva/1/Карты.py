# Колода карт на Python
import collections
from random import choice

Card = collections.namedtuple("Card", ['rank', "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]
    suits = "spades diamonds clubs hearts".split()
    # ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, item):
        return self._card[item]

beer_card = FrenchDeck()
# print(len(beer_card))

#Преимущества метода __getitem__
# print(beer_card[:3])

# print(choice(beer_card)) #Рандомная карта

# for i in reversed(beer_card): #Пробегаемся по объекту в обратном порядке
#     print(i)

# print(Card("Q", "hearts") in beer_card) #Проверяем карту на вхождение


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card: Card):
    # Индекс из массива ranks
    rank_value = FrenchDeck.ranks.index(card.rank)
    #Возвращает число, чем больше его значение, тем выше оно будет стоять
    return rank_value * len(suit_values) + suit_values[card.suit]



for card in sorted(beer_card, key=spades_high):
    print(card)
