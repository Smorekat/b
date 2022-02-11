
import renderer as ren

# player array:
# [pos [x, y], health]
user = [[0,0], 100]
usersize = [10, 20]
class player():
    def __init__(self):
        pass

    def move_up(user=user):
        user[0][1] -= 1
        print("move_up")

    def move_down(user=user):
        user[0][1] += 1
        print("move_down")

    def move_left(user=user):
        user[0][0] -= 1
        print("move_left")
    
    def move_right(user=user):
        user[0][0] += 1
        print("move_right")

    def dash_right(user=user):
        #ren.particle_dash(user)
        ren.dashing = [1.0, 0.0]
        user[0][0] += 2
