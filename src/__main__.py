import pygame
from Model.Game.game import Game  
from Controller import Controller
from View.view import View

def launchGame():
    view = View(1920, 1050, "assets/images/background.jpg")
    game = Game(view)
    game.playParty()
    
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    launchGame()

