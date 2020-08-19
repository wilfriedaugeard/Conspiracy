import pygame 
# Initialize click event and flags
def initializeClick(game, player, controller):
    game.getView().setFlood(False)
    if game.getView().getChoiceNb() and game.getView().getOneRect().collidepoint(pygame.mouse.get_pos()):
        player.setNbCardChosen(1)
        game.getView().setFlood(True)
        play(game, controller)
    elif game.getView().getChoiceNb() and game.getView().getTwoRect().collidepoint(pygame.mouse.get_pos()):
        player.setNbCardChosen(2)
        game.getView().setFlood(True)
        play(game, controller)
    elif game.getView().getChoiceNb() and game.getView().getThreeRect().collidepoint(pygame.mouse.get_pos()):
        player.setNbCardChosen(3)
        game.getView().setFlood(True)
        play(game, controller)
    game.getLordDeck().setIsClick(False)
    game.getView().setChoiceNumber(False)
    game.getPlaceDeck().setIsClick(False)
    for pile in game.getLordPile().getPile():
        pile.setIsClick(False)
    game.getPlacePile().setIsClick(False)

# Check collision on click and set click flags
def onClick(game, player):
    if game.getLordDeck().getRect().collidepoint(pygame.mouse.get_pos()):
        game.getLordDeck().setIsClick(True)
        game.getView().setChoiceNumber(True)
    elif game.getPlaceDeck().getRect().collidepoint(pygame.mouse.get_pos()):
        game.getPlaceDeck().setIsClick(True)
    elif game.getPlacePile().getRect().collidepoint(pygame.mouse.get_pos()):
        game.getPlacePile().setIsClick(True)
    else:
        for pile in game.getLordPile().getPile():
            if(pile.getRect().collidepoint(pygame.mouse.get_pos())):
                pile.setIsClick(True)



def mainMenuClick(game, controller):
    if(game.getView().getMainMenu().getRectPlayButton().collidepoint(pygame.mouse.get_pos())):
        return controller.playParty()

def chooseACardClick(game, controller):
    for card in game.getChosenCards():
        if(card.getRect().collidepoint(pygame.mouse.get_pos())):
            controller.activateFlagScreen('playParty')
            initializeClick(game, game.getPlayerToPlay(), controller)
            game.tmpPlay(game.getPlayer1(), game.getChosenCards(), card)
            controller.viewTick()
          

def play(game, controller):
    controller.activateFlagScreen('chooseACard')
    game.getView().setDisplayChoiceDeckCards(True)
    game.playerTurn(game.getPlayerToPlay())