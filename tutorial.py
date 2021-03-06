from arena import Arena
from obstacle import Obstacle

global game_arena

game_arena = Arena()

# ------------------------------------------------------------------------------------
# Add your obstacles here!
# Order: name, list of coords, color, and radius/length & width
green_circle = Obstacle("circle", [0, 0], "green", 60)
game_arena.add_obstacle(green_circle)

green_square = Obstacle("square", [-200, 200], "green", 60)
game_arena.add_obstacle(green_square)

red_rectangle = Obstacle("rectangle", [0, -200], "red", 60, 100)
game_arena.add_obstacle(red_rectangle)

game_arena.draw_arena()