from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any
import sys


@dataclass
class Node:
    """Represent node in a binary tree"""

    val: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def max_root2leaf_sum(root) -> int:
    if not root:
        return -sys.maxsize
    if not (root.left or root.right):
        return root.val
    left_max_root2leaf_sum = max_root2leaf_sum(root.left)
    right_max_root2leaf_sum = max_root2leaf_sum(root.right)
    return root.val + max(left_max_root2leaf_sum, right_max_root2leaf_sum)


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
        (create_empty_tree(), -sys.maxsize),
        (create_one_node_negative_tree(), -1),
        (create_complete_tree_with_negatives(), 5),
        (create_skewed_tree_with_negatives(), -10),
        (create_balanced_bst_with_negatives(), 10),
        (create_simple_tree_with_negatives(), 6),
    ]

    for root, expected_min_value in test_cases:
        minimum_node_value = max_root2leaf_sum(root)
        assert (
            minimum_node_value == expected_min_value
        ), f"Expected: {expected_min_value}, Received: {minimum_node_value}"
