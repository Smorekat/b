
#import renderer as ren
#import math
import bullets as b
import pygame as pg # only 1 / once
import collisions as c


dashing = [0.0, 0.0]
# player array:
# [pos [x, y], health]
health = 100
user_size = [10, 20]
user = [[0,0], health, user_size]  # TODO: use new in-user size, not independent var
user_speed = 2
user_middle = lambda: [user[0][0] + user_size[0] / 2, user[0][1] + user_size[1] / 2]
stamina = 100
velocity = [0.0, 0.0] 

class player():
    def __init__(self):
        pass

    def move_up(user=user):
        global velocity
        velocity[1] = 1.0 # may be problematic ------
        user[0][1] -= user_speed if not c.is_colliding else 0
        

    def move_down(user=user):
        global velocity
        velocity[1] = -1.0
        user[0][1] += user_speed if not c.is_colliding else 0

    def move_left(user=user):
        global velocity
        velocity[0] = -1.0
        user[0][0] -= user_speed if not c.is_colliding else 0
        
    
    def move_right(user=user):
        global velocity
        velocity[0] = 1.0
        user[0][0] += user_speed if not c.is_colliding else 0  # user_speed if c.is_colliding != velocity else 0
        

    def dash_right(user=user):
        global dashing
        if stamina > 0:
            dashing = [1.0, 0.0]
            user[0][0] += user_speed * 1.5

    def dash_left(user=user):
        global dashing
        if stamina > 0:
            dashing = [-1.0, 0.0]
            user[0][0] -= user_speed * 1.5

    def shoot():
        b.shoot()

    def burst():
        b.burst()


stamina_time = 0
do_count = False
def lower_stamina():
    global stamina, stamina_time, refill_stamina, do_count
    if stamina > 0:
        stamina -= 1
        do_count = True
        stamina_time = 0
    stamina_delay()

stamina_increase = 1
def stamina_refill(stamina_increase=stamina_increase):
    global stamina, refill_stamina, stamina_time
    if dashing != [0.0, 0.0]: 
        stamina_time = 0
        refill_stamina = False

    if refill_stamina and stamina <= 100 and dashing == [0.0, 0.0]:
        stamina += stamina_increase
        
    elif refill_stamina and stamina >= 100:
        refill_stamina = False

refill_stamina = False
def stamina_delay():
    global stamina_time, refill_stamina, do_count
    if do_count : count()
    if stamina_time >= 100:
        refill_stamina = True
        stamina_time = 0
        do_count = False
    stamina_refill()
    
def count():
    global stamina_time
    print("c ", stamina_time)
    stamina_time += 1

