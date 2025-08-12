from collections import deque


def breadth_first_traversal(graph, source, visited_nodes):
    queue = deque([source])
    visited_nodes.add(source)
    while len(queue):
        current = queue.popleft()
        visited_nodes.add(current)
        for neighbor in graph[current]:
            # Do not revisit traversed nodes
            if neighbor not in visited_nodes:
                queue.append(neighbor)
                visited_nodes.add(neighbor)


def depth_first_traversal(graph, source, visited_nodes):
    if source in visited_nodes:
        return
    visited_nodes.add(source)
    for neighbor in graph[source]:
        depth_first_traversal(graph, neighbor, visited_nodes)


def count_connected_components(graph) -> int:
    visited_nodes: set[int] = set()  # O(1) lookup and insertion
    count = 0
    # Iterate through each node. If node has NOT been visited
    # we can perform breadth-first traversal to visit all
    # nodes connected to it. This consitutes one conneted
    # component. Do this for all nodes in the graph. Skip
    # traversals for nodes that have already been visited.
    for node in graph:
        if node in visited_nodes:
            continue
        # Unvisited node: perform breadth-first traversal
        breadth_first_traversal(graph, node, visited_nodes)
        count += 1
    return count


def count_nodes_in_component(graph, src, visited: set[int]) -> int:
    # if node has been visited, it has no unvisited components
    # to be counted. Therefore, return 0: base-case. No depth-first
    # traversal is required
    if src in visited:
        return 0
    # count current unvisited node
    count = 1
    visited.add(src)
    # Go through neighbours and count nodes from their traversals
    for neighbor in graph[src]:
        ## add count for EACH branch-> depth-first traversal
        count += count_nodes_in_component(graph, neighbor, visited)
    return count


def count_nodes_in_component_breadth_first(graph, src, visited: set[int]):
    if src in visited:
        return 0
    count = 0
    queue = deque([src])
    # Whenever a node is added to the queue, we consider it
    # visited. This is because when we add neighbours of a node
    # to the queue, the same neighbours can be neigbours of each other
    # as well due to the undirected nature of the graph. This could lead
    # to repetitions in the queue.
    visited.add(src)
    while len(queue):
        current_node = queue.popleft()
        count += 1
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return count


def count_nodes_in_components_df_iterative(graph, node, visited):
    count = 0
    stack = list()
    stack.append(node)
    visited.add(node)
    while len(stack):
        current = stack.pop()
        count += 1
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.push(neighbor)
                visited.add(neighbor)

    return count


def largest_component(graph) -> int:
    max_count = 0
    visited_nodes: set[int] = set()
    for node in graph:
        if node in visited_nodes:
            continue
        # num_nodes = count_nodes_in_component(graph, node, visited_nodes)
        num_nodes = count_nodes_in_component_breadth_first(graph, node, visited_nodes)
        max_count = max(max_count, num_nodes)
    return max_count


if __name__ == "__main__":
    graph1 = {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}
    graph2 = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    # assert count_connected_components(graph) == 3

    #### Largest component test cases
    ## O(V+E) time complexity, O(V) space complexity
    print("Largest Component Cases")
    test_cases = [(graph1, 5), (graph2, 4)]
    for graph, expected_largest_component in test_cases:
        largest_component_count = largest_component(graph)
        assert (
            largest_component_count == expected_largest_component
        ), f"expected {expected_largest_component}, got {largest_component_count}"

    #### Count components test cases
    ## O(V+E) time complexity, O(V) space complexity
    print("Count Component Cases")
    test_cases = [(graph1, 3), (graph2, 2)]
    for graph, expected_num_components in test_cases:
        num_components = count_connected_components(graph)
        assert (
            num_components == expected_num_components
        ), f"expected {num_components}, got {expected_num_components}"
