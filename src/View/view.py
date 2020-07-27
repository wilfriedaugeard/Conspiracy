import pygame
class View:
    
    def __init__(self, width, height, backgroundLocation):

        self.width = width
        self.height = height
        self.backgroundLocation = backgroundLocation
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.window = self.createWindow(self.width, self.height)
        self.background = self.setBackground(backgroundLocation)
        self.defaultImageCard = pygame.image.load("assets/images/grey.jpg").convert()
        self.defaultImageCard = pygame.transform.scale(self.defaultImageCard, (150, 150))
        self.defaultImageCard.set_alpha(40) 
    
    
        self.refresh()

        self.nbcardFirstLine = 0
        self.vspace = 0
        self.hspace = 0
        self.minivspace = 5
        self.minihspace = 2
        self.spaceBorder = 20



    def createWindow(self, width, height):
        return pygame.display.set_mode((width, height))

    def setBackground(self, imageLocation):
        bg = pygame.image.load(imageLocation).convert()
        self.window.blit(bg, (0,0))
        return bg



    def refresh(self):
        pygame.display.flip()


    def drawCard(self, image, value, x,y):
        self.window.blit(image, (x, y))
        ### display the number (tempory)
        text = self.myfont.render(value, False, (0, 0, 0))
        textRect = text.get_rect(center=(x+(image.get_width()/2),y+(image.get_height()/2)))
        self.window.blit(text, textRect)

    def displayBoard(self, deck, opponentDeck):
        for i in range(len(deck)):
            if(deck[i] != 0):
                self.drawCardInBoard(deck[i].getImage(), deck[i].getValue(), i)
        for i in range(len(opponentDeck)):
            if(opponentDeck[i] != 0):
                self.drawCardInOpponentBox(opponentDeck[i].getImage(), opponentDeck[i].getValue(), i)

    def drawCardInBoard(self, image, value, pos):
        sizeCardWidth = 150
        sizeCardHeight = 150
        startX = self.width/2
        startY = 200
        self.computeCoordCardInBoard(image, value, pos, sizeCardWidth, sizeCardHeight, self.nbcardFirstLine, 0, startX, startY, self.vspace, self.hspace)

    def drawCardInOpponentBox(self, image, value, pos):
        sizeCardWidth = 25
        sizeCardHeight = 25
        startX = self.width-self.spaceBorder-(300/2)
        startY = self.spaceBorder+30
        self.computeCoordCardInBoard(image, value, pos, sizeCardWidth, sizeCardHeight, self.nbcardFirstLine, 0, startX, startY, self.minivspace, self.minihspace)
        

    def computeCoordCardInBoard(self, image, value, pos, cardWidth, cardHeight, n, h, x, y, vspace, hspace):
        index = 0
        while n > 0:
            startX = x - (cardWidth*(n/2))
            startY = y +(h*(hspace+cardHeight))
            if(n%2 == 0):
                startX -= (vspace/2)+(vspace*((n/2) -1))
            else:
                startX -= int(n/2)*vspace
            for i in range(n):
                if(pos == index):
                    image = pygame.transform.scale(image, (cardWidth, cardHeight))
                    self.drawCard(image, str(value), startX+((cardWidth+vspace)*i), startY)
                index+=1
            
            n-=1
            h+=1


    def initComputeCoordCardInBoard(self, cardWidth, cardHeight, n, h, nbCard, x, y, vspace, hspace):
        while n > 0:
            startX = x - (cardWidth*(n/2))
            startY = y + (h*(hspace+cardHeight))
            if(n%2 == 0):
                startX -= (vspace/2)+(vspace*((n/2) -1))
            else:
                startX -= int(n/2)*vspace

            image = pygame.transform.scale(self.defaultImageCard, (cardWidth, cardHeight))
            for i in range(n):
                self.drawCard(image, "", startX+((cardWidth+vspace)*i), startY)
                nbCard+=1
            n-=1
            h+=1

    def initializeBoard(self, nbcardFirstLine, vspace, hspace):
        self.nbcardFirstLine = nbcardFirstLine
        self.vspace = vspace
        self.hspace = hspace

        sizeCardWidth = 150
        sizeCardHeight = 150
        startX = self.width/2
        startY = 200
        self.initComputeCoordCardInBoard(sizeCardWidth, sizeCardHeight, nbcardFirstLine, 0, 0, startX, startY, self.vspace, self.hspace)

        sizeCardWidth = 25
        sizeCardHeight = 25
        startX = self.width-self.spaceBorder-(300/2)
        startY = self.spaceBorder+30
        self.initComputeCoordCardInBoard(sizeCardWidth, sizeCardHeight, nbcardFirstLine, 0, 0, startX, startY, self.minivspace, self.minihspace)






    def drawDeck(self, deck, defaultImage, imageDeck, value, x, y, width, height):
        if(len(deck) == 0):
            image = pygame.transform.scale(defaultImage, (width,height))
        else:
            image = pygame.transform.scale(imageDeck, (width,height))
        self.drawCard(image, value, x, y)


    def displayDeck(self, lordDeck, placeDeck):
        lordSize = 150
        placeHeight = int(lordSize/2)
    
        valueLordDeck = "LordDeck (" +str(len(lordDeck.getDeck()))+")"
        valuePlaceDeck = "PlaceDeck ("+str(len(placeDeck.getDeck()))+")"

        self.drawDeck(lordDeck.getDeck(), self.defaultImageCard, pygame.image.load("assets/images/lordDeck.png").convert(), valueLordDeck, self.spaceBorder, (self.height/2)-lordSize, lordSize, lordSize)
        self.drawDeck(placeDeck.getDeck(), self.defaultImageCard, pygame.image.load("assets/images/lordDeck.png").convert(), valuePlaceDeck, self.spaceBorder, (self.height/2)+10, lordSize, placeHeight)

    def drawPileInPiles(self, pile, width, height, pos, x, ystart, value):
        y = ystart+((height+10)*pos)
        image = pile.getImage()
        self.drawDeck(pile.getPile(), self.defaultImageCard, image, value, x, y, width, height)

    def displayPile(self, lordPile, placePile):
        lordSize = 100
        placeHeight = int(lordSize/2)

        pilesArray = lordPile.getPile()
        nb = len(pilesArray)
        ydep = (nb*lordSize) + (nb-1)*10
        ydep /= 2
        ydep = self.height/2 - ydep
        x = self.width - lordSize - self.spaceBorder

        for i in range(len(pilesArray)):
            n = len(pilesArray[i].getPile())
            if(n != 0):
                valueLordPile = "("+str(n)+")"
                self.drawPileInPiles(pilesArray[i], lordSize, lordSize, i, x, ydep, valueLordPile)
       
        n = len(placePile.getPile())
        x = self.spaceBorder
        y = (self.height/2)+10+75+10
        
        if(n != 0):
            valuePlacePile = "("+str(n)+")"
            self.drawDeck(placePile.getPile(), self.defaultImageCard, pygame.image.load("assets/images/grey.jpg").convert(), valuePlacePile, x, y, lordSize, placeHeight)
            


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

        self.drawDeck(placePile.getPile(), self.defaultImageCard, self.defaultImageCard, "", x, y, lordSize, placeHeight)


    def drawOppentBox(self, x, y, width, height):
        image = pygame.transform.scale(self.background, (width,height))
        self.drawCard(image, "", x, y)

    def initializeOpponentScreen(self, player):
        boxWidth = 300
        boxHeight = 200

        xBox = self.width-self.spaceBorder-boxWidth
        yBox = self.spaceBorder

        self.drawOppentBox(xBox, yBox, boxWidth, boxHeight)


    def drawInfoBox(self, player1, player2):
        
        width = 300
        height = 200
        image = pygame.transform.scale( pygame.image.load("assets/images/scoreBox.png").convert(), (width, height))

        valueP1 = player1.getName()+": "+str(player1.getPearlPts())+" pearls"
        valueP2 = player2.getName()+": "+str(player2.getPearlPts())+" pearls"
        
        x = self.spaceBorder
        y = self.height-self.spaceBorder-height

        self.window.blit(image, (x, y))
        ### display the number (tempory)
        textP1 = self.myfont.render(valueP1, False, (0, 0, 0))
        textP2 = self.myfont.render(valueP2, False, (0, 0, 0))
       
        self.window.blit(textP1, (x+20,y+(image.get_height()/2)-30))
        self.window.blit(textP2, (x+20,y+(image.get_height()/2)))

    # Getters
    def getWindow(self):
        return self.window
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height