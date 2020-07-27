import pygame
class Pile:
    def __init__(self, imageLocation):
        self.pile = []
        self.image = pygame.image.load(imageLocation).convert()
        self.imageWidth = 150
        self.imageHeight = 150
        self.image = pygame.transform.scale(self.image, (self.imageWidth, self.imageHeight))

    def addCard(self, card):
        self.pile.append(card)

    def display(self):
        for member in self.pile:
            member.display()



    # Getters
    def getPile(self):
        return self.pile
    def getImage(self):
        return self.image

