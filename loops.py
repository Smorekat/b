import renderer as ren
import pygame as pg
import player as p

mainClock = pg.time.Clock()

def display():
    pg.display.update()
    pg.display.flip()
    mainClock.tick(60)

def loop():
    ren.screen.fill((0,0,0))
    ren.render()
    ren.do_particles()
    #p.stamina_refill()
    p.stamina_delay()
    #ren.particle_dash()


def mx():
    return pg.mouse.get_pos()[0]

def my():
    return pg.mouse.get_pos()[1]