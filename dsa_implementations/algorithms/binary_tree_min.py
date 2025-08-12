from __future__ import annotations
from typing import Optional, Any
from dsa_implementations.data_structures.circular_queue import CircularQueue
import sys
from dataclasses import dataclass


@dataclass
class Node:
    """Represent node in a binary tree"""

    val: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def tree_min_iterative(root: Node) -> int:
    if not root:
        return sys.maxsize
    minimum_value = root.val
    queue = CircularQueue(capacity=10000)
    queue.push(root)  # q = [root]
    while queue.size():
        popped_node = queue.pop()
        minimum_value = min(popped_node.val, minimum_value)
        if popped_node.left:
            queue.push(popped_node.left)
        if popped_node.right:
            queue.push(popped_node.right)
    return minimum_value


def tree_min_recursive(root: Optional[Node]) -> int:
    if not root:
        return sys.maxsize
    left_min = tree_min_recursive(root.left)
    right_min = tree_min_recursive(root.right)
    return min(left_min, right_min, root.val)


def test_implementation(tree_min_funtion, test_cases):
    for root, expected_min_value in test_cases:
        minimum_node_value = tree_min_funtion(root)
        assert (
            minimum_node_value == expected_min_value
        ), f"Expected: {expected_min_value}, Received: {minimum_node_value}"


if __name__ == "__main__":
    #### Create example trees for testing
    # Example 1: A simple binary tree with negative numbers
    #      -1
    #    /    \
    #   2     -3
    #  / \
    # -4  5
    def create_simple_tree_with_negatives():
        root = Node(-1)
        root.left = Node(2)
        root.right = Node(-3)
        root.left.left = Node(-4)
        root.left.right = Node(5)
        return root

    # Example 2: A balanced binary search tree with negative numbers
    #        0
    #     /     \
    #   -3       4
    #   / \     / \
    # -5  -1   2   6
    def create_balanced_bst_with_negatives():
        root = Node(0)
        root.left = Node(-3)
        root.right = Node(4)
        root.left.left = Node(-5)
        root.left.right = Node(-1)
        root.right.left = Node(2)
        root.right.right = Node(6)
        return root

    # Example 3: A skewed binary tree with negative numbers (left-skewed)
    #   -1
    #   /
    # -2
    # /
    # -3
    #  /
    # -4
    def create_skewed_tree_with_negatives():
        root = Node(-1)
        root.left = Node(-2)
        root.left.left = Node(-3)
        root.left.left.left = Node(-4)
        return root

    # Example 4: A complete binary tree with mixed positive and negative numbers
    #        0
    #     /     \
    #   -2       2
    #   / \     / \
    # -4   -3  1   3
    def create_complete_tree_with_negatives():
        root = Node(0)
        root.left = Node(-2)
        root.right = Node(2)
        root.left.left = Node(-4)
        root.left.right = Node(-3)
        root.right.left = Node(1)
        root.right.right = Node(3)
        return root

    # Example 5: An empty tree
    def create_empty_tree():
        return None

    # Example 6: A one-node tree with a negative number
    def create_one_node_negative_tree():
        return Node(-1)

    test_cases = [
        (create_empty_tree(), sys.maxsize),
        (create_one_node_negative_tree(), -1),
        (create_complete_tree_with_negatives(), -4),
        (create_skewed_tree_with_negatives(), -4),
        (create_balanced_bst_with_negatives(), -5),
        (create_simple_tree_with_negatives(), -4),
    ]

    test_implementation(tree_min_iterative, test_cases)
    test_implementation(tree_min_recursive, test_cases)
