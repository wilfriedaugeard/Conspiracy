import pygame, time
from pygame.locals import *
class mainMenu:
    def __init__(self, view, btnWidth, btnHeight):
        self.view = view
        self.window = view.getWindow()
        self.width = view.getWidth()
        self.height = view.getHeight()
        self.spaceBorder = view.getSpaceBorder()
        self.rectBackground = Rect(0, 0, self.width, self.height)
        self.BLACK = (0,0,0)

        self.titleImage =  pygame.image.load('assets/images/titlewhite.png').convert()

        self.buttonBackground = pygame.image.load("assets/images/flood.png").convert()
        self.btnWidth = btnWidth
        self.btnHeight = btnHeight
        self.playButton =  pygame.transform.scale(self.buttonBackground, (self.btnWidth, self.btnHeight))



    def launch(self):
        i = 1
        while i <= 100:
            pygame.draw.rect(self.window, self.BLACK, self.rectBackground)
            imageResized = pygame.transform.scale(self.titleImage, (int( self.titleImage.get_width()*i/100), int(self.titleImage.get_height()*i/100)))
            self.view.displayTitle(imageResized)

            self.playButton.set_alpha(int(255*i/100))
            self.view.drawCard(self.playButton, "PLAY", self.width/2 - self.btnWidth/2, self.height/2 - self.btnHeight/2, self.view.getMyfont2())

            self.view.refresh()
            time.sleep(0.01)
            i+=1