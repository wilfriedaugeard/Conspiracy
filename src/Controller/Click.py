import pygame 
# Initialize click event and flags
def initializeClick(game, player):
    game.getView().setFlood(False)
    if game.getView().getChoiceNb() and game.getView().getOneRect().collidepoint(pygame.mouse.get_pos()):
        player.setNbCardChosen(1)
        game.getView().setFlood(True)
        play(game)
    elif game.getView().getChoiceNb() and game.getView().getTwoRect().collidepoint(pygame.mouse.get_pos()):
        player.setNbCardChosen(2)
        game.getView().setFlood(True)
        play(game)
    elif game.getView().getChoiceNb() and game.getView().getThreeRect().collidepoint(pygame.mouse.get_pos()):
        player.setNbCardChosen(3)
        game.getView().setFlood(True)
        play(game)
    game.getLordDeck().setIsClick(False)
    game.getView().setChoiceNumber(False)
    game.getPlaceDeck().setIsClick(False)
    for pile in game.getLordPile().getPile():
        pile.setIsClick(False)
    game.getPlacePile().setIsClick(False)

# Check collision on click and set click flags
def onClick(game, player):
    if game.getView().getFlood():
        for card in game.getChosenCards():
            if(card.getRect().collidepoint(pygame.mouse.get_pos())):
                game.setWaiting(False)
                initializeClick(game, player)
                game.tmpPlay(game.getPlayer1(), game.getChosenCards(), card)
    else:
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



def mainMenuClick(game):
    if(game.getView().getMainMenu().getRectPlayButton().collidepoint(pygame.mouse.get_pos())):
        game.playParty()

def play(game):
    game.setWaiting(True)
    game.getView().setDisplayChoiceDeckCards(True)
    game.playerTurn(game.getPlayerToPlay())

    if(game.getWaiting()):
        return
    game.getPlayer1().computePearlPts()
    game.getPlayer2().computePearlPts()
    game.setPlayerToPlay(game.getPlayer2())
    game.getView().setDisplayChoiceDeckCards(False)
