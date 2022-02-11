
import renderer as ren

# player array:
# [pos [x, y], health]
user = [[0,0], 100]
user_size = [10, 20]
user_speed = 3
user_middle = lambda: [user[0][0] + user_size[0] / 2, user[0][1] + user_size[1] / 2]
class player():
    def __init__(self):
        pass

    def move_up(user=user):
        user[0][1] -= user_speed
        print("move_up")

    def move_down(user=user):
        user[0][1] += user_speed
        print("move_down")

    def move_left(user=user):
        user[0][0] -= user_speed
        print("move_left")
    
    def move_right(user=user):
        user[0][0] += user_speed
        print("move_right")

    def dash_right(user=user):
        #ren.particle_dash(user)
        ren.dashing = [1.0, 0.0]
        user[0][0] += user_speed * 1.5

    def dash_left(user=user):
        #ren.particle_dash(user)
        ren.dashing = [-1.0, 0.0]
        user[0][0] -= user_speed * 1.5
