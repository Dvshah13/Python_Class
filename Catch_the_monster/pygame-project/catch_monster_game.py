import pygame
import random


def update(self, change, width, height):
    if change == 0:
        self.speed_x = 0
        self.speed_y = -5
        if self.y < 0:
            self.y = 480
        if self.y > height:
            self.speed_y = -5
        if self.x < 0:
            self.speed_x = 5
        if self.x > width:
            self.speed_x = -5
    elif change == 1:
        self.speed_x = 5
        if self.x < 0:
            self.speed_x = 5
        if self.x > width:
            self.speed_x = -5
    elif change == 2:
        self.speed_x = 0
        self.speed_y = 5
        if self.y < 0:
            self.speed_y = 5
        if self.y > height:
            self.speed_y = -5
        if self.x < 0:
            self.speed_x = 5
        if self.x > width:
            self.speed_x = -5
    elif change == 3:
        self.speed_x = -5
        if self.x < 0:
            self.speed_x = 5
        if self.x > width:
            self.speed_x = -5
        if self.y < 0:
            self.speed_y = 5
        if self.y > height:
            self.speed_y = -5
# class Monster(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.speed_x = 5
#         self.speed_y = 5
#
#     def update(self, width, height):
#         self.x += self.speed_x
#         self.y += self.speed_y
#         if self.x > width:
#             self.speed_x = -5
#         if self.y > height:
#             self.speed_y = -5
#         if self.x < 0:
#             self.speed_x = 5
#         if self.y < 0:
#             self.speed_y = 5

def main():
    # declare the size of the canvas
    width = 510
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
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    monster_x = 100
    monster_y = 100
    monster_speed_x = 5
    monster_speed_y = 0
    change_dir_countdown = 120
    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        monster_x += monster_speed_x
        monster_y += monster_speed_y
        if monster_x > width:
            monster_x = 0
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change = random.randint(0,3)
            if change == 0:
                monster_speed_x = 0
                monster_speed_y = -5
                if monster_y < 0:
                    monster_speed_y = 5
                if monster_y > height:
                    monster_speed_y = -5
            elif change == 1:
                monster_speed_x = 5
                if monster_x < 0:
                    monster_speed_x = 5
                if monster_x > width:
                    monster_speed_x = -5
            elif change == 2:
                monster_speed_x = 0
                monster_speed_y = 5
                if monster_y < 0:
                    monster_speed_y = 5
                if monster_y > height:
                    monster_speed_y = -5
            elif change == 3:
                monster_speed_x = -5
                if monster_x < 0:
                    monster_speed_x = 5
                if monster_x > width:
                    monster_speed_x = -5


        # fill background color


        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        screen.blit(background_image, (0,0))
        screen.blit(hero_image, (235,225))
        screen.blit(monster_image, (monster_x, monster_y))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
