import pygame

from dino_runner.components.obstacles.cactus import Cactus_Large, Cactus_Small
from dino_runner.utils.constants import SMALL_CACTUS , LARGE_CACTUS
from dino_runner.components.obstacles.ave import Ave
from dino_runner.utils.constants import BIRD

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        self.large_cactus = False
        self.small_cactus = False
        self.ave = True


         

    def update(self, game):

        if len(self.obstacles) == 0 and self.ave:
                ave = Ave(BIRD)
                self.obstacles.append(ave)
                self.ave = False


        if len(self.obstacles) == 0 and not self.large_cactus:
            cactus = Cactus_Large(LARGE_CACTUS)
            self.obstacles.append(cactus)
            self.large_cactus = True
            self.small_cactus = True
            self.ave = True
            

        elif len(self.obstacles) == 0 and self.small_cactus:
            cactus = Cactus_Small(SMALL_CACTUS)
            self.obstacles.append(cactus)  
            self.large_cactus = False
            self.small_cactus = False
            self.ave = True




        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)   

            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

 




