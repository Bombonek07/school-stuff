import pygame
import sys
import random
import math

class Snowflake:
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
        self.size = random.randint(3, 5)
        self.wind = random.randint(-1, 1)

    def fall(self):
        self.y += self.size
        if self.wind == -1:
            self.x += math.sin(self.y/90)
        elif self.wind == 1:
            self.x += math.cos(self.y/90)           
        if self.y > self.game.height:
            self.y = 0
            self.x = random.randint(0, self.game.width)
            self.size = random.randint(3, 5)
            self.wind = random.randint(-3, 1)

    def draw(self):
        self.game.screen.blit(pygame.image.load("animace/snowflake.png"), (self.x, self.y))

class game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1920, 1080
        self.snowflakes_amount = 100
        self.img = pygame.image.load("animace/snowflake.png")
        self.snowflakes = self.make_snowflakes()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snowfall Screensaver"), (1,1)
        pygame.display.flip()
        self.game_loop()

    def make_snowflakes(self):
        snowflakes = []
        for _ in range(self.snowflakes_amount):
            snowflakes.append(Snowflake(random.randint(0, self.width), random.randint(0, self.height), self))
        return snowflakes

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(pygame.image.load("animace/christmas_tree.jpg"), (0,0))

            for snowflake in self.snowflakes:
                snowflake.fall()
                snowflake.draw()

            pygame.display.flip()
            pygame.time.Clock().tick(120)

if __name__ == "__main__":
    game()