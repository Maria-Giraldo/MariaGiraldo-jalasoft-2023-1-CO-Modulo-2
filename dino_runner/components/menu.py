import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.components.score import Score

class Menu:
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2 

     
    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height )
        self.scores = Score.lista_score
    



    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)
        

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def resent_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()
    
    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def numero_muertes(self, game, screen):
        font = pygame.font.Font(FONT_STYLE, 20)
        text_muertes = font.render(f"MUERTES: {game.death_count}", True, (0, 0, 0))
        text_muertes_rect = text_muertes.get_rect()
        text_muertes_rect.center = (500, 350)
        screen.blit(text_muertes, text_muertes_rect)

    def score_partida(self, screen): 
        font = pygame.font.Font(FONT_STYLE, 20)
        text_score = font.render(f"SCORE {self.scores[-1]}", True, (0, 0, 0))
        text_score_rect = text_score.get_rect()
        text_score_rect.center = (500, 400)  
        screen.blit(text_score, text_score_rect) 

    def score_maximo(self, screen):
        font = pygame.font.Font(FONT_STYLE, 20)
        text_maximo_score = font.render(f"MAXIMO SCORE: {max(self.scores)}", True, (0, 0, 0))
        text_maximo_score_rect = text_maximo_score.get_rect()
        text_maximo_score_rect.center = (500, 450)
        screen.blit(text_maximo_score, text_maximo_score_rect)
        

