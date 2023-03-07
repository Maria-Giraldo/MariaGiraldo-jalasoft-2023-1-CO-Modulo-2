
import random
from dino_runner.components.obstacles.obstacle import Obstacle



class Ave(Obstacle):
    def __init__(self, image):    
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(200, 320)
        self.stop_index = 0
  
    def draw(self, screen):
        if self.stop_index >=10:
            self.stop_index = 0
        screen.blit(self.image[self.stop_index//5], self.rect)
        self.stop_index +=1

  

        

