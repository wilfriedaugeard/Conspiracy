from Card.lordCard import LordCard
from Card.family import Family
from Card.power import Power
from Card.key import Key

class LordDeck:
    def __init__(self):
        self.deck = []
        self.createDeck()

    
    def createDeck(self):
        for color in Family:
            self.createCard(LordCard(6, color, Power(Key.EMPTY, 0, False, True )), 1)
            self.createCard(LordCard(4, color, Power(Key.EMPTY, 1, False, False)), 2)
            self.createCard(LordCard(3, color, Power(Key.EMPTY, 2, False, False)), 2)
            self.createCard(LordCard(2, color, Power(Key.GOLD, 0, False, False)), 2)
            self.createCard(LordCard(1, color, Power(Key.SILVER, 0, False, False)), 4)
            self.createCard(LordCard(0, color, Power(Key.EMPTY, 0, True , False)), 1)

    def createCard(self, card, nb):
        for i in range(nb):
            self.deck.append(card)

    # Getters
    def getDeck(self):
        return self.deck