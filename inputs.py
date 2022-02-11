from turtle import Screen
from buttons import primaryActions
from loops import *
#from pygame import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_d, K_w
import pygame as pg
from loops import mx, my, loop, display
import renderer as ren
import sys
import player as p

class check():
    def __init__(self) -> None:
        self.collision_check()

    def collision_check(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ren.running = False
                pg.display.quit()
                sys.exit()
                
            elif event.type == pg.MOUSEBUTTONDOWN:
                if ((mx() > primaryActions.attack[0][0] and my() > primaryActions.attack[0][1]) and (mx() < primaryActions.attack[1][0] and my() < primaryActions.attack[1][1])):
                    print(str(pg.mouse.get_pos()), "success")

                elif event.type == pg.MOUSEBUTTONDOWN:
                    print(pg.mouse.get_pos())

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    p.player.shoot()
            """
            if event.type == pg.:
                if event.key == pg.K_w:
                    p.player.move_up()
                    print("w")
                elif event.key == pg.K_s:
                    p.player.move_down()
                    print("s")
                elif event.key == pg.K_a:
                    p.player.move_left()
                    print("a")
                elif event.key == pg.K_d:
                    p.player.move_right()
                    print("d")
            """
        pressed_keys = pg.key.get_pressed()
       
        if pressed_keys[pg.K_w]:
            p.player.move_up()
            #print("w")
        if pressed_keys[pg.K_s]:
            p.player.move_down()
            #print("s")
        if pressed_keys[pg.K_a]:
            p.player.move_left()
            #print("a")
        if pressed_keys[pg.K_d]:
            p.player.move_right()
            #print("d")
        
        if pressed_keys[pg.K_LSHIFT]:
          if pressed_keys[pg.K_a]:
            p.player.dash_left()
            #print("a")
          if pressed_keys[pg.K_d]:
            p.player.dash_right()

        else:
            #p.velocity = [0.0, 0.0]
            p.dashing = [0.0, 0.0]
            ren.num_dash_particles = 0

        
        
        
        

        #else:
            #pass
                #loop()
                #loop_end()