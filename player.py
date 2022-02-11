
#import renderer as ren
#import math

dashing = [0.0, 0.0]
# player array:
# [pos [x, y], health]
user = [[0,0], 100]
user_size = [10, 20]
user_speed = 2
user_middle = lambda: [user[0][0] + user_size[0] / 2, user[0][1] + user_size[1] / 2]
stamina = 100
class player():
    def __init__(self):
        pass

    def move_up(user=user):
        user[0][1] -= user_speed
        #print("move_up")

    def move_down(user=user):
        user[0][1] += user_speed
        #print("move_down")

    def move_left(user=user):
        user[0][0] -= user_speed
        #print("move_left")
    
    def move_right(user=user):
        user[0][0] += user_speed
        #print("move_right")

    #sinspeed = 0
    #sinlocal = 0.1
    #sinold = 0
    def dash_right(user=user):
        global dashing
        if stamina >= 0:
        #player.sinspeed = player.sinspeed + 0.01 if player.sinspeed <= 2 else player.sinspeed
        #ren.particle_dash(user)
            dashing = [1.0, 0.0]
        
        #player.sinlocal += 0.5
        #player.sinspeed = player.sinlocal if math.sin(player.sinlocal) > player.sinold else 0
        #print(player.sinspeed, (user_speed * (1.5 - math.sin(player.sinspeed/3))))
       # player.sinold = math.sin(player.sinlocal)
            user[0][0] += user_speed * 1.5#(2 - math.sin(player.sinlocal))
        

    def dash_left(user=user):
        global dashing
        #ren.particle_dash(user)
        if stamina >= 0:
            dashing = [-1.0, 0.0]
            user[0][0] -= user_speed * 1.5

stamina_time = 0
def lower_stamina():
    global stamina, stamina_time
    stamina -= 1 if stamina >= 0 else 0
    stamina_delay()
    count() # fix me so it works starting at stamina loss ------------------------------------


stamina_increase = 1

def stamina_refill(stamina_increase=stamina_increase):
    global stamina, refill_stamina
    #if stamina <= 0:
    #    stamina -= 0.01
    #if stamina < -1.2:
    #    stamina = 0
   #     stamina_increase = 0.1
    stamina += stamina_increase if stamina < 100 else 0
    if stamina >= 100:
        refill_stamina = False
    

refill_stamina = False
def stamina_delay():
    global stamina_time, refill_stamina
    # count was here ------------------------------------
    if refill_stamina:
        stamina_refill()

    if stamina_time >= 300:
        refill_stamina = True
        stamina_time = 0
    

def count():
    global stamina_time
    print(stamina_time)
    stamina_time += 1