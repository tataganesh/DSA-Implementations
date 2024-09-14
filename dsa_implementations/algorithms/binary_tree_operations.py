"""
Reference  - https://www.youtube.com/watch?v=fAAZixBzIAI
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any
from dsa_implementations.data_structures.stack import Stack


@dataclass
class Node:
    """Represent node in a binary tree"""

    val: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def depth_first_values_iterative(root: Node) -> list[Any]:
    """Print the depth-wise traversal of a binary tree

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
