import renderer as ren
import pygame as pg
import player as p
import bullets as b

mainClock = pg.time.Clock()

def display():
    pg.display.update()
    pg.display.flip()
    mainClock.tick(60)

def loop():
    ren.screen.fill((0,0,0))
    ren.render()
    ren.do_particles()
    b.move_bullet(ren.screen)
    #p.stamina_refill()
    p.stamina_delay()
    #ren.particle_dash()


def mx():
    return pg.mouse.get_pos()[0]

def my():
    return pg.mouse.get_pos()[1]