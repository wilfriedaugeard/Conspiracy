import pygame
class pileView:
    def __init__(self, view):
        self.view = view
        self.defaultImageCard = view.getDefaultImageCard()
        self.window = view.getWindow()
        self.width = view.getWidth()
        self.height = view.getHeight()
        self.spaceBorder = view.getSpaceBorder()
        self.myfont2 = view.getMyfont2()

    def drawPileInPiles(self, pile, width, height, pos, x, ystart, value):
        y = ystart+((height+10)*pos)
        image = pile.getImage()
        pile.initView(self.view.getWindow(), self.view.getMyfont2(), x, y, width, height, self.defaultImageCard, image)

    def displayPile(self, lordPile, placePile):
        for pile in lordPile.getPile():
            pile.display()
        placePile.display()

    def initializePile(self, lordPile, placePile):
        lordSize = 100
        placeHeight = int(lordSize/2)
        pilesArray = lordPile.getPile()
        nb = len(pilesArray)
        ydep = (nb*lordSize) + (nb-1)*10
        ydep /= 2
        ydep = self.height/2 - ydep
        x = self.width - lordSize - self.spaceBorder
        for i in range(len(pilesArray)):
            self.drawPileInPiles(pilesArray[i], lordSize, lordSize, i, x, ydep, "")
        x = self.spaceBorder
        y = (self.height/2)+10+75+10
        placePile.initView(self.window, self.myfont2, x, y, lordSize, placeHeight, self.defaultImageCard, pygame.image.load("assets/images/lordDeck.png").convert())
