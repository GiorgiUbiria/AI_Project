import matplotlib.pyplot as plt
from maze import Maze
from bfs import bfs
from ids import ids
from astar import astar

def plot_maze(maze, path_explored=None, path_solution=None, title="Maze"):
    plt.figure(figsize=(10, 10))
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 1:
                plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='black')
            else:
                plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='white')

    if path_explored:
        px, py = zip(*path_explored)
        num_expanded_nodes = len(path_explored)
        plt.plot(py, px, color='blue', linestyle='--', label=f'Expanded {num_expanded_nodes} Nodes')

    if path_solution:
        px, py = zip(*path_solution)
        plt.plot(py, px, color='red', linewidth=2, label='Solution Path')

    plt.title(title)
    plt.gca().invert_yaxis()

    if path_solution or path_explored:
        plt.legend(loc='upper right')

    plt.show()

def run_visualization(maze_width, maze_height, wall_probability=0.3, algorithm='bfs', max_depth=None):
    maze = Maze(maze_width, maze_height, wall_probability)
    maze.generate_maze()
    start = (0, 0)
    goal = (maze_width - 1, maze_height - 1)

    path = None
    expanded_nodes = None
    title = "Unknown Algorithm"

    if algorithm == 'ids':
        path, expanded_nodes = ids(maze.maze, start, goal, max_depth)
        title = "Solvable Maze with IDS Path" if path else "Unsolvable Maze with IDS"
    elif algorithm == 'bfs':
        path, expanded_nodes = bfs(maze.maze, start, goal)
        title = "Solvable Maze with BFS Path" if path else "Unsolvable Maze with BFS"
    elif algorithm == 'astar':
        path, expanded_nodes = astar(maze.maze, start, goal)
        title = "Solvable Maze with A* Path" if path else "Unsolvable Maze with A*"

    if isinstance(expanded_nodes, int):
        expanded_nodes = [expanded_nodes]

    plot_maze(maze.maze, path_explored=expanded_nodes, path_solution=path, title=title)
    return path is not None

