def minimax(depth, node_index, is_max, values, alpha, beta, branching_factor, pruned):
    # Base case: leaf node
    if depth == 0:
        return values[node_index]

    if is_max:
        max_eval = float('-inf')
        for i in range(branching_factor):
            child_index = node_index * branching_factor + i
            if beta <= alpha:
                pruned.append((depth, child_index, "MAX"))
                break
            val = minimax(depth - 1, child_index, False, values, alpha, beta, branching_factor, pruned)
            max_eval = max(max_eval, val)
            alpha = max(alpha, val)
        return max_eval

    else:
        min_eval = float('inf')
        for i in range(branching_factor):
            child_index = node_index * branching_factor + i
            if beta <= alpha:
                pruned.append((depth, child_index, "MIN"))
                break
            val = minimax(depth - 1, child_index, True, values, alpha, beta, branching_factor, pruned)
            min_eval = min(min_eval, val)
            beta = min(beta, val)
        return min_eval

# Example: binary tree of depth 3, branching factor = 2
values = [3, 5, 6, 9, 1, 2, 0, -1]  # 2^3 = 8 leaves
depth = 3
branching_factor = 2
pruned_nodes = []

optimal = minimax(depth, 0, True, values, float('-inf'), float('inf'), branching_factor, pruned_nodes)

print(f"Optimal value: {optimal}")
print("Pruned branches (depth, node_index, role):")
for d, idx, role in pruned_nodes:
    print(f"  - Depth {d}, Node Index {idx}, Role: {role}")
