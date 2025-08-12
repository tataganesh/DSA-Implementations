from dsa_implementations.data_structures.circular_queue import CircularQueue

# Adjacency list representation of directed graph
directed_graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
}

# Adjacency list representation of undirected graph
undirected_graph = {
    "i": ["j", "k"],
    "j": ["i"],
    "k": ["i", "m", "l"],
    "m": ["k"],
    "l": ["k"],
    "o": ["n"],
    "n": ["o"],
}


def has_path_recursive(graph, source, dest) -> bool:
    if source == dest:
        return True
    ## Go through each neighbour of node
    for neighbor in graph[source]:
        # check if neighbor->dest path exists
        path_exists = has_path_recursive(graph, neighbor, dest)
        # If that path exists, return True
        # (if source->neighbour and neighbour->dest exist, source->dest exists)
        # else, go to next neighbor and check if path exists
        if path_exists:
            return True
    # If branches from all neighbors have been exhausted
    # return false since no path from source->dest was found
    return False


def has_path_bfs(graph, source, dest):
    queue = CircularQueue(capacity=50)
    queue.push(source)
    while queue.size():
        current = queue.pop()
        if current == dest:
            return True
        for neighbor in graph[current]:
            queue.push(neighbor)
    return False


def has_path_undirected(graph, source, dest, visited_nodes=set()) -> bool:
    # Do not proceed further if node has already been visited
    if source in visited_nodes:
        return False
    # If source and dest are same, we found a path
    if source == dest:
        return True
    # Add source to visited set. Ensures same node is not visited again
    visited_nodes.add(source)
    for neighbor in graph[source]:
        # visited_nodes are passed to ensure state is passed
        path_exists = has_path_undirected(graph, neighbor, dest, visited_nodes)
        if path_exists:
            return True
    return False


def has_path_bfs_undirected(graph, source, dest) -> bool:
    visited_nodes = set()
    queue = CircularQueue(capacity=50)
    queue.push(source)
    visited_nodes.add(source)
    while queue.size():
        current = queue.pop()
        if current == dest:
            return True
        for neighbor in graph[current]:
            # Only add unvisted nodes to avoid re-traversal and
            # cycle issues in an undirected graph
            if neighbor not in visited_nodes:
                queue.push(neighbor)
                visited_nodes.add(neighbor)
    return False


if __name__ == "__main__":
    print(has_path_recursive(directed_graph, "j", "g"))
    print(has_path_bfs(directed_graph, "f", "h"))
    print(has_path_bfs_undirected(undirected_graph, "i", "n"))
    print(has_path_undirected(undirected_graph, "i", "m"))
