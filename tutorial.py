from arena import Arena
from obstacle import Obstacle

global game_arena

game_arena = Arena()

# ------------------------------------------------------------------------------------
# Add your obstacles here!
# Parameter order: name, tuple of coords, color, and radius/length & width
game_arena.add_obstacle(Obstacle("circle", (0, 0), "green", 60))
game_arena.add_obstacle(Obstacle("square", (-200, 200), "green", 60))
game_arena.add_obstacle(Obstacle("rectangle", (0, -200), "red", 60, 100))

game_arena.draw_arena()