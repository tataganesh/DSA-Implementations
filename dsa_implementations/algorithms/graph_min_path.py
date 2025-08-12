from collections import deque


def edges_to_graph(edges):
    graph = dict()
    for node1, node2 in edges:
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph


def shortest_path(edges, node_A, node_B) -> int:
    graph = edges_to_graph(edges)
    visited_nodes = set()
    ## We will track the distance of each node added to the
    ## queue from node_A. Initially, since only node_A is present
    ## in the queue, edges between node_A and node_A are 0.
    queue = deque([(node_A, 0)])
    visited_nodes.add(node_A)
    # While queue is non-empty
    while len(queue):
        # pop both the node and the distance of the node from node_A
        current_node, current_node_distance = queue.popleft()
        # if node_B is found, return distance
        if current_node == node_B:
            return current_node_distance
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                # For each unvisited neighbour, add the neigbour
                # and its distance from node_A.
                queue.append((neighbor, current_node_distance + 1))
                visited_nodes.add(neighbor)
    return -1


def shortest_path_edge_level(edges, node_A, node_B):
    graph = edges_to_graph(edges)
    visited_nodes = set()
    queue = deque([node_A])
    visited_nodes.add(node_A)
    # Edge count keeps track of the distance
    # of node_A from all nodes CURRENTLY present in the queue
    # For instance, node_A is currently 0 edge away from node_A
    edge_count = 0
    while len(queue):
        ## We will traverse through ALL nodes
        ## that are `edge_count` away from node_A
        ## These are all nodes currently present in the queue
        num_nodes_at_current_edge = len(queue)
        for _ in range(num_nodes_at_current_edge):
            current_node = queue.popleft()
            if current_node == node_B:
                return edge_count
            for neighbor in graph[current_node]:
                if neighbor not in visited_nodes:
                    visited_nodes.add(neighbor)
                    queue.append(neighbor)
        ## Once we have traversed through all nodes
        ## at `edge_count` distance (and added their neighbours)
        ## to the queue, we can increment it. This indicates
        ## that edge count represents distance of node_A from all nodes
        ## CURRENTLY in the queue.
        edge_count += 1
    return -1


if __name__ == "__main__":
    edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
    assert shortest_path(edges, "w", "z") == 2
    assert shortest_path_edge_level(edges, "w", "z") == 2
    edges = [
        ["a", "c"],
        ["a", "b"],
        ["c", "b"],
        ["c", "d"],
        ["b", "d"],
        ["e", "d"],
        ["g", "f"],
    ]
    assert shortest_path(edges, "b", "g") == -1
    assert shortest_path_edge_level(edges, "b", "g") == -1
