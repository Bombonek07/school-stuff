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
        self.color = random.randint(0, len(self.game.color)-1)

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
            self.color = random.randint(0, len(self.game.color)-1)

    def draw(self):
        pygame.draw.circle(self.game.screen, self.game.color[self.color], (self.x, self.y), self.size)

class game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1920, 1080
        self.snowflakes_amount = 1200
        self.color = self.make_colors()
        self.snowflakes = self.make_snowflakes()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snowfall Screensaver")
        pygame.display.flip()
        self.game_loop()

    def make_snowflakes(self):
        snowflakes = []
        for _ in range(self.snowflakes_amount):
            snowflakes.append(Snowflake(random.randint(0, self.width), random.randint(0, self.height), self))
        return snowflakes

    def make_colors(self):
        color = []
        for _ in range(self.snowflakes_amount):
            color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        return color

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0 , 0, 0))
            self.screen.blit(pygame.image.load("christmas_tree.jpg"), (0,0))

            for snowflake in self.snowflakes:
                snowflake.fall()
                snowflake.draw()

            pygame.display.flip()
            pygame.time.Clock().tick(100)

if __name__ == "__main__":
    game()