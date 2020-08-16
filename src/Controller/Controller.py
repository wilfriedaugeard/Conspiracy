import pygame 
from pygame.locals import *
from Controller.Click import *

def controllerTick(game):
    #Handle Input Events
    for event in pygame.event.get():
        if event.type == QUIT:
            return 0
        elif event.type == MOUSEBUTTONDOWN:
            if(not game.getEndParty()):
                initializeClick(game, game.getPlayer1())
                onClick(game, game.getPlayer1())
        elif event.type is MOUSEBUTTONUP:
            print("")
    return 1