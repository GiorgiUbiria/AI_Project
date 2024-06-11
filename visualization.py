import matplotlib.pyplot as plt
from maze import Maze
from bfs import bfs
from ids import ids
from astar import astar

# Plot the maze
def plot_maze(maze, path_explored=None, path_solution=None, title="Maze"):
    plt.figure(figsize=(10, 10))
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            # Plot the walls
            if maze[x][y] == 1:
                plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='black')
            else:
                plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='white')

    # Plot the explored path
    if path_explored:
        px, py = zip(*path_explored)
        num_expanded_nodes = len(path_explored)
        plt.plot(py, px, color='blue', linestyle='--', label=f'Expanded {num_expanded_nodes} Nodes')

    # Plot the solution path
    if path_solution:
        px, py = zip(*path_solution)
        plt.plot(py, px, color='red', linewidth=2, label='Solution Path')

    plt.title(title)
    plt.gca().invert_yaxis()

    if path_solution or path_explored:
        plt.legend(loc='upper right')

    plt.show()

# Plot the maze dynamically
def plot_maze_dynamic(maze, path_explored=None, path_solution=None, title="Maze", pause_duration=0.001):  # Further reduced pause_duration
    plt.figure(figsize=(10, 10))
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 1:
                plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='black')
            else:
                plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='white')

    plt.title(title)
    plt.gca().invert_yaxis()

    if path_explored:
        for i in range(len(path_explored)):
            # Plot the explored path dynamically
            px, py = zip(*path_explored[:i+1])
            plt.cla()
            for x in range(len(maze)):
                for y in range(len(maze[0])):
                    if maze[x][y] == 1:
                        plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='black')
                    else:
                        plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='white')
            plt.plot(py, px, color='blue', linestyle='--', label=f'Expanded {i+1} Nodes')
            plt.title(title)
            plt.gca().invert_yaxis()
            plt.draw()
            plt.pause(pause_duration)

    if path_solution:
        px, py = zip(*path_solution)
        plt.cla()
        for x in range(len(maze)):
            for y in range(len(maze[0])):
                if maze[x][y] == 1:
                    plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='black')
                else:
                    plt.fill_between([y, y+1], [x, x], [x+1, x+1], color='white')
        plt.plot(py, px, color='red', linewidth=2, label='Solution Path')
        plt.title(title)
        plt.gca().invert_yaxis()
        plt.draw()
        plt.pause(pause_duration * 5)

    if path_solution or path_explored:
        plt.legend(loc='upper right')

    plt.show()

# Run the visualization process
def run_visualization(maze_width, maze_height, wall_probability, algorithms=['bfs']):
    maze = Maze(maze_width, maze_height, wall_probability)
    maze.generate_maze()
    start = (0, 0)
    goal = (maze_width - 1, maze_height - 1)

    for algorithm in algorithms:
        path = None
        expanded_nodes = None
        title = "Unknown Algorithm"

        if algorithm == 'ids':
            result = ids(maze.maze, start, goal)
            if result[0] is not None:
                path, expanded_nodes, *_ = result
                title = "Solvable Maze with IDS Path"
            else:
                _, expanded_nodes, *_ = result
                title = "Unsolvable Maze with IDS"
        elif algorithm == 'bfs':
            path, expanded_nodes, *_ = bfs(maze.maze, start, goal)
            title = "Solvable Maze with BFS Path" if path else "Unsolvable Maze with BFS"
        elif algorithm == 'astar':
            path, expanded_nodes, *_ = astar(maze.maze, start, goal)
            title = "Solvable Maze with A* Path" if path else "Unsolvable Maze with A*"

        if path is not None and expanded_nodes is not None:
            print(f"{title}:")
            print("  Solved: Yes")
            print(f"  Empirical Avg Expanded Nodes: {len(expanded_nodes)}")
            print(f"  Empirical Avg Max Queue Size: {max(len(queue) for queue in expanded_nodes)}")
        else:
            print(f"{title}:")
            print("  Solved: No")
            print("  Empirical Avg Expanded Nodes: 0")
            print("  Empirical Avg Max Queue Size: 0")

        if isinstance(expanded_nodes, int):
            expanded_nodes = [expanded_nodes]

        plot_maze(maze.maze, path_explored=expanded_nodes, path_solution=path, title=title)
        plot_maze_dynamic(maze.maze, path_explored=expanded_nodes, path_solution=path, title=title)

    return any(path is not None for path, _, _, _ in [bfs(maze.maze, start, goal), ids(maze.maze, start, goal), astar(maze.maze, start, goal)])
