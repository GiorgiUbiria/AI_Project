import random

class Maze:
    # Maze initialization with width, height and wall probability
    def __init__(self, width, height, wall_probability=0.3):
        self.width = width
        self.height = height
        self.wall_probability = wall_probability
        # Initialize 2D Matrix of 0s (Empty maze)
        self.maze = [[0 for _ in range(height)] for _ in range(width)]
        
    # Maze generation method
    def generate_maze(self):
        for i in range(self.width):
            for j in range(self.height):
                # Randomly set walls
                if random.random() < self.wall_probability:
                    self.maze[i][j] = 1
        # Open start and end points
        self.maze[0][0] = 0
        self.maze[self.width - 1][self.height - 1] = 0
