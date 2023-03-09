import pygame
import random

BACK = (0, 0 ,0)
WHITE = (225, 225, 225)
pygame.init()
screen = pygame.display.set_mode([1000, 600])
clock = pygame.time.Clock()
done = False
score = 0 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dino_runner/assets/Dino/DinoJump.png")
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310

    def update(self):
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_RIGHT]:
            self.rect.x += 1
        if user_input[pygame.K_LEFT]:
            self.rect.x -= 1

    def draw(self):
        screen.fill(WHITE)
        screen.blit(self.image, self.rect)


class Meteorito(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("dino_runner/assets/Other/meteorito.png")
        self.rect = self.img.get_rect()
        self.i = 0
 
    def update(self):
        self.draw()

    def draw(self):
        for self.i in range(50):
            meteorito = self.img
            meteorito.rect.x = random.randrange(900)
            meteorito.rect.y += 100
            screen.blit(meteorito, meteorito.rect.x, meteorito.rect.y)

    def collazi(self, game):
        if self.img.rect.colliderect(self.image.rect):
          game.playing = False
        