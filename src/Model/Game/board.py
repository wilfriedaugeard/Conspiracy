'''
Class Board: Manages cards in board player
'''
class Board:
    def __init__(self):
        self.deck = [0]*15
        self.placeCards = []
        self.current_pos = 0
    
    # Place a card on a deck place
    def setCard(self, card, pos):
        self.deck[pos] = card
    
    # Add a card to the deck
    def addCard(self, card):
        if(self.current_pos < 15):
            self.setCard(card, self.current_pos)
            self.current_pos += 1

    # Add a place card
    def addPlaceCard(self, card):
        self.placeCards.append(card)
    
    # Display the board on shell
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
    
