from heapq import heappush, heappop


# The heuristic function (Manhattan distance)
def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


# Returns a list of valid neighbors of a given cell
def get_neighbors(maze, cell, n):
    neighbors = []
    x, y = cell
    if x > 0 and maze[x-1][y] != "#":
        neighbors.append((x-1, y))
    if x < n-1 and maze[x+1][y] != "#":
        neighbors.append((x+1, y))
    if y > 0 and maze[x][y-1] != "#":
        neighbors.append((x, y-1))
    if y < n-1 and maze[x][y+1] != "#":
        neighbors.append((x, y+1))
    return neighbors


# The A_star algorithm
def a_star(maze, start, goal, g_cost, n):
    # A heap to store the cells to be expanded
    heap = [(0, start)]
    # A dictionary to store the costs of each cell
    costs = {start: (0, heuristic(start, goal))}
    # A dictionary to store the parents of each cell
    parents = {}
    while heap:
        cost, cell = heappop(heap)
        if cell == goal:
            path = [cell]
            while cell in parents:
                cell = parents[cell]
                path.append(cell)
            path.reverse()
            return path, cost
        for neighbor in get_neighbors(maze, cell, n):
            g = costs[cell][0] + g_cost
            h = heuristic(neighbor, goal)
            f = g + h
            if neighbor not in costs or (g, h) < costs[neighbor]:
                costs[neighbor] = (g, h)
                heappush(heap, (f, neighbor))
                parents[neighbor] = cell
    return None, None
