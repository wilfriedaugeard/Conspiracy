class Board:
    def __init__(self):
        self.deck = [0]*15
        self.placeCards = []
        self.current_pos = 0

    def setCard(self, card, pos):
        self.deck[pos] = card

    def addCard(self, card):
        if(self.current_pos < 15):
            self.setCard(card, self.current_pos)
            self.current_pos += 1

    def addPlaceCard(self, card):
        self.placeCards.append(card)

    def display(self):
        i = 0
        print("BOARD:")
        while(i < self.current_pos):
            self.deck[i].display()
            i+=1
        print("---------------------")
        for card in self.placeCards:
            card.display()
        print("\n")


    # Getters
    def getDeck(self):
        return self.deck
    def getPos(self):
        return self.current_pos
    def getPlaceCards(self):
        return self.placeCards
    