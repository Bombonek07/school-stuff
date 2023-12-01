import pygame
import sys
import random
import math

class Snowflake:
    def __init__(self, x, y, game):
        self.vlocka = ["animace/snowflake.png", "animace/snowflake1.png"]
        self.x = x
        self.y = y
        self.game = game
        self.img = pygame.image.load(random.choice(self.vlocka))

        self.random = random.randint(1, 500)
        if self.random == 1:
            self.size = 200
        elif self.random == 2:
            self.size = 150
        elif self.random == (3 or 4 or 5):
            self.size = 125
        elif self.random == (6 or 7 or 8):
            self.size = 100
        else:
            self.size = random.randint(5, 60)
        
        self.wind = random.randint(-1, 1)
        if self.size < 30:
            self.img = pygame.image.load("animace/snowflake_blor.png")
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        self.deg = random.randint(0, 90)
        self.rotate_img = pygame.transform.rotate(self.img, self.deg)

    def fall(self):
        self.deg2 = random.randint(-1,1)
        self.rotate_img = pygame.transform.rotate(self.img, (self.deg+self.deg2))

        if self.size < 20:
            self.y += self.size / 20
        elif self.size < 40:
            self.y += self.size / 15
        elif self.size >= 40:
            self.y += self.size / 11
        elif self.size >= 50:
            self.y += self.size / 10.5
        elif self.size >= 100:
            self.y += self.size / 10
        elif self.size >= 200:
            self.y += self.size / 9.9
        if self.wind == -1:
            self.x += math.sin(self.y/90)
        elif self.wind == 1:
            self.x += math.cos(self.y/90)          
        if self.y > self.game.height:
            self.y = -200
            self.x = random.randint(-100, self.game.width+100)
            self.wind = random.randint(-1, 1)
            
            self.random = random.randint(1, 500)
            if self.random == 1:
                self.size = 200
            elif self.random == 2:
                self.size = 150
            elif self.random == (3 or 4 or 5):
                self.size = 125
            elif self.random == (6 or 7 or 8):
                self.size = 100
            else:
                self.size = random.randint(5, 60)
            
            if self.size < 30:
                self.img = pygame.image.load("animace/snowflake_blor.png")
            else:
                self.img = pygame.image.load(random.choice(self.vlocka))
            self.img = pygame.transform.scale(self.img, (self.size, self.size))

    def draw(self):
        self.game.screen.blit(self.rotate_img, (self.x, self.y))

class game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1920, 1080
        self.snowflakes_amount = 300
        self.snowflakes = self.make_snowflakes()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snowfall Screensaver"), (1,1)
        pygame.display.flip()
        self.game_loop()

    def make_snowflakes(self):
        snowflakes = []
        for _ in range(self.snowflakes_amount):
            snowflakes.append(Snowflake(random.randint(-200, self.width+200), random.randint(-200, self.height), self))
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
            pygame.time.Clock().tick(50)

if __name__ == "__main__":
    game()