from Model.Game.board import Board

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.pearlPts = 0
        self.nbCardChosen = 0


    def computePearlPts(self):
        pts = 0
        for card in self.board.getDeck():
            if(card != 0):
                pts += card.getPower().getPearl()
        self.pearlPts = pts

        
    def display(self):
        print(self.name)
        print("Pearl score:",self.pearlPts)

    def setNbCardChosen(self, value):
        self.nbCardChosen = value

    # Getters
    def getName(self):
        return self.name
    def getBoard(self):
        return self.board
    def getPearlPts(self):
        return self.pearlPts
    def getNbCardChosen(self):
        return self.nbCardChosen