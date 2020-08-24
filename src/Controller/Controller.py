import pygame, time
from pygame.locals import *
from Controller.Click import *
from View.viewTools import *
from Model.Game.game import Game

EXIT = 0
CONTINUE = 1


class gameController:
    def __init__(self, view):
        self.view = view
        self.game = Game(view)
        self.screenDict = dict(animation = False, mainMenu = False, playParty = False, chooseACard = False, lordPile = False)

    # Controller Tick
    def controllerTick(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return EXIT
            elif event.type == MOUSEBUTTONDOWN:
                return self.schedulerEvent()        
            elif event.type is MOUSEBUTTONUP:
                print("")
        return CONTINUE


    # Schedule events click in relation to screen
    def schedulerEvent(self):
        screen = self.getScreen()
        game = self.game
        if screen == 'mainMenu':
            return mainMenuClick(game, self)
        elif screen == 'playParty':
            self.playTick()
        elif screen == 'chooseACard':
            self.chooseACardTick()
        elif screen == 'lordPile':
            self.lordPileClick()
        else:
            print("")

    # Tick to choose a card 
    def chooseACardTick(self):
        chooseACardClick(self.game, self)

    # Event lordpile click
    def lordPileClick(self):
        lordPileClick(self.game, self)

    # Actions on click
    def playTick(self):
        game = self.game
        if(not game.getEndParty()):
            initializeClick(game, game.getPlayer1(), self)
            onClick(game, game.getPlayer1(), self)
            
    # View tick: call to actualize view
    def viewTick(self):
        viewTick(self.game)

    # Return the actual user screen
    def getScreen(self):
        for screen in self.screenDict:
            if(self.screenDict.get(screen) == True):
                return screen
        return None

    # Load animation at the begin of the game and load game
    def run(self):
        if(self.view.loadAnimation() == []):
            return EXIT
        self.loadGame()
        

    # Load the game et run controller tick
    def loadGame(self):
        self.activateFlagScreen('mainMenu')
        self.view.launchMenu()
        while(self.controllerTick() != 0):
            pass

    # Play a party (course of party events)
    def playParty(self):
        game = self.game
        initializeView(game)
        self.activateFlagScreen('playParty')
        while(game.getPlayer1().getBoard().getPos() < 15 and game.getPlayer2().getBoard().getPos() < 15):
            if(self.controllerTick() == 0):
                return EXIT
            hoverAvailableChoiceBeginTurn(game, game.getPlayerToPlay(), game.getPlayer1())
            if(not game.getEndParty() and game.getPlayerToPlay() == game.getPlayer2()):
                time.sleep(0.5)
                game.playerTurn(game.getPlayerToPlay())
                game.tmpPlayIA(game.chosenCards)
                game.getPlayer1().computePearlPts()
                game.getPlayer2().computePearlPts()
            self.viewTick()
        game.setEndParty(True)
        if(game.getPlayer1().getBoard().getPos() < 15):
            self.completeBoard(game.getPlayer1())
        else:
            self.completeBoard(game.getPlayer2())

   # Compete the player board from deck cards
    def completeBoard(self, player):
        player.setNbCardChosen(1)
        while(player.getBoard().getPos() < 15):
            time.sleep(0.5)
            self.forcedPlay(player)
            self.viewTick()
            self.game.getPlayer1().computePearlPts()
            self.game.getPlayer2().computePearlPts()

    # Force player to take a card from lord deck
    def forcedPlay(self, player):
        self.game.playerTurn(player)
        self.game.tmpPlay(player, self.game.getChosenCards(), self.game.getChosenCards()[0])
       

    # Active only on flag in the hashmap
    def activateFlagScreen(self, flag):
        # Initialize flags
        for x in self.screenDict:
            self.screenDict[x] = False
        self.screenDict[flag] = True
        


# Set flags in order to show choice boxes around cards
def hoverAvailableChoiceBeginTurn(game, playerTurn, player):
    if(playerTurn == player):
        if(len(game.getLordDeck().getDeck()) > 0):
            game.getLordDeck().setIsClick(True)
        for pile in game.getLordPile().getPile():
            if(len(pile.getPile())+player.getBoard().getPos()-1 < 15):
                pile.setIsClick(True)
    if(len(game.getLordDeck().getDeck()) == 0):
        game.getLordDeck().setTransparent(True)
    for pile in game.getLordPile().getPile():
        if(not (len(pile.getPile())+player.getBoard().getPos()-1 < 15)):
            pile.setTransparent(True)
