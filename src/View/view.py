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

    def displayBoard(self, deck):
        for i in range(len(deck)):
            if(deck[i] != 0):
                self.drawCardInBoard(deck[i].getImage(), deck[i].getValue(), i)

    def drawCardInBoard(self, image, value, pos):
        n = self.nbcardFirstLine
        y = 0
        index = 0
        sizeCardWidth = 150
        sizeCardHeight = 150
        while n > 0:
            startX = (self.width/2)- (sizeCardWidth*(n/2))
            startY = 200+(y*(self.hspace+sizeCardHeight))
            if(n%2 == 0):
                startX -= (self.vspace/2)+(self.vspace*((n/2) -1))
            else:
                startX -= int(n/2)*self.vspace
            for x in range(n):
                if(pos == index):
                    self.drawCard(image, str(value), startX+((sizeCardWidth+self.vspace)*x), startY)
                index+=1
            
            n-=1
            y+=1


    def initializeBoard(self, nbcardFirstLine, vspace, hspace):
        self.nbcardFirstLine = nbcardFirstLine
        self.vspace = vspace
        self.hspace = hspace

        n = nbcardFirstLine
        h = 0
        nbCard = 0
        sizeCardWidth = 150
        sizeCardHeight = 150
        while n > 0:
            startX = (self.width/2)- (sizeCardWidth*(n/2))
            startY = 200+(h*(hspace+sizeCardHeight))
            if(n%2 == 0):
                startX -= (vspace/2)+(vspace*((n/2) -1))
            else:
                startX -= int(n/2)*vspace

            for i in range(n):
                self.drawCard(self.defaultImageCard, "", startX+((sizeCardWidth+vspace)*i), startY)
                nbCard+=1
            n-=1
            h+=1


    def displayDeck(self, lordDeck):
        lordSize = 150
        if(len(lordDeck.getDeck()) == 0):
            lordDeckImage = self.defaultImageCard
        else:
            lordDeckImage = pygame.image.load("assets/images/lordDeck.png").convert()
            lordDeckImage = pygame.transform.scale(lordDeckImage, (lordSize,lordSize))
        
        value = "LordDeck (" +str(len(lordDeck.getDeck()))+")"
        self.drawCard(lordDeckImage, value, self.spaceBorder, (self.height/2)-lordSize)



    # Getters
    def getWindow(self):
        return self.window
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height