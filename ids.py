from collections import deque
import resource
from maze import Maze
import timeit

def ids(maze, start, goal):
    # Increase the maximum recursion depth from 1 to the maximum number of cells in the maze
    for max_depth in range(1, len(maze) * len(maze[0])):
        visited = set()
        result = ids_helper(maze, start, goal, max_depth, visited)
        if result[0] is not None:
            return result[:3]
    return None, [], 0

def ids_helper(maze, start, goal, max_depth, visited):
    # Use a deque to initialize the queue with the start node and its path
    queue = deque([(start, [start], 0)])
    visited.add(start)
    expanded_nodes = []
    max_queue_size = 0
    while queue:
        queue_size = len(queue)
        if queue_size > max_queue_size:
            max_queue_size = queue_size
        (vertex, path, depth) = queue.popleft()
        expanded_nodes.append(vertex)
        if vertex == goal:
            return path, expanded_nodes, max_queue_size, len(visited)
        # If the goal is not yet reached, continue expanding the queue only if the current depth is less than the maximum depth
        if depth < max_depth:
            for next_vertex in get_neighbors(maze, vertex):
                if next_vertex not in visited:
                    visited.add(next_vertex)
                    queue.append((next_vertex, path + [next_vertex], depth + 1))
    return None, expanded_nodes, max_queue_size

def get_neighbors(maze, vertex):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    x, y = vertex
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

# IDS simulation
def simulate_ids(maze_width, maze_height, num_simulations):
    total_time = 0
    solved_count = 0
    total_expanded_nodes = 0
    total_max_queue_size = 0
    total_memory_usage = 0
    total_path_length = 0

    for _ in range(num_simulations):
        maze = Maze(maze_width, maze_height)
        maze.generate_maze()
        start = (0, 0)
        goal = (maze_width - 1, maze_height - 1)

        initial_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        timer = timeit.Timer(lambda: ids(maze.maze, start, goal))
        exec_time = timer.timeit(number=1)
        final_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        path, expanded_nodes, max_queue_size = ids(maze.maze, start, goal)
        total_time += exec_time
        total_expanded_nodes += len(expanded_nodes)
        total_max_queue_size += max_queue_size
        total_memory_usage += final_memory - initial_memory
        if path is not None:
            solved_count += 1
            total_path_length += len(path)

    if solved_count == 0:
        return float('inf'), 0, 0, 0, 0, 0
    avg_time = total_time / solved_count
    avg_expanded_nodes = total_expanded_nodes / solved_count
    avg_max_queue_size = total_max_queue_size / solved_count
    avg_memory_usage = total_memory_usage / solved_count
    avg_path_length = total_path_length / solved_count
    return avg_time, solved_count, avg_expanded_nodes, avg_max_queue_size, avg_memory_usage, avg_path_length

