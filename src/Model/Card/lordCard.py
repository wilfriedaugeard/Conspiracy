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
        self.rect = self.image.get_rect()

    def display(self):
        print("Lord card:",self.value, self.family.name, "| pearl:",self.power.getPearl(),"key:",self.power.getKey().name)


    def drawCard(self, image, window, x,y, font):
        self.rect = image.get_rect().move(x, y)
        window.blit(image, (x, y))
        ### display the number (tempory)
        value = str(self.value)
        text = font.render(value, False, (0, 0, 0))
        textRect = text.get_rect(center=(x+(image.get_width()/2),y+(image.get_height()/2)))
        window.blit(text, textRect)

    def setRect(self, value):
        self.rect = value

    #Getter
    def getValue(self):
        return self.value
    def getFamily(self):
        return self.family
    def getPower(self):
        return self.power
    def getImage(self):
        return self.image
    def getRect(self):
        return self.rect


    