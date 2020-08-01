from Model.Card.lordCard import LordCard
from Model.Card.family import Family
from Model.Card.power import Power
from Model.Card.key import Key
import pygame
from pygame.locals import *
class LordDeck:
    def __init__(self):
        self.deck = []
        self.createDeck()

        self.isClick = False
        # VIEW
        self.image = None
        self.defaultImage = None
        self.font = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.rect = None
    
    def createDeck(self):
        i = 0
        path = "assets/images/"
        ext = ".jpg"
        for color in Family:
            image = path+str(color.name).lower()+ext
            self.createCard(LordCard(6, color, Power(Key.EMPTY, 0, False, True ), image), 1)
            self.createCard(LordCard(4, color, Power(Key.EMPTY, 1, False, False), image), 2)
            self.createCard(LordCard(3, color, Power(Key.EMPTY, 2, False, False), image), 2)
            self.createCard(LordCard(2, color, Power(Key.GOLD, 0, False, False), image), 2)
            self.createCard(LordCard(1, color, Power(Key.SILVER, 0, False, False), image), 4)
            self.createCard(LordCard(0, color, Power(Key.EMPTY, 0, True , False), image), 1)
            i+=1

    def createCard(self, card, nb):
        for i in range(nb):
            self.deck.append(card)

    # VIEW
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
        valueLordDeck = "LordDeck (" +str(len(self.deck))+")"
        if(len(self.deck) == 0):
            image = pygame.transform.scale(self.defaultImage, (self.width, self.height))
        else:
            image = pygame.transform.scale(self.image, (self.width, self.height))
        self.drawCard(image, valueLordDeck, self.x, self.y, self.font)

    def drawCard(self, image, value, x,y, font):
        self.rect = image.get_rect().move(x, y)
        if(self.isClick):
            border = 3
            color = (242, 175, 19)  
            rect = Rect(x-border, y-border, image.get_width()+2*border, image.get_height()+2*border)
            pygame.draw.rect(self.window, color, rect)
        self.window.blit(image, (x, y))
        ### display the number (tempory)
        text = font.render(value, False, (0, 0, 0))
        textRect = text.get_rect(center=(x+(image.get_width()/2),y+(image.get_height()/2)))
        self.window.blit(text, textRect)


    def setIsClick(self, isClick):
        self.isClick = isClick

    # Getters
    def getDeck(self):
        return self.deck
    def getRect(self):
        return self.rect