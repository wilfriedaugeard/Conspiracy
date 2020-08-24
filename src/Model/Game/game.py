from Model.Game.player import Player
from Model.Deck.lordDeck import LordDeck
from Model.Deck.placeDeck import PlaceDeck
from Model.Deck.lordPile import LordPile
from Model.Deck.pile import Pile
from Model.Card.lordCard import LordCard

from View.viewTools import *

from Model.Game.placeTools import *
import random, time

class Game:
    def __init__(self, view):
        self.view = view
        self.player1 = Player("Wil")
        self.player2 = Player("IA")
        self.endParty = False
        self.lordDeck  = LordDeck()
        self.placeDeck = PlaceDeck()
        self.lordPile  = LordPile()
        self.placePile = Pile("assets/images/placeDeck.png")
        self.playerToPlay = self.player1
        self.waiting = False
        self.chosenCards = []
        self.pileChosen = None
        

    # Take randomly nb cards from the deck
    def takeCard(self, nbCard, deck):
        cards = []
        if(nbCard > len(deck)):
            nbCard = len(deck)
        self.chosenCards = []
        for i in range(nbCard):
            index = random.randrange(len(deck))
            card = deck[index]
            
            if(type(card) is LordCard):
                cards.append(card)
            self.chosenCards.append(card)
            deck.remove(card)
        return cards

    # Action to do to a turn
    def playerTurn(self, player):
        # Draw lord card and choose randomly one of them
        if(player.getNbCardChosen() == 0):
            nbCard = random.randrange(1,4)
        else:
            nbCard = player.getNbCardChosen()
            print(nbCard)
        self.takeCard(nbCard, self.lordDeck.getDeck())
        if(player == self.player2):
            print("IA turn")
        

    def tmpPlayIA(self, drawedCards):
        card = random.choice(drawedCards)
        drawedCards.remove(card)
        self.player2.getBoard().addCard(card)
        card.display()
        self.addCardsInPile(drawedCards, self.lordPile)
        # Check if a place is unlocked
        #unlockPlace(self, player)
        self.chosenCards = []
        self.switchPlayer()


    def addPileCardOnDeck(self, player):
        for card in self.pileChosen.getPile():
            player.getBoard().addCard(card)
            card.display()
        self.pileChosen.getPile().clear()
        self.pileChosen = None
        self.chosenCards = []
        self.switchPlayer()

    def tmpPlay(self, player, drawedCards, chosenCard):
        card = chosenCard
        drawedCards.remove(card)
        player.getBoard().addCard(card)
        card.display()
        self.addCardsInPile(drawedCards, self.lordPile)
        # Check if a place is unlocked
        #unlockPlace(self, player)
        self.chosenCards = []
        self.switchPlayer()
    
    # Switch player to play
    def switchPlayer(self):
        if(self.playerToPlay == self.player1):
            self.setPlayerToPlay(self.player2)
        else:
            self.setPlayerToPlay(self.player1)

    # Add a pack of cards to a pile
    def addCardsInPile(self, cards, pile):
        for c in cards:
            pile.addCard(c)


    # Setters
    def setPlayerToPlay(self, player):
        self.playerToPlay = player
    def setWaiting(self, wait):
        self.waiting = wait
    def setChosenCards(self, value):
        self.chosenCards = value
    def setEndParty(self, value):
        self.endParty = value
    def setPileChosen(self, pile):
        self.pileChosen = pile

    # Getters
    def getView(self):
        return self.view
    def getPlayer1(self):
        return self.player1
    def getPlayer2(self):
        return self.player2
    def getLordPile(self):
        return self.lordPile
    def getPlacePile(self):
        return self.placePile
    def getLordDeck(self):
        return self.lordDeck
    def getPlaceDeck(self):
        return self.placeDeck 
    def getEndParty(self):
        return self.endParty   
    def getPlayerToPlay(self):
        return self.playerToPlay
    def getWaiting(self):
        return self.waiting
    def getChosenCards(self):
        return self.chosenCards