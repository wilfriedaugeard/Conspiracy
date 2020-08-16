import random
def unlockPlace(game, player):
    nbSilverKey = 0
    nbGoldKey = 0
    i = 0
    # Check the last place
    board = player.getBoard()
    if(board.getPlaceCards() != []):
        lastPlaceCard = board.getPlaceCards()[-1]
        i = lastPlaceCard.getPos()
        if(i<15):
            i+=1
    # Check keys after the last place
    while(i < board.getPos()):
        card = board.getDeck()[i]
        if(card.getPower().getKey().value == 1):
            nbSilverKey+=1
        if(card.getPower().getKey().value == 2):
            nbGoldKey+=1
        # Unlock place
        if(nbGoldKey > 1 or nbSilverKey > 1):
            # Choose the deck to draw
            if(len(game.getPlaceDeck().getDeck()) < 3 and len(game.getPlacePile().getPile()) > 2):
                drawedCards = game.drawCard(3, game.getPlacePile().getPile())
            elif(len(game.getPlaceDeck().getDeck()) > 2 and len(game.getPlacePile().getPile()) < 3):
                drawedCards = game.drawCard(3, game.getPlaceDeck().getDeck())
            else:
                if(bool(random.getrandbits(1))):
                    drawedCards = game.drawCard(3, game.getPlaceDeck().getDeck())
                else: 
                    drawedCards = game.drawCard(3, game.getPlacePile().getPile())
            # Take randomly a place between 3 place cards
            placeCard = random.choice(drawedCards)
            drawedCards.remove(placeCard)
            # Put rest in place pile
            game.addCardsInPile(drawedCards, game.getPlacePile)
            # Set the place position 
            placeCard.setPos(i)
            board.addPlaceCard(placeCard)
            nbSilverKey = 0
            nbGoldKey = 0
        i += 1
