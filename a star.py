import heapq

# Define directions: up, down, left, right
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

class Node:
    def __init__(self, position, g, h, parent=None):
        self.position = position  # (x, y)
        self.g = g                # Cost from start to node
        self.h = h                # Heuristic cost to goal
        self.f = g + h            # Total cost
        self.parent = parent      # Parent node for path reconstruction

    def __lt__(self, other):  # Needed for heapq
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)
        if current.position == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Reverse path

        closed_set.add(current.position)

        for d in dirs:
            neighbor_pos = (current.position[0] + d[0], current.position[1] + d[1])

            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):

                g_cost = current.g + 1
                h_cost = heuristic(neighbor_pos, goal)
                neighbor = Node(neighbor_pos, g_cost, h_cost, current)

                # Avoid adding duplicates with higher cost
                if all(neighbor.position != n.position or neighbor.f < n.f for n in open_list):
                    heapq.heappush(open_list, neighbor)

    return None  # No path found

# Example grid (0 = walkable, 1 = wall)
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
print("Path found by A*:", path)
