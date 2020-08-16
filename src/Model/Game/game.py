from Model.Game.player import Player
from Model.Deck.lordDeck import LordDeck
from Model.Deck.placeDeck import PlaceDeck
from Model.Deck.lordPile import LordPile
from Model.Deck.pile import Pile
from Model import Deck

from Controller.Controller import *
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
        

    def playParty(self):
        initializeView(self)
        while(controllerTick(self)!=0):
            while(self.player1.getBoard().getPos() < 15 and self.player2.getBoard().getPos() < 15):
                self.hoverAvailableChoiceBeginTurn(self.playerToPlay, self.player1)
                if(not self.endParty and self.playerToPlay == self.player2):
                    time.sleep(0.5)
                    self.playerTurn(self.playerToPlay)
                    self.player1.computePearlPts()
                    self.player2.computePearlPts()
                    self.playerToPlay = self.player1
                    time.sleep(0.5)
                else:
                    if(controllerTick(self) == 0):
                        return
                viewTick(self)
            self.endParty = True
            



    # Draw randomly nb cards among the deck
    def drawCard(self, nbCard, deck):
        cards = []
        if(nbCard > len(deck)):
            nbCard = len(deck)
        for i in range(nbCard):
            index = random.randrange(len(deck))
            card = deck[index]
            cards.append(card)
            deck.remove(card)
        return cards

   
    def playerTurn(self, player):
        # Draw lord card and choose randomly one of them
        if(player.getNbCardChosen() == 0):
            nbCard = random.randrange(1,4)
        else:
            nbCard = player.getNbCardChosen()
            print(nbCard)
        drawedCards = self.drawCard(nbCard, self.lordDeck.getDeck())
        card = random.choice(drawedCards)
        drawedCards.remove(card)
        player.getBoard().addCard(card)
        card.display()
        self.addCardsInPile(drawedCards, self.lordPile)
        # Check if a place is unlocked
        unlockPlace(self, player)


    def addCardsInPile(self, cards, pile):
        for c in cards:
            pile.addCard(c)


    def play(self):
        self.playerTurn(self.playerToPlay)
        self.player1.computePearlPts()
        self.player2.computePearlPts()
        self.playerToPlay = self.player2

    def onClick(self, player):
        if self.view.getFlood():
            pass
        else:
            if self.lordDeck.getRect().collidepoint(pygame.mouse.get_pos()):
                self.lordDeck.setIsClick(True)
                self.view.setChoiceNumber(True)

            elif self.placeDeck.getRect().collidepoint(pygame.mouse.get_pos()):
                self.placeDeck.setIsClick(True)
            elif self.placePile.getRect().collidepoint(pygame.mouse.get_pos()):
                self.placePile.setIsClick(True)
            else:
                for pile in self.lordPile.getPile():
                    if(pile.getRect().collidepoint(pygame.mouse.get_pos())):
                        pile.setIsClick(True)


    def hoverAvailableChoiceBeginTurn(self, playerTurn, player):
        if(playerTurn == player):
            if(len(self.lordDeck.getDeck()) > 0):
                self.lordDeck.setIsClick(True)
            for pile in self.lordPile.getPile():
                if(len(pile.getPile())+player.getBoard().getPos()-1 < 15):
                    pile.setIsClick(True)

        if(len(self.lordDeck.getDeck()) == 0):
            self.lordDeck.setTransparent(True)
        for pile in self.lordPile.getPile():
            if(not (len(pile.getPile())+player.getBoard().getPos()-1 < 15)):
                pile.setTransparent(True)



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