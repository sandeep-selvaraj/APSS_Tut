import random
import math
from queue import PriorityQueue

VISITED = [] #Keep a track of all the neighborhoods visited
PENALTY = 1

def simulated_annealing(grid, start, goal, T, alpha, max_iterations):
    current_solution = start
    current_cost = get_path_length(grid, start, goal)
    best_solution = current_solution
    best_cost = current_cost

    for i in range(max_iterations):
        # Generate a random move to a neighboring cell
        next_solution = random_neighbor(grid, current_solution)
        next_cost = get_path_length(grid, next_solution, goal)

        delta_cost = next_cost - current_cost
        acceptance_probability = min(1, math.exp(-delta_cost / T))

        # Decide whether to accept the new solution
        if acceptance_probability > random.uniform(0, 1):
            current_solution = next_solution
            current_cost = next_cost

        # Update the best solution
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

        T *= alpha

    return best_solution

def get_path_length(grid, start, goal):
    # Implementation of the algorithm to find the length of the path
    # from start to goal in the grid
	# Add penalty to whenever the path traverses a wall
	# Manhattan distance can also be used

    pq = PriorityQueue()
    pq.put((0, start))
    visited = set([start])

    while not pq.empty():
        dist, curr = pq.get()
        x, y = curr

        if curr == goal:
            return dist

        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):
                if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                    pq.put((dist + manhattan_distance(neighbor, goal), neighbor))
                    visited.add(neighbor)

## For passing through a wall
                elif grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in visited:
                    pq.put((dist + manhattan_distance(neighbor, goal) + PENALTY, neighbor))
                    visited.add(neighbor)

    return -1  # If no path is found, return -1


def random_neighbor(grid, current_solution):
    # Implementation of the algorithm to generate a random move to a neighboring cell in the grid

    neighbors = []
    x, y = current_solution

    # Generate the list of unvisited neighbors
    if x > 0 and grid[x-1][y] not in VISITED:
        neighbors.append((x-1, y))
    if x < len(grid) - 1 and grid[x+1][y] not in VISITED:
        neighbors.append((x+1, y))
    if y > 0 and grid[x][y-1] not in VISITED:
        neighbors.append((x, y-1))
    if y < len(grid[0]) - 1 and grid[x][y+1] not in VISITED:
        neighbors.append((x, y+1))

    # Return a random unvisited neighbor
    if len(neighbors) > 0:
        next_solution = random.choice(neighbors)
        VISITED.append(next_solution)
        return next_solution
    else:
        return current_solution

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)