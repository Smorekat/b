from matplotlib.cbook import sanitize_sequence
from buttons import *
import pygame as pg
import random as rng
#import loops as lp
from pygame.locals import DOUBLEBUF
import player as p
import enemy as e
import maps as m
#import bullets as b

size = width, height = (500, 500)   # set window/screen dimensions
screen = pg.display.set_mode(size,DOUBLEBUF,32)  # make screen
icon = pg.image.load("./img/cot.jpeg")  # import icon 
pg.display.set_icon(icon)   # set icon
running = True  # set game to run



class render(): # rendering functions class
    def __init__(self): # render things
        self.load_map()
        
        #self.particle_test()
        self.show_player()
        self.ui()   # draw ui (buttons)

        e.enemy_health_logic(screen)  # not sure why but have this in render

        

    def ui(self):   # draw buttons
        # primaryActions(screen)  # draw primary buttons
        statistics(screen)
    #particles = []

    def show_player(self):
        
        pg.draw.rect(screen, (200, 255, 100), 
                        [p.user[0][0], p.user[0][1],
                         p.user_size[0], p.user_size[1]])  # p.usersize[0], p.user[0][1] + p.usersize[1]])

    def show_enemies(self):
        pass  # fix
        # pg.draw.rect(screen, (e.red, e.green, 20), [enemy[0][0], enemy[0][1], enemy_size[0], enemy_size[1]], 0)
    def load_map(self):
      level = m.load_map(0)   # temp 
      current_column = 0
      ratio = 10
      parsed_map = []

      size = 0  # (height / width) * (ratio * 10)
      blockw = 0  # size
      blockh = 0  # blockw
      blockx = 0  # (width / len(column)) * current_block
      blocky = 0  # (height / len(column)) * current_column
      color = (255, 0, 0)# (100, 100, 100)
      for column in level:
        
        # print(column)
        current_block = 0
        for block in column:
            # print(block)
            
            
            # print(height/width)
            if block != 0:
                
                size = (height / width) * (ratio * 10)
                blockw = size
                blockh = blockw
                blockx = (width / len(column)) * current_block
                blocky = (height / len(column)) * current_column
                color = (100, 100, 100)
                pg.draw.rect(screen, color, [blockx, blocky, blockw, blockh])

                # print(blockx, blocky)
            parsed_map.append([[block, column], [blockx, blocky, blockw, blockh], [size, color]])
            current_block += 1
        current_column += 1

# dashing = [0.0, 0.0]
particles = []
num_dash_particles = 0

def particle_dash():
  global num_dash_particles
  # print(dashing)
                                              #[0][0]startx    [0][1]starty   [1][0]velocityx          [1][1]velocityy       [2]size
  if p.dashing != [0.0, 0.0]:
    p.lower_stamina()

    print(p.stamina)
    if num_dash_particles <= 5:
        particles.append([[p.user_middle()[0], p.user_middle()[1]], [rng.randint(0, 20) / 7 - 1, -2], rng.randint(4, 6), [rng.randint(100, 255), rng.randint(100, 255), rng.randint(100, 255)]])
        num_dash_particles += 1
    else: 
        pass
      #dashing = [0.0, 0.0]
  for particle in particles:
    particle[0][0] += particle[1][0]  # x + velocity
    particle[0][1] += particle[1][1]  # y + velocity
    particle[2] -= 0.1      # decay
    particle[1][1] += 0.1   # y velocity
    def delta_particle(pos):
      delta_speed = 0.1
      delta = -delta_speed if p.dashing[pos] > 0.0 else 0
      delta = delta_speed if p.dashing[pos] < 0.0 else 0
      return delta
    particle[1][0] -= delta_particle(0)   # x velocity
    particle[1][0] -= delta_particle(1)   # x velocity
    
    pg.draw.circle(screen, (particle[3]), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
    if particle[2] <= 0:
      particles.remove(particle)
  #dashing = [0.0, 0.0]
          
    

"""
    def particle_test(self):
        
        # screen.fill((0,0,0))
        mx, my = pg.mouse.get_pos()
        self.particles.append([[mx, my], [rng.randint(0, 20) / 10 - 1, -2], rng.randint(4, 6)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.05
            pg.draw.circle(screen, (rng.randint(100, 255), rng.randint(100, 255), rng.randint(100, 255)), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)
"""

def do_particles():
  #global num_dash_particles
  #num_dash_particles = 0
  particle_dash()