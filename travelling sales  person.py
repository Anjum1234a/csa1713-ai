import itertools

# Distance matrix where dist[i][j] is the distance from city i to city j
dist = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

n = len(dist)
cities = list(range(n))

# Initialize minimum path cost as infinity
min_path_cost = float('inf')
best_path = []

# Try every possible permutation of cities
for perm in itertools.permutations(cities[1:]):
    current_path = [0] + list(perm) + [0]
    cost = sum(dist[current_path[i]][current_path[i + 1]] for i in range(n))
    
    if cost < min_path_cost:
        min_path_cost = cost
        best_path = current_path

# Output the result
print("Shortest path:", best_path)
print("Minimum cost:", min_path_cost)
