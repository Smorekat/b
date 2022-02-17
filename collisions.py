import pygame as pg
import maps as m
import player as p
import random as rng

def walls():
    # collide = lambda subjectx, subjecty, subjectw, subjecth, objectx, objecty, objectw, objecth: True if (subjectx > objectx and subjecty > objecty) and (subjectx+subjectw < objectx+objectw and subjecty+subjecth < objecty + objecth) else False
    level = []
    m.make_map(level)
    for sector in level:
        # print(level)
        # print(sector)
        # (subjectx > objectx and subjecty > objecty) and (subjectx+subjectw < objectx+objectw and subjecty+subjecth < objecty + objecth)
        # [[block, column], [blockx, blocky, blockw, blockh], [size, color]]
        if (p.user[0][0]+p.user[2][0] > sector[1][0] and p.user[0][1]+p.user[2][1] > sector[1][1]) and (p.user[0][0] < sector[1][0]+sector[1][2] and p.user[0][1] < sector[1][1] + sector[1][3]):
            # p.user[0][0] -= p.velocity[0] + p.user_speed
            # p.user[0][1] -= p.velocity[1] + p.user_speed
            p.user[0][0] += int(-p.velocity[0] * 10) + p.user_speed #int(p.velocity[0])
            p.user[0][1] += int(p.velocity[1] * 10) + p.user_speed #int(p.velocity[0])
            # BUG: Fix collisions for bullets and player w walls
            # TODO: Add enemy pathfinding
            # TODO: document and format code (comment)
            print("u suck ----------------------------------------------------------------", rng.randint(0, 100))
        # else: print("u gud")
        # if user collides with wall, find if x is greater and move w speed and x. refer to opengl/SDL ogltk demo.
        # cycle through /new/ world wall coords.
