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
def onClick(game, player, controller):
    if game.getLordDeck().getRect().collidepoint(pygame.mouse.get_pos()):
        game.getLordDeck().setIsClick(True)
        game.getView().setChoiceNumber(True)
    elif game.getPlaceDeck().getRect().collidepoint(pygame.mouse.get_pos()):
        game.getPlaceDeck().setIsClick(True)
    elif game.getPlacePile().getRect().collidepoint(pygame.mouse.get_pos()):
        game.getPlacePile().setIsClick(True)
    else:
        for pile in game.getLordPile().getPile():
            if(not pile.getTransparent() and pile.getRect().collidepoint(pygame.mouse.get_pos())):
                player.setNbCardChosen(len(pile.getPile()))
                game.setPileChosen(pile)
                game.setChosenCards(pile.getPile())
                pile.setIsClick(True)
                game.getView().setFlood(True)
                clickPile(game, controller)


# Main menu click event
def mainMenuClick(game, controller):
    if(game.getView().getMainMenu().getRectPlayButton().collidepoint(pygame.mouse.get_pos())):
        return controller.playParty()


def chooseACardClick(game, controller):
    for card in game.getChosenCards():
        if(card.getRect().collidepoint(pygame.mouse.get_pos())):
            controller.activateFlagScreen('playParty')
            initializeClick(game, game.getPlayerToPlay(), controller)
            game.tmpPlay(game.getPlayer1(), game.getChosenCards(), card)
            game.getPlayerToPlay().setNbCardChosen(0)
            controller.viewTick()

def lordPileClick(game, controller):
    for card in game.getChosenCards():
        if(card.getRect().collidepoint(pygame.mouse.get_pos())):
            game.addPileCardOnDeck(game.getPlayerToPlay())
        controller.activateFlagScreen('playParty')
        initializeClick(game, game.getPlayerToPlay(), controller)
        game.getView().setDisplayChoiceDeckCards(False)
        controller.viewTick()



def clickPile(game, controller):
    controller.activateFlagScreen('lordPile')
    game.getView().setDisplayChoiceDeckCards(True)


def play(game, controller):
    controller.activateFlagScreen('chooseACard')
    game.getView().setDisplayChoiceDeckCards(True)
    game.playerTurn(game.getPlayerToPlay())