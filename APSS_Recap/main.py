# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from a_star import sat_algo, maze_algo
from ea_algos import ea_tsp

def _do_sat_a_star():
    cnf = [[1, 2], [-1, 3], [2, 3, 4]]
    print(sat_algo.boolean_satisfiability(cnf, sat_algo.variables_in_cnf(cnf)))


def _do_maze_a_star():
    # Example maze with n = 5
    n = 5
    maze = [
        ["S", ".", ".", ".", "."],
        ["#", "#", ".", "#", "#"],
        [".", ".", ".", "#", "."],
        [".", "#", "#", "#", "."],
        [".", ".", ".", ".", "G"],
    ]

    # The cost of moving from one cell to another in the maze
    COST = 1

    # The goal position (top-right corner of the maze)
    GOAL = (n - 1, n - 1)

    # Starting position (bottom-left corner of the maze)
    start = (0, 0)

    # Find the shortest path
    path, cost = maze_algo.a_star(maze, start, GOAL, COST, n)

    # Print the results
    if path:
        print("Shortest path:", path)
        print("Cost:", cost)
    else:
        print("No solution found.")

def _call_ea_tsp():
    cities = 8
    distances = [[0, 10, 20, 30, 40, 50, 60, 70],
                 [10, 0, 10, 20, 30, 40, 50, 60],
                 [20, 10, 0, 10, 20, 30, 40, 50],
                 [30, 20, 10, 0, 10, 20, 30, 40],
                 [40, 30, 20, 10, 0, 10, 20, 30],
                 [50, 40, 30, 20, 10, 0, 10, 20],
                 [60, 50, 40, 30, 20, 10, 0, 10],
                 [70, 60, 50, 40, 30, 20, 10, 0]]

    print(ea_tsp.evolutionary_algorithm(cities, distances, 10, 5, 0.8, 0.5))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # _do_maze_a_star()
    _call_ea_tsp()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
