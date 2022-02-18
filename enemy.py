import pygame as pg
import bullets as b
import random as rng
import collisions as c

 
#mainClock = pg.time.Clock()
enemies = []
enemy_size = [15,30]
def spawn():
    enemies.append([[rng.randint(100,400), rng.randint(100, 400)], 100])
    
    
def enemy_health_logic(screen):
    red = 0
    green = 0
    for enemy in enemies:

        for bullet in b.bullets:
            #((mx() > primaryActions.attack[0][0] and my() > primaryActions.attack[0][1]) and (mx() < primaryActions.attack[1][0] and my() < primaryActions.attack[1][1])):
            #[p.user[0][0], p.user[0][1]], [int(p.velocity[0]), int(p.velocity[1])], 0])#p.user[0]
            if (bullet[0][0]+b.bullet_size > enemy[0][0] and bullet[0][1]+b.bullet_size > enemy[0][1]) and (bullet[0][0] < enemy[0][0]+enemy_size[0] and bullet[0][1] < enemy[0][1]+enemy_size[1]):
# c.collision_alg(bullet[0][0], bullet[1][1], b.bullet_size, b.bullet_size, enemy[0][0], enemy[0][1], enemy_size[0], enemy_size[1])): #bullet[0][0] > enemy[0][0] and bullet[0][1] > enemy[0][1]) and (bullet[0][0]+b.bullet_size < enemy[0][0]+enemy_size[0] and bullet[0][1]+b.bullet_size < enemy[0][1]+enemy_size[1]):
                enemy[1] -= b.bullet_damage
                b.bullets.remove(bullet)
                if enemy[1] <= 0:
                    enemies.remove(enemy)
        
        red = 255 - enemy[1] if red >= 0 and red <= 255 else 0
        green = 0 + enemy[1] if green <= 255 and green >= 0 else 0
        # print(red, green)
        pg.draw.rect(screen, (red, green, 20), [enemy[0][0], enemy[0][1], enemy_size[0], enemy_size[1]], 0)
        
