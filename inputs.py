from turtle import Screen
from buttons import primaryActions
from loops import *
from pygame import QUIT, MOUSEBUTTONDOWN
import pygame as pg
from loops import mx, my, loop, display
import renderer as ren
import sys

class check():
    def __init__(self) -> None:
        self.collision_check()

    def collision_check(self):
        for event in pg.event.get():
            if event.type == QUIT:
                ren.running = False
                pg.display.quit()
                sys.exit()
                
            elif event.type == MOUSEBUTTONDOWN and ((mx() > primaryActions.attack[0][0] and my() > primaryActions.attack[0][1]) and (mx() < primaryActions.attack[1][0] and my() < primaryActions.attack[1][1])):
                print(str(pg.mouse.get_pos()), "success")

            elif event.type == MOUSEBUTTONDOWN:
                print(pg.mouse.get_pos())
            else:
                pass
                #loop()
                #loop_end()