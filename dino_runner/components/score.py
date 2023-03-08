import pygame
from dino_runner.utils.constants import FONT_STYLE

class Score:
    
    lista_score= []

    def __init__(self):
       self.score = 0

    def update_score(self, game):
        self.score += 1 
        self.lista_score.append(self.score) 
        

        if self.score % 200 == 0 and game.game_speed < 500:
            game.game_speed += 5
            game.x_pos_bg -= game.game_speed

    def draw_score(self, screen):

        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)

    def reset_score(self):
        self.score = 0
