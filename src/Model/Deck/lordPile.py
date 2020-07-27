from Model.Card.family import Family
from Model.Deck.pile import Pile

class LordPile:
    def __init__(self):
        self.lordPile = []
        self.createPile()

    def createPile(self):
        path = "assets/images/"
        ext = ".jpg"
        for member in Family:
            image = path+str(member.name).lower()+ext
            self.lordPile.append(Pile(image))

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