import pygame
import random
from random import choice

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.fire import Fire
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import FIRE_TYPE, SHIELD_TYPE, HAMMER_TYPE
class PowerUpManeger:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)
        self.duration = 7
        self.powers = [Shield(), Fire(), Hammer()]


    def generate_power_up(self):
        self.when_appears += random.randint(300, 600)
        power_up = choice(self.powers)
        self.power_ups.append(power_up)

    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True 
                game.player.power_time_up = power_up.start_time + (self.duration*1000)

                if game.player.type  == FIRE_TYPE:
                    pygame.mixer.music.load("dino_runner/assets/sounds/fireSound.mp3")
                    pygame.mixer.music.play() 
                elif game.player.type == SHIELD_TYPE:
                    pygame.mixer.music.load("dino_runner/assets/sounds/soundShield.mp3")
                    pygame.mixer.music.play()                 
                elif game.player.type == HAMMER_TYPE:
                    pygame.mixer.music.load("dino_runner/assets/sounds/hammerSound.mp3")
                    pygame.mixer.music.play()
                self.power_ups.remove(power_up)






    def draw(self, screen):
        for power_ups in self.power_ups: 
            power_ups.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)
    




