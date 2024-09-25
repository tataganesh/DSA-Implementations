from __future__ import annotations
from typing import Optional, Any
from dataclasses import dataclass
from dsa_implementations.data_structures.circular_queue import CircularQueue
from collections import deque


@dataclass
class Node:
    """Represent node in a binary tree"""

    val: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def tree_includes(root, target) -> bool:
    if not root:  ## Negative case
        return False
    if root.val == target:  ## Affirmative case
        return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)


def tree_sum(root) -> int:
    # Base case: None node should return 0
    if not root:
        return 0
    # Treating each sub probklem separately, the sum of the treee
    # represented by root is sum(left_subtree) + root_value + sum(right_subtree)
    return root.val + tree_sum(root.left) + tree_sum(root.right)


def tree_sum_iterative(root) -> int:
    # Base case: None node should return 0
    if not root:
        return 0
    # Let's do a breadth-first traversal
    queue = CircularQueue(capacity=1000)
    queue.push(root)
    total_sum = 0
    # Iterate till queue is empty -> We traverse each level of tree
    while queue.size():
        popped_node = queue.pop()
        total_sum += popped_node.val
        if popped_node.left:
            queue.push(popped_node.left)
        if popped_node.right:
            queue.push(popped_node.right)
    return total_sum


def tree_sum_iterative_deque(root) -> int:
    # Base case: None node should return 0
    if not root:
        return 0
    # Let's do a breadth-first traversal
    queue: deque = deque([])
    queue.append(root)
    total_sum = 0
    # Iterate till queue is empty -> We traverse each level of tree
    while len(queue):
        popped_node = queue.popleft()
        total_sum += popped_node.val
        if popped_node.left:
            queue.append(popped_node.left)
        if popped_node.right:
            queue.append(popped_node.right)
    return total_sum


if __name__ == "__main__":
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

    print(tree_includes(create_complete_tree(), 7))

    recursive_sum = tree_sum(create_complete_tree())
    iterative_sum = tree_sum_iterative_deque(create_complete_tree())
    print(recursive_sum, iterative_sum)
    assert (
        recursive_sum == iterative_sum
    ), "Recusive and iterative tree_sum functions do not match"
