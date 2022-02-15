import player as p
import pygame as pg
#import renderer as ren
#import inputs as i

bullets = []
bullet_damage = 10
def shoot():
    bullets.append([[p.user[0][0], p.user[0][1]], [int(p.velocity[0]), int(p.velocity[1])], 0])#p.user[0]])


bursting = False
burst_shots = 0
def burst():
    global bursting, burst_shots
    if bursting:
        do_burst()

def do_burst():
    global bursting, burst_shots
    burst_shots += 1
    if burst_shots % 10 == 0:
        shoot()
        burst_shots = 0
    else:
        bursting = False
            

def shoot_logic():
    burst()


bullet_size = 5
def move_bullet(screen):

    for bullet in bullets:
        bullet[0][0] += int(bullet[1][0] * 10) #int(p.velocity[0])
        bullet[0][1] += int(-bullet[1][1] * 10) #int(p.velocity[0])
        
        #print(bullet)
        #print(bullets)
        pg.draw.rect(screen, (255, 200, 200), [bullet[0][0], bullet[0][1], bullet_size, bullet_size], 0)
        bullet[2] += 1
        if bullet[2] >= 100: # when lifespan is too long, kill
            bullets.remove(bullet)