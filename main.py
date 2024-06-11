from bfs import simulate_bfs
from ids import simulate_ids
from astar import simulate_astar
from visualization import run_visualization

def main():
    # Initial maze parameters
    maze_width = 25
    maze_height = 25 
    num_simulations = 100

    # # Maze parameters without IDS
    # maze_width = 100
    # maze_height = 100 
    # num_simulations = 1000
    #
    # # Maze parameters for visualization
    # maze_width = 15
    # maze_height = 15 

    # Randomized Maze BFS
    avg_time_bfs, solved_count_bfs, avg_expanded_nodes_bfs, avg_max_queue_size_bfs, avg_memory_usage_bfs, avg_path_legth_bfs = simulate_bfs(maze_width, maze_height, num_simulations)           
    print("BFS:")
    print("  Theoretical Time Complexity: O(b^d)")
    print("  Theoretical Space Complexity: O(b^d)")
    print(f"  Empirical Average Time: {avg_time_bfs:.6f} sec")
    print(f"  Solved: {solved_count_bfs}/{num_simulations}")
    print(f"  Empirical Avg Expanded Nodes: {avg_expanded_nodes_bfs}")
    print(f"  Empirical Avg Max Queue Size: {avg_max_queue_size_bfs}\n")
    print(f"  Empirical Avg Memory Usage: {avg_memory_usage_bfs:.6f} MB")
    print(f"  Empirical Avg Path Length: {avg_path_legth_bfs}\n")

    # Randomized Maze IDS
    avg_time_ids, solved_count_ids, avg_expanded_nodes_ids, avg_max_queue_size_ids,avg_memory_usage_ids, avg_path_length_ids  = simulate_ids(maze_width, maze_height, num_simulations)
    print("IDS:")
    print("  Theoretical Time Complexity: O(b^d)")
    print("  Theoretical Space Complexity: O(d)")
    print(f"  Empirical Average Time: {avg_time_ids:.6f} sec")
    print(f"  Solved: {solved_count_ids}/{num_simulations}")
    print(f"  Empirical Avg Expanded Nodes: {avg_expanded_nodes_ids}")
    print(f"  Empirical Avg Max Queue Size: {avg_max_queue_size_ids}")
    print(f"  Empirical Avg Memory Usage: {avg_memory_usage_ids:.6f} MB")
    print(f"  Empirical Avg Path Length: {avg_path_length_ids}\n")

    # Randomized Maze A*
    avg_time_astar, solved_count_astar, avg_expanded_nodes_astar, avg_max_queue_size_astar, avg_memory_usage_astar, avg_path_length_astar = simulate_astar(maze_width, maze_height, num_simulations)
    print("A*:")
    print("  Theoretical Time Complexity: O(b^d)")
    print("  Theoretical Space Complexity: O(b^d)")
    print(f"  Empirical Average Time: {avg_time_astar:.6f} sec")
    print(f"  Solved: {solved_count_astar}/{num_simulations}")
    print(f"  Empirical Avg Expanded Nodes: {avg_expanded_nodes_astar}")
    print(f"  Empirical Avg Max Queue Size: {avg_max_queue_size_astar}\n")
    print(f"  Empirical Avg Memory Usage: {avg_memory_usage_astar:.6f} MB")
    print(f"  Empirical Avg Path Length: {avg_path_length_astar}\n")

    # # Visualization for each algorithm
    # algorithms = ['bfs', 'ids', 'astar']
    # solvable = run_visualization(maze_width, maze_height, 0.3, algorithms)
    # if not solvable:
    #     print("Maze was unsolvable for all algorithms, try running again or adjusting wall probability.")


if __name__ == "__main__":
    main()
