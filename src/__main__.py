import pygame, random
from Model.Game.game import Game  
from Controller import Controller
from View.view import View

def launchGame():
    # Controller.controllerTick()
    view = View(1920, 1050, "assets/images/background.jpg")
    game = Game(view)
    game.playParty()

   
            
        
def loadView():
    window = pygame.display.set_mode((1920, 1050))
    bg = pygame.image.load("assets/images/background.jpg").convert()
    window.blit(bg, (0,0))
    pygame.display.flip()
    
    # TEST
    width, height = pygame.display.get_surface().get_size()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    # color
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0) 
    LORDPILE  = pygame.Color(250, 213, 211)
    PLACEPILE = pygame.Color(218, 250, 211)
    SCOREPLAYER = pygame.Color(211, 242, 250)
    TEST = pygame.Color( 215, 250, 211 )

    # size
    spaceBorder = 20
    space = 10
    vspaceBoard = 20
    hspaceBoard = 10

    lordsize = (150, 150)
    placesize = (150, 75)
    scoreplayer = (250, 150)
    testSize = (100, 100)

    # surface
    lordpile = pygame.Surface(lordsize)  # Create a Surface to draw on.
    textlordPile = myfont.render('Lord Pile', False, (0, 0, 0))
    placepile = pygame.Surface(placesize)
    textplacePile = myfont.render('Place Pile', False, (0, 0, 0))
    scoreArea = pygame.Surface(scoreplayer)

    lordInBoard = pygame.Surface(testSize)


    # rectangle
    pygame.draw.rect(lordpile, LORDPILE, lordpile.get_rect(), 10)  # Draw on it.
    textlordPile_rect = textlordPile.get_rect(center=(spaceBorder+(lordsize[0]/2),(height/2)-lordsize[1]/2))
    pygame.draw.rect(placepile, PLACEPILE, placepile.get_rect())
    textplacePile_rect = textplacePile.get_rect(center=(spaceBorder+(placesize[0]/2),space+(height/2)+placesize[1]/2))
    pygame.draw.rect(scoreArea, SCOREPLAYER, scoreArea.get_rect())
    pygame.draw.rect(lordInBoard, TEST, lordInBoard.get_rect())


    # Blit
    lordPileImage = pygame.image.load("assets/images/grey.jpg").convert()
    lordPileImage = pygame.transform.scale(lordPileImage, (150,150))
    lordPileImage.set_alpha(150)
    window.blit(lordPileImage,  (spaceBorder, (height/2)-lordsize[1]))
    window.blit(textlordPile, textlordPile_rect)
    window.blit(placepile, (spaceBorder, (height/2)+space))
    window.blit(textplacePile, textplacePile_rect)
    window.blit(scoreArea, (spaceBorder, (height-spaceBorder-scoreplayer[1])))
    window.blit(scoreArea, ((width-spaceBorder-scoreplayer[0]), spaceBorder))


    testwidth = width-spaceBorder-testSize[0]
    testheight = (height/2)-(testSize[1]/2)

    # defausse
    window.blit(lordInBoard, (testwidth, testheight))
    window.blit(lordInBoard, (testwidth, testheight+testSize[1]+space))
    window.blit(lordInBoard, (testwidth, testheight+2*(testSize[1]+space)))
    window.blit(lordInBoard, (testwidth, testheight-testSize[1]-space))
    window.blit(lordInBoard, (testwidth, testheight-2*(testSize[1]+space)))

    # Board
    
    yellowLord = pygame.image.load("assets/images/yellow.jpg").convert()
    blueLord = pygame.image.load("assets/images/blue.jpg").convert()
    greenLord = pygame.image.load("assets/images/green.jpg").convert()
    greenLord = pygame.transform.scale(greenLord, (150,150))
    purpleLord = pygame.image.load("assets/images/purple.jpg").convert()
    redLord = pygame.image.load("assets/images/red.jpg").convert()
    lordImage = [yellowLord, blueLord, greenLord, purpleLord, redLord]
    for card in lordImage:
        card.set_alpha(200)
    createViewBoard(window, 5, lordImage, lordsize, 20, 10)

    pygame.display.flip()
     
   
def createViewBoard(window, nbcardFirstLine, rectToBlit, sizeOfRect, vspace, hspace):
    width, height = pygame.display.get_surface().get_size()
    n = nbcardFirstLine
    h = 0
    while n > 0:
        startX = (width/2)- (sizeOfRect[0]*(n/2))
        startY = 200+(h*(hspace+sizeOfRect[1]))
        if(n%2 == 0):
            startX -= (vspace/2)+(vspace*((n/2) -1))
        else:
            startX -= int(n/2)*vspace
        
        for i in range(n):
            index = random.randrange(len(rectToBlit))
            image = rectToBlit[index]
            window.blit(image, (startX+((sizeOfRect[0]+vspace)*i), startY))
        n-=1
        h+=1

    
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    #loadView()
    launchGame()

