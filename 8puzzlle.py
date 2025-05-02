import heapq

# Goal state
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Heuristic function: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Convert nested list to a tuple for hashing
def state_to_tuple(state):
    return tuple(num for row in state for num in row)

# Find position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate possible next moves
def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# A* Search Algorithm
def a_star(start_state):
    visited = set()
    heap = []
    g_score = 0
    f_score = manhattan_distance(start_state)
    heapq.heappush(heap, (f_score, g_score, start_state, []))

    while heap:
        f, g, current_state, path = heapq.heappop(heap)
        state_key = state_to_tuple(current_state)

        if current_state == GOAL_STATE:
            return path + [current_state]

        if state_key in visited:
            continue
        visited.add(state_key)

        for neighbor in get_neighbors(current_state):
            if state_to_tuple(neighbor) not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(heap, (new_f, new_g, neighbor, path + [current_state]))

    return None

# Example usage
start_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = a_star(start_state)

if solution:
    print("Steps to solve:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
