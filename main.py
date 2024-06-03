from bfs import simulate_bfs
from ids import simulate_ids
from visualization import run_visualization
from astar import simulate_astar

def main():
    maze_width = 100 
    maze_height = 100
    num_simulations = 1000
    max_depth = 500

    # avg_time, solved_count = simulate_bfs(maze_width, maze_height, num_simulations)
    # print(f"Average BFS execution time over {num_simulations} simulations - with {solved_count} being solved: {avg_time:.6f} seconds")
    #
    # avg_ids_time, solved_ids_count = simulate_ids(maze_width, maze_height, num_simulations, max_depth)
    # print(f"Average IDS execution time over {num_simulations} simulations - with {solved_ids_count} being solved: {avg_ids_time:.6f} seconds")
    #
    # avg_time_astar, solved_count_astar = simulate_astar(maze_width, maze_height, num_simulations)
    # print(f"Average A* execution time over {num_simulations} simulations - with {solved_count_astar} being solved: {avg_time_astar:.6f} seconds")

    solvable_bfs = run_visualization(maze_width, maze_height, 0.3, algorithm="bfs")
    if not solvable_bfs:
        print("BFS: Maze was unsolvable, try running again or adjusting wall probability.")

    solvable_ids = run_visualization(maze_width, maze_height, 0.3, algorithm="ids", max_depth=max_depth)
    if not solvable_ids:
        print("IDS: Maze was unsolvable, try running again or adjusting wall probability.")

    solvable_astar = run_visualization(maze_width, maze_height, 0.3, algorithm="astar")
    if not solvable_astar:
        print("A*: Maze was unsolvable, try running again or adjusting wall probability.")


if __name__ == "__main__":
    main()

