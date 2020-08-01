import pygame
from pygame.locals import *

class Pile:
    def __init__(self, imageLocation):
        self.pile = []
        self.image = pygame.image.load(imageLocation).convert()
        self.imageWidth = 150
        self.imageHeight = 150
        self.image = pygame.transform.scale(self.image, (self.imageWidth, self.imageHeight))

        self.isClick = False
        
        # VIEW
        self.defaultImage = None
        self.font = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.rect = None

        self.transparent = False

    def addCard(self, card):
        self.pile.append(card)

    def print(self):
        for member in self.pile:
            member.display()

    def initView(self, window, font, x, y, width, height, defaultImage, image):
        self.window = window
        self.image = image
        self.defaultImage = defaultImage
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.height = height



    def display(self):
        valueDeck = "(" +str(len(self.pile))+")"
        if(len(self.pile) == 0):
            valueDeck = ""
            image = pygame.transform.scale(self.defaultImage, (self.width, self.height))
        else:
            image = pygame.transform.scale(self.image, (self.width, self.height))
            if(self.transparent):
                image.set_alpha(90)
        self.drawCard(image, valueDeck, self.x, self.y, self.font)

    def drawCard(self, image, value, x,y, font):
        self.rect = image.get_rect().move(x, y)
        if(self.isClick and len(self.pile) != 0):
            border = 3
            color = (242, 175, 19) 
            rect = Rect(x-border, y-border, image.get_width()+2*border, image.get_height()+2*border)
            pygame.draw.rect(self.window, color, rect)
        if(self.transparent):
            image.set_alpha(60)
        self.window.blit(image, (x, y))
        ### display the number (tempory)
        text = font.render(value, False, (0, 0, 0))
        textRect = text.get_rect(center=(x+(image.get_width()/2),y+(image.get_height()/2)))
        self.window.blit(text, textRect)

    def setIsClick(self, isClick):
        self.isClick = isClick

    def setTransparent(self, value):
        self.transparent = value

    # Getters
    def getPile(self):
        return self.pile
    def getImage(self):
        return self.image
    def getRect(self):
        return self.rect

