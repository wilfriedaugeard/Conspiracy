import pygame 
from pygame.locals import *
from Controller.Click import *

EXIT = 0
CONTINUE = 1

def controllerTick(game):
    #Handle Input Events
    for event in pygame.event.get():
        if event.type == QUIT:
            return EXIT
        elif event.type == MOUSEBUTTONDOWN:
            if(not game.getEndParty()):
                if(game.getWaiting()):
                    onClick(game, game.getPlayer1())
                    return CONTINUE
                initializeClick(game, game.getPlayer1())
                onClick(game, game.getPlayer1())
        elif event.type is MOUSEBUTTONUP:
            print("")
    return CONTINUE

def controllerTickMainMenu(game):
    for event in pygame.event.get():
        if event.type == QUIT:
            return EXIT
        elif event.type == MOUSEBUTTONDOWN:
            mainMenuClick(game)
        elif event.type is MOUSEBUTTONUP:
            print("")
    return CONTINUE


# Set flags in order to show choice boxes around cards
def hoverAvailableChoiceBeginTurn(game, playerTurn, player):
    if(playerTurn == player):
        if(len(game.getLordDeck().getDeck()) > 0):
            game.getLordDeck().setIsClick(True)
        for pile in game.getLordPile().getPile():
            if(len(pile.getPile())+player.getBoard().getPos()-1 < 15):
                pile.setIsClick(True)
    if(len(game.getLordDeck().getDeck()) == 0):
        game.getLordDeck().setTransparent(True)
    for pile in game.getLordPile().getPile():
        if(not (len(pile.getPile())+player.getBoard().getPos()-1 < 15)):
            pile.setTransparent(True)
