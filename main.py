import sys
import pygame as pg
from pygame.locals import *
import inputs as inp
from loops import *
import renderer as ren



def main():     # put it all together
    pg.init()   # start pygame

    
    while (ren.running):    # while game is running
        loop()      # draw on screen
        inp.check()     # check for any inputs
        display()   # render and display windowd


if __name__ == "__main__":  # when executed
    main()  # run