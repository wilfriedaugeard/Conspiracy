from board import Board

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.pearlPts = 0

    def computePearlPts(self):
        for card in self.board.getDeck():
            if(card != 0):
                self.pearlPts += card.getPower().getPearl()

    def display(self):
        print(self.name)
        print("Pearl score:",self.pearlPts)

    # Getters
    def getName(self):
        return self.name
    def getBoard(self):
        return self.board
    def getPearlPts(self):
        return self.pearlPts