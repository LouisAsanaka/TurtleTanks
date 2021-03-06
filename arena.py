from builder import Builder

from constants import *

class Arena:
    
    def __init__(self):
        self.obstacles = []
        self.builder = Builder()
        
    def get_obstacles(self):
        return self.obstacles
        
    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)
            
    def draw_arena(self):
        self.builder.draw_arena_outline()
        for obstacle in self.obstacles:
            self.builder.draw_shape(obstacle)