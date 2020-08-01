import pygame 
from pygame.locals import *
from Model.Game.player import Player
from Model.Deck.lordDeck import LordDeck
from Model.Deck.placeDeck import PlaceDeck
from Model.Deck.lordPile import LordPile
from Model.Deck.pile import Pile
from Controller import Controller
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
        self.initializeView()
        while(self.controllerTick()!=0):
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
                    if(self.controllerTick() == 0):
                        return
                self.viewTick()
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
        #board.display()

    def initializeClick(self, player):
        if self.view.getChoiceNb() and self.view.getOneRect().collidepoint(pygame.mouse.get_pos()):
            player.setNbCardChosen(1)
            self.play()
        elif self.view.getChoiceNb() and self.view.getTwoRect().collidepoint(pygame.mouse.get_pos()):
            player.setNbCardChosen(2)
            self.play()
        elif self.view.getChoiceNb() and self.view.getThreeRect().collidepoint(pygame.mouse.get_pos()):
            player.setNbCardChosen(3)
            self.play()
        self.lordDeck.setIsClick(False)
        self.view.setChoiceNumber(False)
        self.placeDeck.setIsClick(False)
        for pile in self.lordPile.getPile():
            pile.setIsClick(False)
        self.placePile.setIsClick(False)

    def play(self):
        self.playerTurn(self.playerToPlay)
        self.player1.computePearlPts()
        self.player2.computePearlPts()
        self.playerToPlay = self.player2

    def onClick(self, player):
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


    def controllerTick(self):
        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0
            elif event.type == MOUSEBUTTONDOWN:
                if(not self.endParty):
                    self.initializeClick(self.player1)
                    self.onClick(self.player1)
            elif event.type is MOUSEBUTTONUP:
                print("")
        return 1


    def initializeView(self):
        self.view.refreshBg()
        self.view.displayTitle()
        self.view.initializeOpponentScreen(self.player2)
        self.view.initializeBoard(5, 20, 10)
        self.view.initializePile(self.lordPile, self.placePile)
        self.view.initializeDecks(self.lordDeck, self.placeDeck)
        self.view.drawChoiceNumber(self.lordDeck)

    def viewTick(self):
        self.initializeView()
        self.view.displayDecks(self.lordDeck, self.placeDeck)  
        self.view.displayBoard(self.player1.getBoard().getDeck(), self.player2.getBoard().getDeck())
        self.view.displayPile(self.lordPile, self.placePile)
        self.view.drawInfoBox(self.player1, self.player2)
        self.view.refresh()