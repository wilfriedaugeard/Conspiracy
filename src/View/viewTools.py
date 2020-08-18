
# View initialization
def initializeView(game):
    game.getView().refreshBg()
    game.getView().displayTitle(game.getView().getTitleImage())
    game.getView().initializeOpponentScreen(game.getPlayer2())
    game.getView().initializeBoard(5, 20, 10)
    game.getView().initializePile(game.getLordPile(), game.getPlacePile())
    game.getView().initializeDecks(game.getLordDeck(), game.getPlaceDeck())
    game.getView().drawChoiceNumber(game.getLordDeck())
    

# Tick
def viewTick(game):
    initializeView(game)
    game.getView().displayDecks(game.getLordDeck(), game.getPlaceDeck())  
    game.getView().displayBoard(game.getPlayer1().getBoard().getDeck(), game.getPlayer2().getBoard().getDeck())
    game.getView().displayPile(game.getLordPile(), game.getPlacePile())
    game.getView().drawInfoBox(game.getPlayer1(),  game.getPlayer2())
    game.getView().displayFlood()
    game.getView().displayTokenCardsFromDeck(game.getChosenCards())
    game.getView().refresh()