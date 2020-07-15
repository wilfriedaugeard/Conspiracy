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
            drawedCards = self.drawCard(3)
            card = random.choice(drawedCards)
            self.player1.getBoard().addCard(card)
            drawedCards.remove(card) 
            for c in drawedCards:
                print("Card to add: %s" % c)
                self.lordPile.addCard(c)
            self.lordPile.display()
        self.player1.computePearlPts()


    def drawCard(self, nbCard):
        cards = []
        for i in range(nbCard):
            index = random.randrange(len(self.lordDeck.getDeck()))
            card = self.lordDeck.getDeck()[index]
            cards.append(card)
            self.lordDeck.getDeck().remove(card)
        return cards