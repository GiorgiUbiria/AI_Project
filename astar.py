from heapq import heappop, heappush
from maze import Maze
import timeit

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    open_list = []
    heappush(open_list, (0, start, [start]))
    g_costs = {start: 0}
    f_costs = {start: heuristic(start, goal)}
    expanded_nodes = []

    while open_list:
        _, current, path = heappop(open_list)
        expanded_nodes.append(current)

        if current == goal:
            return path, expanded_nodes

        for neighbor in get_neighbors(maze, current):
            tentative_g_cost = g_costs[current] + 1
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_costs[neighbor] = tentative_g_cost + heuristic(neighbor, goal)
                heappush(open_list, (f_costs[neighbor], neighbor, path + [neighbor]))

    return None, expanded_nodes

def get_neighbors(maze, vertex):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    x, y = vertex
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def simulate_astar(maze_width, maze_height, num_simulations):
    total_time = 0
    solved_count = 0

    for _ in range(num_simulations):
        maze = Maze(maze_width, maze_height)
        maze.generate_maze()
        start = (0, 0)
        goal = (maze_width - 1, maze_height - 1)

        timer = timeit.Timer(lambda: astar(maze.maze, start, goal))
        exec_time = timer.timeit(number=1)

        path, _ = astar(maze.maze, start, goal)
        total_time += exec_time
        if path is not None:
            solved_count += 1

    if solved_count == 0:
        return float('inf'), 0
    avg_time = total_time / solved_count
    return avg_time, solved_count
