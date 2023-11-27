import pygame
import sys
import random
import math

pygame.init()

width, height, snowflakes_amount = 1920, 1080, 1200 

screen = pygame.display.set_mode((width, height))       # window size
pygame.display.set_caption("Snowfall Screensaver")      # window name
pygame.display.flip()                                   # sreen refresh

white = ((220, 220, 220),(160,160,180),(100, 100, 120)) # snowflakes colors

snowflakes = [] 

class Snowflake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(1, 3)        # size of the snowflake
        self.wind = random.randint(-1, 1)       # wind direction
        self.color = random.randint(0, 2)       # picks the color of the snowflake

    def fall(self):                             # makes a falling animation
        self.y += self.size
        if self.wind == -1:                     # wind to the left
            self.x += math.sin(self.y/90)       # how much will the win efect the snowflake, depends on size of it
        elif self.wind == 1:                    # wind to the right
            self.x += math.cos(self.y/90)       # how much will the win efect the snowflake, depends on size of it
        if self.y > height:                     # after the random y position on the start:
            self.y = 0                          # sets y to 0, the snowflakes fall from the top
            self.x = random.randint(0, width)   # where does the snowflake spawn on x cord.
            self.size = random.randint(1, 3)    # size of the snowflake
            self.wind = random.randint(-1, 1)   # wind direction
            self.color = random.randint(0, 2)   # picks the color of the snowflake

    def draw(self):
        pygame.draw.circle(screen, white[self.color], (self.x, self.y), self.size)     # makes a round shape

for _ in range(snowflakes_amount):                                                     # generates amount of snowflakes in list 'snowflakes'
    snowflakes.append(Snowflake(random.randint(0, width), random.randint(0, height)))  # at the start in generates them randomly on the screen

while True:                           # main game loop
    for event in pygame.event.get():  # quit
        if event.type == pygame.QUIT: # quit
            pygame.quit()             # quit
            sys.exit()                # quit

    screen.fill((0, 0, 0))            # backgroud

    for snowflake in snowflakes:      # for every snowflake in snowflakes:
        snowflake.fall()              # calls fall to make a falling animation
        snowflake.draw()              # calls draw to make a roud shape

    pygame.display.flip()             # sreen refresh 
    pygame.time.Clock().tick(60)      # time roll