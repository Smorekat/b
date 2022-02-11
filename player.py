
#import renderer as ren
#import math
import bullets as b

dashing = [0.0, 0.0]
# player array:
# [pos [x, y], health]
health = 100
user = [[0,0], health]
user_size = [10, 20]
user_speed = 2
user_middle = lambda: [user[0][0] + user_size[0] / 2, user[0][1] + user_size[1] / 2]
stamina = 100
velocity = [0.0, 0.0]

class player():
    def __init__(self):
        pass

    def move_up(user=user):
        global velocity
        user[0][1] -= user_speed
        velocity = [0.0, 1.0]
        #print("move_up")

    def move_down(user=user):
        global velocity
        user[0][1] += user_speed
        velocity = [0.0, -1.0]
        #print("move_down")

    def move_left(user=user):
        global velocity
        user[0][0] -= user_speed
        velocity = [-1.0, 0.0]
        #print("move_left")
    
    def move_right(user=user):
        global velocity
        user[0][0] += user_speed
        velocity = [1.0, 0.0]
        #print("move_right")

    #sinspeed = 0
    #sinlocal = 0.1
    #sinold = 0
    def dash_right(user=user):
        global dashing
        if stamina > 0:
            dashing = [1.0, 0.0]
            user[0][0] += user_speed * 1.5
        #if stamina >= 0:
        #player.sinspeed = player.sinspeed + 0.01 if player.sinspeed <= 2 else player.sinspeed
        #ren.particle_dash(user)
            #dashing = [1.0, 0.0]
        
        #player.sinlocal += 0.5
        #player.sinspeed = player.sinlocal if math.sin(player.sinlocal) > player.sinold else 0
        #print(player.sinspeed, (user_speed * (1.5 - math.sin(player.sinspeed/3))))
       # player.sinold = math.sin(player.sinlocal)
            #user[0][0] += user_speed * 1.5#(2 - math.sin(player.sinlocal))
        

    def dash_left(user=user):
        global dashing
        if stamina > 0:
            dashing = [-1.0, 0.0]
            user[0][0] -= user_speed * 1.5



    def shoot():
        b.shoot()
        #else: stamina_refill()

stamina_time = 0
do_count = False
def lower_stamina():
    global stamina, stamina_time, refill_stamina, do_count
    if stamina > 0:
        stamina -= 1
        do_count = True
        stamina_time = 0
        #removing_stamina = True
        #refill_stamina = True
        #count()
    stamina_delay()


stamina_increase = 1

def stamina_refill(stamina_increase=stamina_increase):
    global stamina, refill_stamina, stamina_time
    #if stamina <= 0:
    #    stamina -= 0.01
    #if stamina < -1.2:
    #    stamina = 0
   #     stamina_increase = 0.1
    #if stamina <= 0:
    #count() # fix me so it works starting at stamina loss ------------------------------------

    if dashing != [0.0, 0.0]: 
        stamina_time = 0
        refill_stamina = False

    if refill_stamina and stamina <= 100 and dashing == [0.0, 0.0]:
        stamina += stamina_increase
        
    elif refill_stamina and stamina >= 100:
        refill_stamina = False

    
    
        #stamina_time = 0    -- problems with count setting to 0
    

refill_stamina = False
def stamina_delay():
    global stamina_time, refill_stamina, do_count
    # count was here ------------------------------------
    # and dashing == [0.0, 0.0]
    if do_count : count()
    if stamina_time >= 100:
        refill_stamina = True #if dashing == [0.0, 0.0] else False
        stamina_time = 0
        do_count = False
    stamina_refill()
    

def count():
    global stamina_time
    print("c ", stamina_time)
    stamina_time += 1