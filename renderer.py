from buttons import *
import pygame as pg
import random as rng
import loops as lp

size = width, height = (500, 500)   # set window/screen dimensions
screen = pg.display.set_mode(size,0,32)  # make screen
icon = pg.image.load("./img/cot.jpeg")  # import icon 
pg.display.set_icon(icon)   # set icon
running = True  # set game to run

class render(): # rendering functions class
    def __init__(self): # render things
        #self.ui()   # draw ui (buttons)
        self.particle_test()

    def ui(self):   # draw buttons
        primaryActions(screen)  # draw primary buttons

    particles = []

    def particle_test(self):
        
        screen.fill((0,0,0))
        mx, my = pg.mouse.get_pos()
        self.particles.append([[mx, my], [rng.randint(0, 20) / 10 - 1, -2], rng.randint(4, 6)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.01
            particle[1][1] += 0.05
            pg.draw.circle(screen, (rng.randint(100, 255), rng.randint(100, 255), rng.randint(100, 255)), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)
