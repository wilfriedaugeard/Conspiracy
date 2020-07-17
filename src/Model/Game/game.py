from Model.Game.player import Player
from Model.Deck.lordDeck import LordDeck
from Model.Deck.placeDeck import PlaceDeck
from Model.Deck.lordPile import LordPile
from Model.Deck.pile import Pile
import random

class Game:
    def __init__(self):
        self.player1 = Player("Wil")
        self.player2 = Player("IA")

        self.lordDeck  = LordDeck()
        self.placeDeck = PlaceDeck()
        self.lordPile  = LordPile()
        self.placePile = Pile()
        

    def playParty(self):
        while(self.player1.getBoard().getPos() < 15 and self.player2.getBoard().getPos() < 15):
            self.playerTurn(self.player1)
        self.player1.computePearlPts()

    # Draw randomly nb cards among the deck
    def drawCard(self, nbCard, deck):
        cards = []
        for i in range(nbCard):
            index = random.randrange(len(deck))
            card = deck[index]
            cards.append(card)
            deck.remove(card)
        return cards

   
    def playerTurn(self, player):
        # Draw lord card and choose randomly one of them
        drawedCards = self.drawCard(3, self.lordDeck.getDeck())
        card = random.choice(drawedCards)
        drawedCards.remove(card)
        player.getBoard().addCard(card)
        self.addCardsInPile(drawedCards, self.lordPile)
        # Check if a place is unlocked
        self.unlockPlace(player)



    def addCardsInPile(self, cards, pile):
        for c in cards:
            pile.addCard(c)


    def unlockPlace(self, player):
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
                if(len(self.placeDeck.getDeck()) < 3 and len(self.placePile.getPile()) > 2):
                    drawedCards = self.drawCard(3, self.placePile.getPile())
                elif(len(self.placeDeck.getDeck()) > 2 and len(self.placePile.getPile()) < 3):
                    drawedCards = self.drawCard(3, self.placeDeck.getDeck())
                else:
                    if(bool(random.getrandbits(1))):
                        drawedCards = self.drawCard(3, self.placeDeck.getDeck())
                    else: 
                        drawedCards = self.drawCard(3, self.placePile.getPile())
                # Take randomly a place between 3 place cards
                placeCard = random.choice(drawedCards)
                drawedCards.remove(placeCard)
                # Put rest in place pile
                self.addCardsInPile(drawedCards, self.placePile)
                # Set the place position 
                placeCard.setPos(i)
                board.addPlaceCard(placeCard)
                nbSilverKey = 0
                nbGoldKey = 0
            i += 1
        board.display()

    