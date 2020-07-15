from Card.family import Family
from Deck.pile import Pile

class LordPile:
    def __init__(self):
        self.lordPile = []
        self.createPile()

    def createPile(self):
        for member in Family:
            self.lordPile.append(Pile())

    def addCard(self, card):
        for member in Family:
            if(card.getFamily() == member):
                self.lordPile[member.value].addCard(card)


    def display(self):
        for pile in self.lordPile:
            if(pile.getPile() != []):
                print("[")
                pile.display()
                print("]")
            else:
                print("[]")

    # Getters
    def getPile(self):
        return self.lordPile