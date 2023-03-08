import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING_BOY, JUMPING_BOY, DUCKING_BOY


class Dinosaur(Sprite):
    X_POST = 80
    Y_POST = 310 
    JUMP_SPEED = 8.5 
    DUCK_SPEED = 6.5   

    def __init__(self):
        self.image = RUNNING_BOY[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POST
        self.dino_rect.y = self.Y_POST
        self.stop_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        self.dino_duck = False
        self.duck_speed = self.DUCK_SPEED

        
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()    

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif user_input[pygame.K_DOWN] and not self.dino_duck:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False 
            self.dino_duck = False   

        if self.stop_index >=10:
            self.stop_index = 0
    def run(self):
        self.image = RUNNING_BOY[0] if self.stop_index // 5 else RUNNING_BOY[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POST
        self.dino_rect.y = self.Y_POST
        self.stop_index += 1

    def jump(self):
        self.image = JUMPING_BOY
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POST
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED
    def duck(self):
        self.image = DUCKING_BOY[0] if self.stop_index // 5 else DUCKING_BOY[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POST
        self.dino_rect.y = 350
        self.stop_index += 1
        self.duck_speed -=0.8

        if self.duck_speed < -self.DUCK_SPEED:
            self.dino_rect.y = self.Y_POST
            self.dino_duck = False
            self.duck_speed = self.DUCK_SPEED 
    def draw(self, screen):  
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y) )


