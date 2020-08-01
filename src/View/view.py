import pygame
class View:
    
    def __init__(self, width, height, backgroundLocation):

        self.width = width
        self.height = height
        self.backgroundLocation = backgroundLocation
        self.myfont = pygame.font.SysFont('nanumsquareround', 25)
        self.myfont2 = pygame.font.SysFont('nanumsquareround', 20)
        
        self.window = self.createWindow(self.width, self.height)
        self.background = self.setBackground(backgroundLocation)
        
        self.titleimage = pygame.image.load("assets/images/title.png").convert_alpha()
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

        self.lastWinnerCrown = None


    '''
    INIT VIEW
    '''
    def createWindow(self, width, height):
        return pygame.display.set_mode((width, height))

    def setBackground(self, imageLocation):
        bg = pygame.image.load(imageLocation).convert()
        self.window.blit(bg, (0,0))
        return bg

    def displayTitle(self):
        coeff = 0.8
        width = int(640*coeff)
        height = int(100*coeff)
        image = pygame.transform.scale(self.titleimage, (width, height))
        self.window.blit(image, ((self.width/2)-width/2,self.spaceBorder))


    '''
    REFRESH
    '''

    def refreshBg(self):
        self.window.blit(self.background, (0,0))

    def refresh(self):
        pygame.display.flip()

    '''
    DRAW CARD
    '''

    def drawCard(self, image, value, x,y, font):
        self.window.blit(image, (x, y))
        ### display the number (tempory)
        text = font.render(value, False, (0, 0, 0))
        textRect = text.get_rect(center=(x+(image.get_width()/2),y+(image.get_height()/2)))
        self.window.blit(text, textRect)

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

    '''
    BOARD
    '''
    def displayBoard(self, deck, opponentDeck):
        for i in range(len(deck)):
            if(deck[i] != 0):
                self.drawCardInBoard(deck[i].getImage(), deck[i].getValue(), i)
        for i in range(len(opponentDeck)):
            if(opponentDeck[i] != 0):
                self.drawCardInOpponentBox(opponentDeck[i].getImage(), opponentDeck[i].getValue(), i)    

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
                    self.drawCard(image, str(value), startX+((cardWidth+vspace)*i), startY, self.myfont)
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
                self.drawCard(image, "", startX+((cardWidth+vspace)*i), startY, self.myfont)
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


    '''
    DECK
    '''
    def initializeDecks(self, lordDeck, placeDeck):
        lordSize = 150
        placeHeight = int(lordSize/2)
        lordDeck.initView(self.window, self.myfont2, self.spaceBorder, (self.height/2)-lordSize, lordSize, lordSize, self.defaultImageCard, pygame.image.load("assets/images/lordDeck.png").convert())
        placeDeck.initView(self.window, self.myfont2, self.spaceBorder, (self.height/2)+10, lordSize, placeHeight, self.defaultImageCard, pygame.image.load("assets/images/lordDeck.png").convert())


    def drawDeck(self, deck, defaultImage, imageDeck, value, x, y, width, height):
        if(len(deck) == 0):
            image = pygame.transform.scale(defaultImage, (width,height))
        else:
            image = pygame.transform.scale(imageDeck, (width,height))
        self.drawCard(image, value, x, y, self.myfont2)

    def displayDecks(self, lordDeck, placeDeck):
        lordDeck.display()
        placeDeck.display()
       
    '''
    PILE
    '''
    def drawPileInPiles(self, pile, width, height, pos, x, ystart, value):
        y = ystart+((height+10)*pos)
        image = pile.getImage()
        pile.initView(self.window, self.myfont2, x, y, width, height, self.defaultImageCard, image)
        #self.drawDeck(pile.getPile(), self.defaultImageCard, image, value, x, y, width, height)

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
        

    '''
    OPPONENT BOX
    '''
    def drawOppentBox(self, x, y, width, height):
        image = pygame.transform.scale(self.background, (width,height))
        self.drawCard(image, "", x, y, self.myfont)

    def initializeOpponentScreen(self, player):
        boxWidth = 300
        boxHeight = 200

        xBox = self.width-self.spaceBorder-boxWidth
        yBox = self.spaceBorder

        self.drawOppentBox(xBox, yBox, boxWidth, boxHeight)


    '''
    SCORE BOX
    '''
    def drawInfoBox(self, player1, player2):
        
        width = 300
        height = 200
        image = pygame.transform.scale( pygame.image.load("assets/images/scoreBox.jpg").convert(), (width, height))

        x = self.spaceBorder
        y = self.height-self.spaceBorder-height
        self.window.blit(image, (x, y))

        # Text
        nameP1 = player1.getName()+":"
        nameP2 = player2.getName()+":"
        scoreP1 = str(player1.getPearlPts())
        scoreP2 = str(player2.getPearlPts())
        txtP1Pearl = "pearl" 
        txtP2Pearl = "pearl"


        if(player1.getPearlPts() > 1):
            txtP1Pearl += "s"
        if(player2.getPearlPts() > 1):
            txtP2Pearl += "s" 

        yP1 = y+(image.get_height()/2)-30
        yP2 = y+(image.get_height()/2)

        # Crown image
        X = x+20
        crownImage = pygame.transform.scale( pygame.image.load("assets/images/crown.png").convert_alpha(), (20, 20))

        if(player1.getPearlPts() > player2.getPearlPts()):
            self.window.blit(crownImage, (X, yP1))
            self.lastWinnerCrown = player1
        
        if(player2.getPearlPts() > player1.getPearlPts()):
            self.window.blit(crownImage, (X, yP2))
            self.lastWinnerCrown = player2

        if(player1.getPearlPts() == player2.getPearlPts() and player1.getPearlPts() != 0):
            if(self.lastWinnerCrown == player1):
                self.window.blit(crownImage, (X, yP2))
            else:
                self.window.blit(crownImage, (X, yP1))


        # Player name
        X += 30
        textP1 = self.myfont.render(nameP1, False, (0, 0, 0))
        textP2 = self.myfont.render(nameP2, False, (0, 0, 0))
        self.window.blit(textP1, (X, yP1))
        self.window.blit(textP2, (X, yP2))
        
        # Score
        X += width/2-30
        textP1 = self.myfont.render(scoreP1, False, (0, 0, 0))
        textP2 = self.myfont.render(scoreP2, False, (0, 0, 0))
        self.window.blit(textP1, (X, yP1))
        self.window.blit(textP2, (X, yP2))

        # Pearl text
        X += 35
        textP1 = self.myfont.render(txtP1Pearl, False, (0, 0, 0))
        textP2 = self.myfont.render(txtP2Pearl, False, (0, 0, 0))
        self.window.blit(textP1, (X, yP1))
        self.window.blit(textP2, (X, yP2))





    # Getters
    def getWindow(self):
        return self.window
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height