import pygame, time
from Model.Game.game import Game  
from Controller import Controller
from View.view import View
from moviepy.editor import VideoFileClip 

def launchGame():
    view = View(1920, 1050, "assets/images/background.jpg")
    view.loadGame()
    game = Game(view)
    if(not game.loadAnimation()):
        print("quit animation")
        game.view.clean()
        return 
    
    game.mainMenu()
    #time.sleep(2)
    #game.playParty()
    

def launchVideo():
    pygame.display.set_caption('video')
    clip = VideoFileClip('assets/videos/animation2D.mp4') 
    clip.preview() 
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    launchGame()
    

