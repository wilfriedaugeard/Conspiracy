import pygame, time
from Model.Game.game import Game  
from Controller import Controller
from View.view import View
from moviepy.editor import VideoFileClip 

def launchGame():
    # Load view and initialize it
    view = View(1920, 1050, "assets/images/background.jpg")
    view.loadGame()

    # Load controller and run it
    controller = Controller.gameController(view)
    controller.run()
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    launchGame()
    

