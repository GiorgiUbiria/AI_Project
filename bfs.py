from collections import deque
from maze import Maze
import timeit

def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    expanded_nodes = []
    
    while queue:
        (vertex, path) = queue.popleft()
        expanded_nodes.append(vertex)
        if vertex == goal:
            return path, expanded_nodes
        for next_vertex in get_neighbors(maze, vertex):
            if next_vertex not in visited:
                visited.add(next_vertex)
                queue.append((next_vertex, path + [next_vertex]))

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

def simulate_bfs(maze_width, maze_height, num_simulations):
    total_time = 0
    solved_count = 0
    
    for _ in range(num_simulations):
        maze = Maze(maze_width, maze_height)
        maze.generate_maze()
        start = (0, 0)
        goal = (maze_width - 1, maze_height - 1)
        
        timer = timeit.Timer(lambda: bfs(maze.maze, start, goal))
        exec_time = timer.timeit(number=1)
        
        path, _ = bfs(maze.maze, start, goal)
        total_time += exec_time
        if path is not None:
            solved_count += 1
    
    if solved_count == 0:
        return float('inf'), 0
    avg_time = total_time / solved_count
    return avg_time, solved_count

