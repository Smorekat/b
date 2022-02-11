import player as p
import pygame as pg
#import renderer as ren

bullets = []
def shoot():
    bullets.append([[p.user[0][0], p.user[0][1]], [int(p.velocity[0]), int(p.velocity[1])], 0])#p.user[0]])
    

def move_bullet(screen):

    for bullet in bullets:
        bullet[0][0] += int(bullet[1][0] * 10) #int(p.velocity[0])
        #print(bullet)
        #print(bullets)
        pg.draw.rect(screen, (255, 200, 200), [bullet[0][0], bullet[0][1], 5, 5], 0)
        bullet[2] += 1
        if bullet[2] >= 100: # when lifespan is too long, kill
            bullets.remove(bullet)