import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, ICON_FINAL
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.counter import Counter
from dino_runner.components.power_ups.power_up_manager import PowerUpManeger
from dino_runner.components.lluvia_meteoritos import Player

class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.power_up_manager = PowerUpManeger()
        self.player_final = Player()
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset_game()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def run_final(self):
        self.playing = True
        while self.playing:
            self.events()
            self.player_final.update()
            self.player_final.draw()
            

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.score.update(self)
        self.update_game_speed()

    def draw(self):
        
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.score.draw(self.screen)
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

        
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count.count == 0 and self.score.count != 1000:
            self.menu.draw(self.screen, 'Press any key to start ...')
        elif self.score.count == 500 and self.playing == False:
                self.menu.draw(self.screen, "¡¡FELICIDADES, HAZ LLEGADO AL FINAL DEL JUEGO!!") 
                self.menu.draw(self.screen, "Para ser campeon debes poder superar la lluvia de meteoritos", half_screen_width, 350) 
                self.menu.draw(self.screen, "press any key to start", half_screen_width, 400)  
                      
        else:
            self.update_highest_score()
            self.menu.draw(self.screen, 'Game over. Press any key to restart')
            self.menu.draw(self.screen, f'Your score: {self.score.count}', half_screen_width, 350, )
            self.menu.draw(self.screen, f'Highest score: {self.highest_score.count}', half_screen_width, 400, )
            self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 450, )

        if self.score.count == 1000:
            self.screen.blit(ICON_FINAL, (half_screen_width - 150, half_screen_height - 250))    
        else:
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))    
        
        self.menu.update(self)
                
    def update_game_speed(self):
        if self.score.count % 200 == 0 and self.game_speed < 500:
            self.game_speed += 5
            
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)
            
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset()
        self.power_up_manager.reset_power_ups()

    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) /1000, 2)
            if time_to_show >=0 :
                self.menu.draw(self.screen, f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 500, 50)
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE




