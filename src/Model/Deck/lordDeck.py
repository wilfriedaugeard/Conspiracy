from Model.Card.lordCard import LordCard
from Model.Card.family import Family
from Model.Card.power import Power
from Model.Card.key import Key

class LordDeck:
    def __init__(self):
        self.deck = []
        self.createDeck()

    
    def createDeck(self):
        i = 0
        path = "assets/images/"

        for color in Family:
            image = path+str(color.name).lower()+".jpg"
            self.createCard(LordCard(6, color, Power(Key.EMPTY, 0, False, True ), image), 1)
            self.createCard(LordCard(4, color, Power(Key.EMPTY, 1, False, False), image), 2)
            self.createCard(LordCard(3, color, Power(Key.EMPTY, 2, False, False), image), 2)
            self.createCard(LordCard(2, color, Power(Key.GOLD, 0, False, False), image), 2)
            self.createCard(LordCard(1, color, Power(Key.SILVER, 0, False, False), image), 4)
            self.createCard(LordCard(0, color, Power(Key.EMPTY, 0, True , False), image), 1)
            i+=1

    def createCard(self, card, nb):
        for i in range(nb):
            self.deck.append(card)

    # Getters
    def getDeck(self):
        return self.deck