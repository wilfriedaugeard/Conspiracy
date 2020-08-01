from Model.Card.placeCard import PlaceCard
from Model.Card.family import Family
import pygame


class PlaceDeck:
    def __init__(self):
        self.deck = []
        self.createDeck()

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
        self.createCard(PlaceCard(7,0,0,0,0,0,False, False, False, 0,  Family.BLUE), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.BLUE), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.GREEN), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.YELLOW), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.PURPLE), 1)
        self.createCard(PlaceCard(0,0,0,0,0,0,False, True,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(5,1,0,0,0,0,False, False,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(4,2,0,0,0,0,False, False,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(3,0,0,0,0,0,False, False,  False, 2, Family.RED), 1)
        self.createCard(PlaceCard(3,3,0,0,0,0,False, False,  False, 0, Family.RED), 1) 
        self.createCard(PlaceCard(3,0,0,0,0,0,False, False,  False, 1, Family.RED), 2)
        self.createCard(PlaceCard(3,0,0,0,0,0,False, False,  False, 2, Family.RED), 1)
        self.createCard(PlaceCard(3,0,0,0,0,0,True , False,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(0,0,0,0,2,0,False, False,  False, 0, Family.RED), 1) 
        self.createCard(PlaceCard(0,0,0,2,0,0,False, False,  False, 0, Family.RED), 1)
        self.createCard(PlaceCard(0,0,1,0,0,0,False, False,  False, 0, Family.RED), 1) 
        self.createCard(PlaceCard(0,0,0,0,0,1,False, False,  False, 0, Family.RED), 1) 
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.RED), 1)
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.GREEN), 1)
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.YELLOW), 1)
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.PURPLE), 1)
        self.createCard(PlaceCard(1,0,0,0,0,0,False, False,  True, 0, Family.BLUE), 1)

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
        valueLordDeck = "placeDeck (" +str(len(self.deck))+")"
        if(len(self.deck) == 0):
            image = pygame.transform.scale(self.defaultImage, (self.width, self.height))
        else:
            image = pygame.transform.scale(self.image, (self.width, self.height))
        self.drawCard(image, valueLordDeck, self.x, self.y, self.font)

    def drawCard(self, image, value, x,y, font):
        self.rect = image.get_rect().move(x, y)
        self.window.blit(image, (x, y))
        ### display the number (tempory)
        text = font.render(value, False, (0, 0, 0))
        textRect = text.get_rect(center=(x+(image.get_width()/2),y+(image.get_height()/2)))
        self.window.blit(text, textRect)
    
    # Getters
    def getDeck(self):
        return self.deck
    def getRect(self):
        return self.rect