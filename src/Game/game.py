from player import Player
from Deck.lordDeck import LordDeck
from Deck.placeDeck import PlaceDeck
from Deck.lordPile import LordPile
from Deck.pile import Pile
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
            self.lordPile.display()
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


    def addCardsInPile(self, cards, pile):
        for c in cards:
            pile.addCard(c)
            
    def unlockPlace(self, player):
        unlock = False
        nbSilverkey = 0
        nbGoldKey = 0
        # ...