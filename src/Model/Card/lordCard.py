import pygame
class LordCard:
    def __init__(self, value, family, power, imageLocation):
        self.value = value
        self.family = family
        self.power = power
        self.image = pygame.image.load(imageLocation).convert()
        self.imageWidth = 150
        self.imageHeight = 150
        self.image = pygame.transform.scale(self.image, (self.imageWidth, self.imageHeight))

    def display(self):
        print("Lord card:",self.value, self.family.name, "| pearl:",self.power.getPearl(),"key:",self.power.getKey().name)


    #Getter
    def getValue(self):
        return self.value
    
    def getFamily(self):
        return self.family

    def getPower(self):
        return self.power
    def getImage(self):
        return self.image


    