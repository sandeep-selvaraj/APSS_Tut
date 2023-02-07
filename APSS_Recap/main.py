# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from a_star import sat_algo, maze_algo


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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _do_maze_a_star()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
