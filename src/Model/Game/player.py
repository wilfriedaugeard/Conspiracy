from Model.Game.board import Board
'''
Class Player: all infos about a player
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.pearlPts = 0
        self.nbCardChosen = 0

    # Computes player's pearls number
    def computePearlPts(self):
        pts = 0
        for card in self.board.getDeck():
            if(card != 0):
                pts += card.getPower().getPearl()
        self.pearlPts = pts

    # Display pearl score    
    def display(self):
        print(self.name)
        print("Pearl score:",self.pearlPts)

    # Set how many cards the player has chosen
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