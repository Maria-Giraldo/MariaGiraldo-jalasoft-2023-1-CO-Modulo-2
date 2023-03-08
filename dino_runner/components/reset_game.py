import pygame

class Reset_game:
        def __init__(self):
                pass
               
        def reset_game(self, game):      
               game.score.reset_score()
               game.obstacle_manager.reset_obstacles()
               game.game_speed = game.GAME_SPEED