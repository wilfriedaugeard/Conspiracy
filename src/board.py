
class Board:
    def __init__(self):
        self.deck = [0]*15
        self.current_pos = 0

    def placeCard(self, card, pos):
        self.deck[pos] = card

    def addCard(self, card):
        if(self.current_pos < 15):
            self.placeCard(card, self.current_pos)
            self.current_pos += 1

    # Getters
    def getDeck(self):
        return self.deck
    def getPos(self):
        return self.current_pos
    