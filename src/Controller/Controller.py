import pygame 
from pygame.locals import *

def controllerTick():
    #Handle Input Events
    for event in pygame.event.get():
        if event.type == QUIT:
            return 0
        elif event.type == MOUSEBUTTONDOWN:
            print("click")
        elif event.type is MOUSEBUTTONUP:
            print("unclick")
    return 1


def viewTick():
    print("")