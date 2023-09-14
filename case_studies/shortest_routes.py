"""
**Problem Statement: Optimizing Delivery Routes**

You work for a delivery company that needs to optimize its delivery routes to save time and fuel costs. You are given
a map of a city represented as a grid. Each cell in the grid represents a location, and it can either be a delivery
point (D), a warehouse (W), an obstacle (X), or an empty space (.).

Your task is to find the shortest path from each warehouse (W) to every delivery point (D) while avoiding obstacles (
X). Additionally, you need to minimize the total distance traveled by all delivery trucks combined. You can assume
that a delivery truck can move in four directions: up, down, left, or right.

Write a Python function `optimize_delivery_routes(grid)` that takes a grid as input and returns a list of tuples,
where each tuple represents a delivery route from a warehouse to a delivery point. Each tuple should contain the
following information:

1. Starting warehouse coordinates (row, column). 2. Ending delivery point coordinates (row, column). 3. The sequence
of moves (U for up, D for down, L for left, R for right) to reach the delivery point while avoiding obstacles.

The goal is to minimize the total distance traveled by all delivery trucks combined.

Example:
```python
grid = [
    ["W", ".", ".", ".", ".", ".", ".", ".", "D"],
    [".", "X", ".", ".", "D", ".", "W", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "W", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["D", ".", ".", ".", ".", ".", ".", ".", "W"]
]

result = optimize_delivery_routes(grid)

# Expected result:
# [
#     ((0, 0), (0, 8), "R"*8),
#     ((1, 6), (0, 4), "U"*2+"L"*4),
#     ((3, 2), (1, 6), "R"*4+"D"*1),
#     ((8, 8), (8, 0), "L"*8)
# ]
```

Solving this problem efficiently requires a combination of graph traversal algorithms (such as Breadth-First Search)
and optimization techniques. It's a complex problem that involves pathfinding, distance calculation, and coordination
between multiple delivery trucks.
"""


# Define possible movements: Up, Down, Left, Right
MOVEMENTS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
MOVEMENT_NAMES = ['R', 'L', 'U', 'D']

def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X'

def shortest_path(grid, start, end):
    visited = set()
    queue = [(start, [])]

    while queue:
        (x, y), path = queue.pop(0)

        if (x, y) == end:
            return path

        for (dx, dy), move in zip(MOVEMENTS, MOVEMENT_NAMES):
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, grid) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                new_path = path + [move]
                queue.append(((new_x, new_y), new_path))
        print(queue)
    return None

def optimize_delivery_routes(grid):
    warehouses = []
    delivery_points = []

    # Find warehouse and delivery point coordinates
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'W':
                warehouses.append((i, j))
            elif grid[i][j] == 'D':
                delivery_points.append((i, j))

    routes = []

    # Find the shortest route from each warehouse to each delivery point
    for warehouse in warehouses:
        for delivery_point in delivery_points:
            path = shortest_path(grid, warehouse, delivery_point)
            if path:
                routes.append((warehouse, delivery_point, path))

    return routes

grid = [
    ["W", ".", ".", ".", ".", ".", ".", ".", "D"],
    [".", "X", ".", ".", "D", ".", "W", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "W", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["D", ".", ".", ".", ".", ".", ".", ".", "W"]
]

result = optimize_delivery_routes(grid)
print(result)
