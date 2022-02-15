import pygame as pg
import player as p

class primaryActions(): # draw primary buttons
    def __init__(self, screen): # draw buttons
        self.btn_attack(screen) # draw attack button
        #self.fps(screen)
    
    # first button coordinates
    attack = [[50,50], []]
    #attackpos1 = (50,50)
    attacklength = (100, 50)
    attack[1] = [attack[0][0]+attacklength[0], attack[0][1]+attacklength[1]]
    
    def btn_attack(self, screen):   # draw attack button

        pg.draw.rect(screen, (0, 0, 255),   # draw button frame
                [self.attack[0], self.attacklength]) # on screen, color Blue, x1;y1;lx;ly

    def fps(self, screen):
        #sysfont = pg.font.get_default_font()

        font = pg.font.SysFont(None, 48)
        clock = pg.time.Clock()
        img = font.render(str(clock.get_fps()), True, (255, 255, 255))
        screen.blit(img, (20, 20))

class statistics():
    def __init__(self, screen):
        self.stamina_bar(screen)
        self.health_bar(screen)

    def stamina_bar(self, screen):
        pg.draw.rect(screen, (150, 100, 0), [[350, 450], [110, 20]], 5)

        #print("st" + str(p.stamina))
        pg.draw.rect(screen, (0, 0, 255), [[355,455], [p.stamina, 10]], 0)

    def health_bar(self, screen):
        pg.draw.rect(screen, (150, 100, 0), [[350, 430], [110, 20]], 5)

        #print("st" + str(p.stamina))
        pg.draw.rect(screen, (255, 0, 20), [[355,435], [p.health, 10]], 0)