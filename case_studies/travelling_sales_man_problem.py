"""
**Problem Statement: Optimal Delivery Routing**

You are working for a delivery company that needs to optimize its delivery routes to minimize the total distance traveled by its delivery trucks. The company has a list of delivery points (locations) and wants to determine the most efficient route to deliver packages to all these points, starting and ending at the company's warehouse.

Your task is to write a Python program that can find the optimal route for the delivery trucks based on the following criteria:

1. **Input Data:** The program should take as input a list of delivery points, including their coordinates (latitude and longitude), and the coordinates of the warehouse.

2. **Route Calculation:** The program should calculate the optimal route that starts and ends at the warehouse while visiting all delivery points exactly once. This is a variation of the Traveling Salesman Problem (TSP).

3. **Output:** The program should output the optimal route, including the order in which delivery points should be visited, and the total distance traveled.

4. **Visualization:** Optionally, you can visualize the route on a map to provide a visual representation of the optimized delivery path.

The optimization should take into account the distances between points on the map (you can use real geographical coordinates to calculate distances accurately) and aim to minimize the total distance traveled.

You can use libraries like NetworkX, scipy, or any suitable Python libraries for solving TSP or graph optimization problems.

Example:
```python
# Input data
warehouse = (12.9716, 77.5946)  # Warehouse coordinates (latitude, longitude)
delivery_points = [
    (12.9575, 77.5802),  # Delivery point 1
    (12.9634, 77.5669),  # Delivery point 2
    (12.9747, 77.6119),  # Delivery point 3
    # Add more delivery points...
]

# Your program should calculate the optimal route and print it along with the total distance.
# Optionally, you can visualize the route on a map.
```

Your solution should efficiently handle a moderate number of delivery points and provide a clear and optimized delivery route.

Feel free to adjust the problem statement or add additional requirements to make it more challenging if desired.
"""

import itertools

# Calculate the Euclidean distance between two points
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Calculate the total distance of a route
def calculate_total_distance(route, points):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(points[route[i]], points[route[i + 1]])
    return total_distance

# Find the optimal route using brute force
def find_optimal_route(warehouse, delivery_points):
    all_points = [warehouse] + delivery_points
    num_points = len(all_points)
    all_routes = itertools.permutations(range(1, num_points))  # Exclude the warehouse itself

    optimal_route = None
    min_distance = float('inf')

    for route in all_routes:
        route = (0,) + route  # Start and end at the warehouse (point 0)
        distance = calculate_total_distance(route, all_points)

        if distance < min_distance:
            min_distance = distance
            optimal_route = route

    return optimal_route, min_distance

# Input data
warehouse = (12.9716, 77.5946)
delivery_points = [
    (12.9575, 77.5802),
    (12.9634, 77.5669),
    (12.9747, 77.6119),
]

# Find the optimal route and total distance
optimal_route, total_distance = find_optimal_route(warehouse, delivery_points)

# Print the optimal route and total distance
print("Optimal Route:")
for point_index in optimal_route:
    print(delivery_points[point_index - 1])  # Subtract 1 to account for the warehouse

print(f"Total Distance: {total_distance:.2f} units")
