"""
Reference  - https://www.youtube.com/watch?v=fAAZixBzIAI
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any
from dsa_implementations.data_structures.circular_queue import CircularQueue
from dsa_implementations.data_structures.stack import Stack


@dataclass
class Node:
    """Represent node in a binary tree"""

    val: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def breadth_first_values_iterative(root: Node) -> list[Any]:
    """Print the depth-wise traversal of a binary tree

    Args:
        root (Node): Root node of a binary tree
    """
    if not root:
        return []
    queue = CircularQueue(capacity=1000)
    # First, push root node
    queue.push(root)
    traversed_nodes = list()
    while queue.size():
        # Pop node from front of queue. This node
        # has been traversed.
        popped_node = queue.pop()
        traversed_nodes.append(popped_node.val)
        if popped_node.left:
            queue.push(popped_node.left)
        if popped_node.right:
            queue.push(popped_node.right)
    return traversed_nodes


def depth_first_values_iterative(root: Node) -> list[Any]:
    """Print the breadth-wise traversal of a binary tree

    Args:
        root (Node): Root node of a binary tree
    """
    if not root:
        return []
    traversed_node_values: list[Any] = list()
    stack = Stack()
    stack.push(root)  # Ensure that root is already present in the stack
    while stack.size():
        # First, pop the element from the stack and print it since
        # it has been traversed
        traversed_node = stack.pop()
        traversed_node_values.append(traversed_node.val)
        # Push right and left children to stack (in that order)
        # Left is pushed after right to make sure that it is
        # considered first during traversal (need to go as deep
        # as possible from the left side)
        if traversed_node.right:
            stack.push(traversed_node.right)
        if traversed_node.left:
            stack.push(traversed_node.left)
    return traversed_node_values


def depth_first_values_recursive(root: Optional[Node]) -> list[Any]:
    if not root:
        return []
    # We want to perform depth-first traversal
    # of each subtree. We need to start from the left
    # subtree and go deep into that branch, and so on. We assume that each function
    # call returns the depth-first traversed nodes starting from that node.
    # If any of the children don't exist, the function returns an empty list
    # and you move onto root.right.
    left_tree_traversed_nodes: list[Any] = depth_first_values_recursive(root.left)
    right_tree_traversed_nodes: list[Any] = depth_first_values_recursive(root.right)
    # Once you get left and right subtree traversed nodes, you can do
    # root + left + right to get the depth-first values starting from the
    # root node
    return [root.val] + left_tree_traversed_nodes + right_tree_traversed_nodes


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    ## construct tree
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    # print(breadth_first_values_iterative(a))
    traversed_node_iterative = depth_first_values_iterative(a)
    traversed_node_recursive = depth_first_values_recursive(a)
    assert (
        traversed_node_iterative == traversed_node_recursive
    ), "Depth-first traversal: Iterative and Recursive implementations do not produce the same result"
    """
        a
        /  \
        b    c
       /       \
      d         f
    """

    ## Some more examples generated using Claude

    # Example 1: A simple binary tree
    #      1
    #    /   \
    #   2     3
    #  / \
    # 4   5
    def create_simple_tree():
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        return root

    # Example 2: A balanced binary search tree
    #       4
    #     /   \
    #    2     6
    #   / \   / \
    #  1   3 5   7
    def create_balanced_bst():
        root = Node(4)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(5)
        root.right.right = Node(7)
        return root

    # Example 3: A skewed binary tree (right-skewed)
    #  1
    #   \
    #    2
    #     \
    #      3
    #       \
    #        4
    def create_skewed_tree():
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        root.right.right.right = Node(4)
        return root

    # Example 4: A complete binary tree
    #        1
    #     /     \
    #    2       3
    #   / \     / \
    #  4   5   6   7
    def create_complete_tree():
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        return root

    print(breadth_first_values_iterative(create_simple_tree()))
