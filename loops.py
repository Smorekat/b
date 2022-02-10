import renderer as ren
import pygame as pg

mainClock = pg.time.Clock()

def display():
    #pg.display.flip()
    pg.display.update()
    mainClock.tick(60)

def loop():
    #ren.screen.fill((0,0,0))
    ren.render()

def mx():
    return pg.mouse.get_pos()[0]

def my():
    return pg.mouse.get_pos()[1]