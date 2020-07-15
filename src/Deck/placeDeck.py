from Card.placeCard import PlaceCard
from Card.family import Family

class PlaceDeck:
    def __init__(self):
        self.deck = []
        self.createDeck()


    def createDeck(self):
        self.createCard(PlaceCard(7,0,0,0,0,0,False, False, False, 0,  Family.BLUE), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.BLUE), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.GREEN), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.YELLOW), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.PURPLE), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(5,1,0,0,0,0,False, False,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(4,2,0,0,0,0,False, False,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(3,0,0,0,0,0,False, False,  False, 2, Family.RED), 1)
        self.createCard(PlaceCard(3,3,0,0,0,0,False, False,  False, 0, Family.RED), 1) 
        self.createCard(PlaceCard(3,0,0,0,0,0,False, False,  False, 1, Family.RED), 2)
        self.createCard(PlaceCard(3,0,0,0,0,0,False, False,  False, 2, Family.RED), 1)
        self.createCard(PlaceCard(3,0,0,0,0,0,True , False,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(0,0,0,0,2,0,False, False,  False, 0, Family.RED), 1) 
        self.createCard(PlaceCard(0,0,0,2,0,0,False, False,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(0,0,1,0,0,0,False, False,  False, 0, Family.RED), 1) 
        self.createCard(PlaceCard(0,0,0,0,0,1,False, False,  False, 0, Family.RED), 1) 
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.RED), 1)
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.GREEN), 1)
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.YELLOW), 1)
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.PURPLE), 1)
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.BLUE), 1)

    def createCard(self, card, nb):
        for i in range(nb):
            self.deck.append(card)