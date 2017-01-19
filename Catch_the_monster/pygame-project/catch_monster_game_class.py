import pygame
import random
from math import *
import time



KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

HEROSPEED = 5
HEROIMG = 'images/hero.png'
MONSTERSPEED = 5
MONSTERIMG = 'images/monster.png'
GOBLINSPEED = 5
GOBLINIMG = 'images/goblin.png'
SAFEBUFFER = 50

def detectCollision(x1, y1, x2, y2):
    if x1 + 32 < x2:
        return False
    if x2 + 32 < x1:
        return False
    if y1 + 32 < y2:
        return False
    if y2 + 32 < y1:
        return False
    else:
        return True



class Monster(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.speed_x = MONSTERSPEED
        self.speed_y = 0
        self.surface = pygame.image.load(MONSTERIMG).convert_alpha()
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.lastDirectionChange = time.time()

    def setInitialPosition(self, width, height, hero):
        #get hero position and don't place monster within 50 pixels of hero
        min_x = hero.x - SAFEBUFFER
        min_y = hero.y - SAFEBUFFER
        max_x = hero.x + SAFEBUFFER
        max_y = hero.y + SAFEBUFFER

        while safe_x >= min_x and safe_x <= max_x and safe_y >= min_y and safe_y <= max_y
            safe_x = randint(0,width)
            safe_y = randint(0, height)
        self.x = safe_x
        self.y = safe_y
            #placed in safe zone

    def update(self):
        self.move()
        self.checkBoundries(width, height)
        if time.time() - self.lastDirectionChange > 2:
            self.changeDirection()

    def changeDirection(self):
            r = randint(1,4)
            if r == 1:
                self.speed_x = 0
                self.speed_y = MONSTERSPEED
            if r == 2:
                self.speed_x = 0
                self.speed_y = -MONSTERSPEED
            if r == 3:
                self.speed_x = MONSTERSPEED
                self.speed_y = 0
            if r == 4:
                self.speed_x = -MONSTERSPEED
                self.speed_y = 0
            self.lastDirectionChange = time.time()


    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def checkBoundries(self):
        global width, height
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.x = height
        if self.x < width:
            self.x = 0
        if self.y < height:
            self.x = 0

    # def update(self, change, width, height):
    #     if change == 0:
    #         self.speed_x = 0
    #         self.speed_y = -5
    #         if self.y < 0:
    #             self.y = height
    #     elif change == 1:
    #         self.speed_x = 5
    #         if self.x > width:
    #             self.x = 0
    #     elif change == 2:
    #         self.speed_x = 0
    #         self.speed_y = 5
    #         if self.y > height:
    #             self.y = 0
    #     elif change == 3:
    #         self.speed_x = -5
    #         if self.x < 0:
    #             self.x = width
    # def render(self, screen, collisions):
    #     if collisions == False:
    #         screen.blit(self.surface, (self.x, self.y))
    #
    #     else:
    #         # font = pygame.font.Font(None, 25)
    #         # text = font.render('Yay, you win!', True, "black")
    #         # screen.blit(text, (160, 230))
    #         Goblin(100,100)

class Hero(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.speed_x = HEROSPEED
        self.speed_y = HEROSPEED
        self.surface = pygame.image.load(HEROIMG).convert_alpha()
        self.maxspeed = HEROSPEED
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def update(self, width, height, edgeWidth):
        self.move()
        self.checkBoundries(width, height, edgeWidth)

        if time.time() - self.lastDirectionChange > 2:
            self.changeDirection()

    def changeDirection(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def checkBoundries(self):
        global width, height
        if self.speed_x < 0:
            self.x = self.maxspeed
        if self.speed_y < 0:
            self.x + self.width = self.maxspeed
        if self.speed_x < width:
            self.y = -self.maxspeed
        if self.speed_y < height:
            self.y + self.height = -self.maxspeed


class Goblin(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 0

    def render(self, screen):
        goblin_image = pygame.image.load('images/goblin.png').convert_alpha()
        screen.blit(goblin_image, (self.x, self.y))

def CheckCollision(char1,char2):
    return (char1.x + char1.width > char2.x) and (char2.x + char2.width > char1.x) and (char1.y + char1.height > char2.y) and (char2.y + char2.height > char1.y))

def main():
    # declare the size of the canvas
width = 512
height = 480


    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption("Deepak's PY Game")

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background_image = pygame.image.load('images/background.png').convert_alpha()
    # hero_image = pygame.image.load('images/hero.png').convert_alpha()
    # monster_image = pygame.image.load('images/monster.png').convert_alpha()

    hero = Hero(width/2, height/2)
    monster = Monster()
    monster.setInitialPosition(width, height, hero)

    # monster_speed_x = 5
    # monster_speed_y = 0
    change_dir_countdown = 120
    # game loop
    stop_game = False
    game_over = False
    soundPlayed = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    hero.changeDirection(0,hero.maxspeed)
                elif event.key == pygame.K_UP:
                    hero.changeDirection(0,-hero.maxspeed)
                elif event.key == pygame.K_LEFT:
                    hero.changeDirection(-hero.maxspeed,0)
                elif event.key == pygame.K_RIGHT:
                    hero.changeDirection(hero.maxspeed,0)
                elif event.key == pygame.K_RETURN:
                    game_over = False
                    soundPlayed = False
                    monster.setInitialPosition(width, height, hero)
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True



        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        monster.update(width, height)
        hero.update(width, height, 32)

        monster.x += monster.speed_x
        monster.y += monster.speed_y
        if monster.x > width:
            monster.x = 0
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            # change = random.randint(0,3)
            monster.update(random.randint(0,3), width, height)
            change_dir_countdown = 30

        if hero.x < 25:
            hero.x = 25
        if hero.y < 30:
            hero.y = 30
        if hero.x > 450:
            hero.x = 450
        if hero.y > 415:
            hero.y = 415






        # fill background color


        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        monster.update()
        screen.blit(background_image, (0,0))
        collisions = detectCollision(monster.x, monster.y, hero.x, hero.y)
        monster.render(screen, collisions)
        hero.render(screen)
        if not game_over:
            monster.render(screen)
        else:
            #play sound
            if not soundPlayed:
            sound = pygame.mixer.Sound('sounds/win.wav')
            sound.play()
            soundPlayed = True
        if checkCollision(monster, hero):
            game_over = True



        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
