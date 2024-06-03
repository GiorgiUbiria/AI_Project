import random

class Maze:
    def __init__(self, width, height, wall_probability=0.3):
        self.width = width
        self.height = height
        self.wall_probability = wall_probability
        self.maze = [[0 for _ in range(height)] for _ in range(width)]
        
    def generate_maze(self):
        for i in range(self.width):
            for j in range(self.height):
                if random.random() < self.wall_probability:
                    self.maze[i][j] = 1
        self.maze[0][0] = 0
        self.maze[self.width - 1][self.height - 1] = 0
