import player as p
import pygame as pg
#import renderer as ren
#import inputs as i

bullets = []
bullet_damage = 10





# p.velocity
class shoot():
    def __init__(self):
        self.do()

    old_velocity = [0.0, 0.0]   # FIXME
    def do(self):
        print(self.old_velocity)
        bullets.append([[p.user[0][0], p.user[0][1]], [int(self.old_velocity[0]), int(self.old_velocity[1])], 0])#p.user[0]])


bursting = False
burst_shots = 0
clock = 0.0 #pg.time.get_ticks()     # first use of pygame clock instead of loop + variable counter
burst_delay = 0.0

def set_delay():
    global clock, burst_delay
    #clock = pg.time.get_ticks()     # first use of pygame clock instead of loop + variable counter\
    burst_delay = clock + 50

def burst():
    global burst_shots, burst_delay, clock, bursting
    set_delay()
    print("bursted")
    
    #print(burst_delay, clock, bursting, burst_shots)




def do_burst():
    global bursting, burst_shots
    burst_shots += 1
    if burst_shots < 5:
        shoot()
    
    elif burst_shots > 5:
        bursting = False
        burst_shots = 0
        
            

def shoot_logic():
    global burst_delay, clock, bursting, burst_shots
    clock = pg.time.get_ticks()
    if clock > burst_delay and bursting == True:
        print(burst_delay, clock, bursting, burst_shots)
        do_burst()
        set_delay()


# BUG: Fix crippled bullets

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