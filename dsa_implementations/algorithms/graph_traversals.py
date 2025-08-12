from __future__ import annotations
from dsa_implementations.data_structures.stack import Stack
from dsa_implementations.data_structures.circular_queue import CircularQueue


# Adjacency list representation of graph
graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def depth_first_print(graph: dict[str, list], source: str):
    stack = Stack()
    stack.push(source)
    visited_nodes = list()
    while not stack.isEmpty():
        popped_vertex = stack.pop()
        print(popped_vertex)
        visited_nodes.append(popped_vertex)
        for neighbor in graph[popped_vertex]:
            stack.push(neighbor)


def depth_first_print_recursive(graph: dict[str, list], source: str):
    print(source)
    for neighbor in graph[source]:
        depth_first_print_recursive(graph, neighbor)


def breadth_first_print(graph: dict[str, list], source: str):
    queue = CircularQueue(capacity=50)
    queue.push(source)
    while queue.size():
        popped_node = queue.pop()
        print(popped_node)
        for neighbor in graph[popped_node]:
            queue.push(neighbor)


if __name__ == "__main__":
    print("Depth First Iterative")
    depth_first_print(graph, "a")
    print("Depth First Recursive")
    depth_first_print_recursive(graph, "a")
    print("Breadth First")
    breadth_first_print(graph, "a")
